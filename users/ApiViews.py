from re import sub
from django.http import JsonResponse
from rest_framework.views import APIView
from redisManager import RedisManager

from utils.Frontend import FRONTEND_DOMAIN
from .models import Sponsor, User, UserPaymentManager, Profile
from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth.hashers import make_password, check_password
from knox.models import AuthToken
from utils.httpResponse import HttpResponse
from utils.JWTTokenManager import UserTokenManager
from utils.SendMail import SendEmail
from utils.RandomStrings import GenerateRandomString
from threading import Thread
from django.contrib.auth import logout
from utils.UserSlugManager import UserSlugManager
from rest_framework import permissions, parsers
from utils.Validators import Validate
from rest_framework.viewsets import ModelViewSet



class UpdateUserProfile(APIView):
    permission_classes =[permissions.IsAuthenticated]
    parser_classes = [ parsers.FormParser, parsers.MultiPartParser]
    def put(self, request):
        
        twitterHandle = request.data.get("twitterHandle")
        facebookHandle = request.data.get("facebookHandle")
        linkedInHandle = request.data.get("linkedInHandle")
        
        if twitterHandle:
            if not Validate.validateUrl(twitterHandle):
                return HttpResponse.error("Please enter a valid URL address.Following this format https://www.owerrijobhunt.ng")

        if facebookHandle:
            if not Validate.validateUrl(facebookHandle):
                return HttpResponse.error("Please enter a valid URL address.Following this format https://www.owerrijobhunt.ng")

        if linkedInHandle:
            if not Validate.validateUrl(linkedInHandle):
                return HttpResponse.error("Please enter a valid URL address.Following this format https://www.owerrijobhunt.ng")

        data = request.data.dict()
        for i in data.copy():
            if not data[i]:
                data.pop(i)
        
        
        

        instance = request.user.profile

        

        serializer = ProfileSerializer(data=data, instance = instance, partial=True)

        if serializer.is_valid():
            s = serializer.save()
            return HttpResponse.success("User Profile Updated Successfully", data = serializer.data)
        print(serializer.errors)
        return HttpResponse.error("Error Updating User Profile")






class TestApi(APIView):
    def get(self, request):
        CACHE_KEY ="CACHE_KEY"
        cached_data = RedisManager().get(CACHE_KEY)
        if not cached_data:
            users = list(User.object.values())
            RedisManager().set(CACHE_KEY, data)
            return JsonResponse(users, safe=False)
        else:
            return JsonResponse(cached_data, safe=False)



class RegisterUser(APIView):
    def get(self, request):
        s = UserSerializer(User.object.all(), many=True)
        return HttpResponse.success("User", data={"morgan":"dhdd"})
    
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        username = request.data.get("username")
        phoneNumber = request.data.get("phoneNumber")

        
        
        if not email:
            return HttpResponse.error("Please enter an email")
        if not password:
            return HttpResponse.error("Please enter a password")
        if not username:
            return HttpResponse.error("Please enter a Username")
        if not phoneNumber:
            return HttpResponse.error("Please enter your phone number")
   

        if not Validate.validateEmail(email):
            return HttpResponse.error("Please enter a valid email")



        

        try:
            u = User.object.get(email=email)
            return HttpResponse.error("Email already registered")
        except User.DoesNotExist as e:
            pass

        try:
            u = User.object.get(username=username)
            return HttpResponse.error("Username already registered, please choose another.")
        except User.DoesNotExist as e:
            pass

        try:
            u = User.object.get(phoneNumber=phoneNumber)
            return HttpResponse.error("Phone Number already registered, please choose another.")
        except User.DoesNotExist as e:
            pass

            
        slug = UserSlugManager().generateUserSlug()

        data = {"email":email,"username":username,"phoneNumber":phoneNumber,"slug":slug, "password": make_password(password)}

        serializer = UserSerializer(data=data)
        
        

        if serializer.is_valid():
            serializer.save()
            u = User.object.get(email=email)
            data = {
                "user":UserSerializer(u).data,
            }
            sendUserAcctEmail = Thread(target=sendUserAccountActivationEmail, args=(request,u))
            sendUserAcctEmail.start()
            return HttpResponse.success("User created successfully, please check your email to active your account", data)
        
        return HttpResponse.error("Error Registering User")




