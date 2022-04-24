
from ast import arg
from django.http import JsonResponse
from rest_framework.views import APIView
from redisManager import RedisManager
from users.serializers import UserSerializer
from utils.AllowedCompanyPlans import ALLOWED_COMPANY_PLANS
from utils.Frontend import FRONTEND_DOMAIN
from utils.UserSlugManager import UserSlugManager
from .models import Company, User
from django.contrib.auth.hashers import make_password, check_password
from utils.httpResponse import HttpResponse
from utils.JWTTokenManager import UserTokenManager
from utils.SendMail import SendEmail
from utils.RandomStrings import GenerateRandomString
from threading import Thread
from django.core.validators import EmailValidator
from .serializers import CompanySerializer
from knox.models import AuthToken
from rest_framework import permissions




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



class RegisterCompany(APIView):
    
    def post(self, request):
        company_name = request.data.get("company_name")
        company_email_address = request.data.get("company_email_address")
        company_password = request.data.get("company_password")
        company_type= request.data.get("company_type")
        company_phoneNumber = request.data.get("company_phoneNumber")



        
        if not company_name:
            return HttpResponse.error("Please enter the company name")

        if not company_email_address:
            return HttpResponse.error("Please enter company email address")
        if not company_password:
            return HttpResponse.error("Please enter company password")
        if not company_type:
            return HttpResponse.error("Please enter company type")

        if not company_phoneNumber:
            return HttpResponse.error("Please enter company phone Number")

        try:
            EmailValidator()(company_email_address)
        except Exception as e:
            return HttpResponse.error("Sorry, your email is not valid")

        

        try:
            u = User.object.get(email=company_email_address)
            return HttpResponse.error("Email already registered")
        except User.DoesNotExist as e:
            pass

        try:
            u = User.object.get(phoneNumber=company_phoneNumber)
            return HttpResponse.error("Phone Number already registered")
        except User.DoesNotExist as e:
            pass

            
        slug = UserSlugManager().generateUserSlug()

        dataUser = {"email":company_email_address,"username":company_name,"is_active":True,"phoneNumber":company_phoneNumber,"slug":slug, "password": make_password(company_password)}




        serializerUser = UserSerializer(data=dataUser)
        
        

        if serializerUser.is_valid():
            u = serializerUser.save()


            # START REGISTERING COMPANY
            c = Company.objects.create(
                company_name=company_name,
                company_slug= UserSlugManager().generateUserSlug(),
                company_area_of_interest=company_type,
                registered_by = u
            )

            serializerCompany = CompanySerializer(Company.objects.get(id=c.id))
            sendUserAcctEmail = Thread(target=sendCompanyEmail, args=(request,u, 'emails/UserAccountActivation.html'))
            sendUserAcctEmail.start()
            data = {"company": serializerCompany.data}
            return HttpResponse.success("Company created successfully, please check your email to active company  account", data)
            
            
            
        else:
            return JsonResponse({ "userError": serializerUser.error_messages}, status=400)
        



class LoginCompany(APIView):
    def post(self, request):
        company_email = request.data.get("company_email")
        company_password = request.data.get("company_password")
        if not company_email:
            return HttpResponse.error("Please enter  company email")
        if not company_password:
            return HttpResponse.error("Please enter  company password")

        try:
            u = User.object.get(email=company_email)
            if u.email == company_email:
                if check_password(company_password, u.password):
                    
                    if u.is_active:
                        try:
                            company = u.company
                        except Exception as e:
                            return HttpResponse.error("A company is not registered here")
                        # if company.company_is_active:
                        token = AuthToken.objects.create(u)
                        data ={
                            "company": CompanySerializer(company).data,
                            "token":token[1],
                        }
                        return HttpResponse.success("Company LoggedIn Successfully", data)
                        # else:
                        #     return HttpResponse.error("Company has not yet paid for a plan  account not activated")



                    else:
                        return HttpResponse.error("Company Email not yet activated")
                else:
                    return HttpResponse.error("Please check  company password")

            else:
                return HttpResponse.error("Company Email is not correct, try again")


        except User.DoesNotExist as e:
            return HttpResponse.error("Company with this Email does not exist does not exist.")


class UpdateProfile(APIView):
    # permission_classes =[permissions.IsAuthenticated]


    def put(self, request, companyID):
        company_name = request.data.get("company_name")
        company_address = request.data.get("company_address")
        company_area_of_interest = request.data.get("company_area_of_interest")
        company_mobile_contact = request.data.get("company_mobile_contact")
        company_email_address = request.data.get("company_email_address")



        
        if not company_name:
            return HttpResponse.error("Please enter the company name")
        if not company_address:
            return HttpResponse.error("Please enter the company address")

        
        if not company_area_of_interest:
            return HttpResponse.error("Please enter the company area of interest")
        if not company_mobile_contact:
            return HttpResponse.error("Please enter the company mobile contact")
        if not company_email_address:
            return HttpResponse.error("Please enter company email address")


        try:
            co = Company.objects.get(id=companyID)

        except Company.DoesNotExist as e:
            return HttpResponse.error("Company ID does not match a query object")
        c1 = CompanySerializer(co, { 
            "company_name":company_name,
            "company_address":company_address,
            "company_area_of_interest":company_area_of_interest,
            "company_mobile_contact":company_mobile_contact,

        }, partial=True)

        if c1.is_valid():
            user = co.registered_by
            user.email = company_email_address
            user.save()
            c= c1.save()
            
            return HttpResponse.success("Company Credentials Updated Successfully", {
                "company":CompanySerializer(co).data
            })
        return HttpResponse.error("Error Updating Company Profile")
        
        


class UpdateCompanyPlan(APIView):
     
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def patch(self, request):
        company_id = request.data.get("company_id")
        company_current_plan = request.data.get("company_current_plan")
        if not company_id:
            return HttpResponse.error("Please enter  company ID")

        try:
            c= Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return HttpResponse.error("Company With this ID does not Exist")
        
        if not company_current_plan in ALLOWED_COMPANY_PLANS:
            return HttpResponse.error("Specified Plan Not Allowed")


        data = {
            "company_current_plan":company_current_plan,
            "company_is_active": True
        }
        serializer = CompanySerializer(instance=c, data=data, partial=True)
        if serializer.is_valid():
            c = serializer.save()
            t = Thread(target=sendCompanyEmail, args =(request, c,"emails/CompanyPaymentCompleted.html"))
            t.start()
            data ={
                "company": serializer.data,
            }
            return HttpResponse.success("Company Plan Updated Successfully", data)
        return HttpResponse.error("Error Updating Company Plan")

    





class GetCompanyFromSlug(APIView):
    def get(self, request, slug):
        print(slug)
        c = Company.objects.filter(company_slug=slug)
        if len(c) > 0:
            c=c[0]
            token = AuthToken.objects.create(c.registered_by)
            data ={
                "company": CompanySerializer(c).data,
                "token":token[1],
            }
            return HttpResponse.success("Company retrieved Successfully", data)

        else:
            return HttpResponse.error("Company with this slug does not exist.")



def sendCompanyEmail(request, user, template):
    tokenGen = UserTokenManager()
    tokenGenerated = tokenGen.generateToken(user)
    activationLink = FRONTEND_DOMAIN+"user/emailActivation/"+tokenGenerated
    
    email = SendEmail(template,"Company Account Activation",{"activationLink":activationLink, "company_account": True }, user.email)
    email.send()
