
import os
from django.contrib import admin
from django.urls import path, include
from users.ApiViews import TestApi
from django.http import FileResponse, JsonResponse
from django.conf import settings



def getFavicon(request):
    path = os.path.join(settings.BASE_DIR, "static/favicon.ico")
    response = FileResponse(open(path, 'rb'), status =200)
    return response


def home(request):
    return JsonResponse({"welcome":"Owerri Job Hunt API"})
urlpatterns = [
    path("", home, name="home",),
    path("test", TestApi.as_view(), name="testApi"),
    path('admin/', admin.site.urls),
    path("favicon.ico", getFavicon),
    path("api/user/candidate/", include("users.urls")),
    path("topics/", include("topics.urls")),
    path("api/user/company/", include("companies.urls")),
    path("api/job/", include("jobs.urls"))
]



# path("users/", include("users.urls")),
#     path("topics/", include("topics.urls")),
#     path("companies/", include("companies.urls"))