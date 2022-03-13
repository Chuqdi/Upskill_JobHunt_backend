from django.http import JsonResponse
from rest_framework.views import APIView
from redisManager import RedisManager

from utils.Frontend import FRONTEND_DOMAIN
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password, check_password
from knox.models import AuthToken
from utils.httpResponse import HttpResponse
from utils.JWTTokenManager import UserTokenManager
from utils.SendMail import SendEmail
from utils.RandomStrings import GenerateRandomString
from django.contrib.sites.shortcuts import get_current_site
from threading import Thread
from django.contrib.auth import logout
from django.core.validators import EmailValidator
from utils.UserSlugManager import UserSlugManager





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
        full_name = request.data.get("fullName")
        email = request.data.get("email")
        age = request.data.get("age")
        password = request.data.get("password")

        
        
        if not email:
            return HttpResponse.error("Please enter an email")
        if not password:
            return HttpResponse.error("Please enter a password")
        if not full_name:
            return HttpResponse.error("Please enter a full name")
        if not age:
            return HttpResponse.error("Please enter age")

        try:
            EmailValidator()(email)
        except Exception as e:
            return HttpResponse.error("Sorry, your email is not valid")

        

        try:
            u = User.object.get(email=email)
            return HttpResponse.error("Email already registered")
        except User.DoesNotExist as e:
            pass

            
        slug = UserSlugManager().generateUserSlug()

        data = {"email":email, "full_name":full_name, "age":age,"slug":slug, "password": make_password(password)}

        serializer = UserSerializer(data=data)
        
        

        if serializer.is_valid():
            serializer.save()
            u = User.object.get(email=email)
            data = {
                "user":serializer.validated_data,
            }
            sendUserAcctEmail = Thread(target=sendUserAccountActivationEmail, args=(request,u))
            sendUserAcctEmail.start()
            return HttpResponse.success("User created successfully, please check your email to active your account", data)
        
        print(serializer.errors)
        return HttpResponse.error("Error Registering User")


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
                print(password)
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






def sendUserAccountActivationEmail(request, user):
    tokenGen = UserTokenManager()
    tokenGenerated = tokenGen.generateToken(user)
    activationLink = FRONTEND_DOMAIN+"users/user-email-activation/"+GenerateRandomString.randomStringGenerator(40)+"/"+tokenGenerated+"/"+GenerateRandomString.randomStringGenerator(20)
    
    email = SendEmail('emails/UserAccountActivation.html',"User Account Activation",{"activationLink":activationLink}, user.email)
    email.send()



def sendUserForgotPasswordEmail(request, user):
    tokenGen = UserTokenManager()
    tokenGenerated = tokenGen.generateToken(user)
    activationLink = FRONTEND_DOMAIN+"users/user-forgot-password-complete/"+GenerateRandomString.randomStringGenerator(40)+"/"+tokenGenerated+"/"+GenerateRandomString.randomStringGenerator(20)
    
    email = SendEmail('emails/UserPasswordChange.html',"User Password Change",{"activationLink":activationLink}, user.email)
    email.send()