class UpdateProfile(APIView):
    permission_classes=[ permissions.IsAuthenticated ]
    def put(self, request):
        email = request.data.get("email")
        username = request.data.get("username")

        if not email:
            return HttpResponse.error("Please enter an email")

        if not username:
            return HttpResponse.error("Please enter your username")


       

        data = {"email":email, "username":username}

        serializer = UserSerializer(request.user, data=data, partial=True)
        
        

        if serializer.is_valid():
            serializer.save()
            u = User.object.get(email=email)
            data = {
                "user":UserSerializer(u).data,
            }
            sendUserAcctEmail = Thread(target=sendUserAccountActivationEmail, args=(request,u))
            sendUserAcctEmail.start()
            return HttpResponse.success("User profile Updated successfully", data)
        
        return HttpResponse.error("Error Updating User Profile User")

class Login(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        if not email:
            return HttpResponse.error("Please enter an email")
        if not password:
            return HttpResponse.error("Please enter a password")

        try:
            u = User.object.get(email=email)
            if u.email == email:
                if check_password(password, u.password):
                    token = AuthToken.objects.create(u)
                    data ={
                        "user": UserSerializer(u).data,
                        "token":token[1],
                    }
                    if u.is_active:
                        return HttpResponse.success("User LoggedIn Successfully", data)
                    else:
                        return HttpResponse.error("User account not activated")
                else:
                    return HttpResponse.error("Please check your password")

            else:
                return HttpResponse.error("Email is not correct, try again")


        except User.DoesNotExist as e:
            return HttpResponse.error("User with this email does not exist.")


class UpdateUserPayment(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def patch(self, request):
        userID = request.data.get("userID")

        if not userID:
            return HttpResponse.error("Please enter user ID")
        users = User.object.filter(id= userID)
        if len(users) > 0:
            user = users[0]
            payment = UserPaymentManager.objects.get(user= user.id)
            payment.is_paid = True
            payment.save()
            
            return HttpResponse.success("User Payment Updated Successfully")

        else:
            return HttpResponse.error("User With This ID does not exist")
        pass

class GetUserFromSlug(APIView):
    def get(self, request, slug):
        try:
            u = User.object.get(slug=slug)
            token = AuthToken.objects.create(u)
            data ={
                "user": UserSerializer(u).data,
                "token":token[1],
            }
            if u.is_active:
                return HttpResponse.success("User retrieved Successfully", data)
            else:
                return HttpResponse.error("User account not activated")

           

        except User.DoesNotExist as e:
            return HttpResponse.error("User with this slug does not exist.")

def resendUserRegisterationEmail(request, userID):
    users = User.object.filter(id=userID)
    if len(users) > 0:
        user = users[0]
        t = Thread(target=sendUserAccountActivationEmail, args=( request,user ))
        t.start()
        return HttpResponse.success("User Activation Email Sent Successfully")
    
    return HttpResponse.error("Please user ID does not exist")



    

class LogoutUser(APIView):
    def post(self, request):
        logout(request=request)
        return HttpResponse.success("User Logged Out Successfully")



class UserForgotPassword(APIView):
    def post(self, request):
        logout(request)
        email = request.data.get("email")

        if not email:
            return HttpResponse.error("Please enter your email")


        try:
            u =User.object.get(email=email)
        except User.DoesNotExist as e:
            return HttpResponse.error("User with this email does not exist.")
        t = Thread(target=sendUserForgotPasswordEmail, args=(request, u))
        t.start()
        return HttpResponse.success("Please check your email to continue")


class CompleteUserForgotPassword(APIView):
    def patch(self, request):
        token = request.data.get("token")
        newPassword = request.data.get("password")

        if not token:
            return HttpResponse.error("No Token Found.")
        if not newPassword:
            return HttpResponse.error("User Password was not specified.")

        tokenManager = UserTokenManager()
        res = tokenManager.decodeToken(token)
        if  res.get("state"):
            u = res.get("user")
            data = {"password": make_password(newPassword)}
            serialiser = UserSerializer(instance=u, data=data, partial=True)
            if serialiser.is_valid():
                serialiser.save()
                return HttpResponse.success("User password updated succesfully",{"user":UserSerializer(u).data})
            return JsonResponse({"error":serialiser.errors})
        else:
            return HttpResponse.error(res.get("message"))

class CreateSponsor(APIView):
    def post(self, request):
        website = request.data.get("website")
        email = request.data.get("email")

        if not email:
            return HttpResponse.error("Please enter Sponsors email")
        if not website:
            return HttpResponse.error("Please enter Sponsors website address.")

        if not Validate.validateEmail(email):
            return HttpResponse.error("Please enter a valid email")

        if not Validate.validateUrl(website):
            return HttpResponse.error("Please enter a valid URL address.Following this format https://www.owerrijobhunt.ng")
        
        sponsors = Sponsor.objects.filter(email=email)

        if len(sponsors) > 0:
            return HttpResponse.error("This Email Is alread registered as a sponsor")


        sponsors = Sponsor.objects.filter(website=website)
        if len(sponsors) > 0:
            return HttpResponse.error("This Website Is alread registered as a sponsor")

            
        sponsor = Sponsor.objects.create(email = email, website=website)
        return HttpResponse.success("Sponsorship added, we will contact u very soon")

class SendUserContactUsEmail(APIView):
    def post(self, request):
        name = request.data.get("name")
        email = request.data.get("email")
        subject = request.data.get("subject")
        message = request.data.get("message")

        if not name:
            return HttpResponse.error("Please enter your name ")

        if not email:
            return HttpResponse.error("Please enter your email ")
        if not subject:
            return HttpResponse.error("Please enter your subject ")
        if not message:
            return HttpResponse.error("Please enter your message ")
        data = {
            "name":name,
            "email":email,
            "subject":subject,
            "message":message
        }
        t =Thread(target=sendUserContactUsEmail, args =(data,))
        t.start()
        return HttpResponse.success("Thanks For Contacting Us We will reply you soon, if need be")




class TestUser(APIView):
    def get(self, request):
        user = User.object.first()
        return HttpResponse.success(data={"user":UserSerializer(user).data}, message="hdggd")

def CompleteUserAccountActivation(request, token):
    tokenManager = UserTokenManager()
    res = tokenManager.decodeToken(token)
    if  res.get("state"):
        u = res.get("user")
        u.is_active = True
        u.save()
        return HttpResponse.success("User account activated succesfully",{"user":UserSerializer(u).data})
    else:
        return HttpResponse.error(res.get("message"))

        


def sendUserContactUsEmail(data):
    email = SendEmail('emails/ContactUsEmail.html',"User Contact Us-owerrijobhunt.ng",data, "morganhezekiah11@gmail.com")
    email.send()

def sendUserAccountActivationEmail(request, user):
    tokenGen = UserTokenManager()
    tokenGenerated = tokenGen.generateToken(user)
    activationLink = FRONTEND_DOMAIN+"user/emailActivation/"+tokenGenerated
    
    email = SendEmail('emails/UserAccountActivation.html',"User Account Activation",{"activationLink":activationLink}, user.email)
    email.send()



def sendUserForgotPasswordEmail(request, user):
    tokenGen = UserTokenManager()
    tokenGenerated = tokenGen.generateToken(user)
    activationLink = FRONTEND_DOMAIN+"users/user-forgot-password-complete/"+GenerateRandomString.randomStringGenerator(40)+"/"+tokenGenerated+"/"+GenerateRandomString.randomStringGenerator(20)
    
    email = SendEmail('emails/UserPasswordChange.html',"User Password Change",{"activationLink":activationLink}, user.email)
    email.send()



