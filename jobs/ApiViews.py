from rest_framework.views import APIView
from .serializers import JobSerializer
from .models import Job
from rest_framework import permissions
from utils.httpResponse import HttpResponse



NATURE_OF_JOB_TYPES =[ "REMOTE", "PHYSICAL", "HYBRID"]
GENDER_TYPES =[ "MALE", "FEMALE", "CUSTOM"]

class CreateJob(APIView):
    permission_classes =[
        permissions.IsAuthenticated
    ]

    def post(self, request):
        company_name = request.data.get("company_name")
        company_location = request.data.get("company_location")
        nature_of_job = request.data.get("nature_of_job")
        skills = request.data.get("skills")
        gender = request.data.get("gender")
        age_bracket = request.data.get("age_bracket")
        years_of_experience = request.data.get("years_of_experience")
        job_description = request.data.get("job_description")
        other_benefits = request.data.get("other_benefits")
        salary_range = request.data.get("salary_range")
        application_deadline = request.data.get("application_deadline")

        
        if not company_name:
            return HttpResponse.error("Please enter company name")

        if not company_location:
            return HttpResponse.error("Please enter company location")
        
        if not nature_of_job:
            return HttpResponse.error("Please enter the nature of job")

        if not skills:
            return HttpResponse.error("Please enter required skills")
        

        if not gender:
            return HttpResponse.error("Please enter  gender")
        

        if not age_bracket:
            return HttpResponse.error("Please enter age bracket")

        if not years_of_experience:
            return HttpResponse.error("Please enter required years of experience")

        if not job_description:
            return HttpResponse.error("Please enter job description ")

        if not other_benefits:
            return HttpResponse.error("Please enter  other benefit")

        if not salary_range:
            return HttpResponse.error("Please enter  salary range")
        
        if not application_deadline:
            return HttpResponse.error("Please enter  application deadline")


        if nature_of_job in NATURE_OF_JOB_TYPES:
            return HttpResponse.error("Please choosing an allowed job nature ")
        
        if gender in GENDER_TYPES:
            return HttpResponse.error("Please choosing an allowed job nature ")
        

        data ={
            "company_name":company_name,
            "company_location":company_location,
            "nature_of_job":nature_of_job,
            "skills":skills,
            "gender":gender,
            "age_bracket":age_bracket,
            "years_of_experience":years_of_experience,
            "job_description":job_description,
            "other_benefits":other_benefits,
            "salary_range":salary_range,
            "application_deadline":application_deadline,
            "isBusiness": not request.user.is_admin,
            "isAdmin":request.user.is_admin
        }

        serializer = JobSerializer(data=data)

        if serializer.is_valid():
            s = serializer.save()
            data ={
                "job":s
            }

            return HttpResponse.success("Job Created successfully", data)

    def delete(self, request, ID):
        try:
            job = Job.objects.get(id=ID)
        except Job.DoesNotExist as e:
            return HttpResponse.error("Job ID does not match any query")
        
        return HttpResponse.success("Job deleted successfully")

