
import os
from django.contrib import admin
from django.urls import path, include
from users.ApiViews import TestApi
from django.http import FileResponse
from django.conf import settings



def getFavicon(request):
    path = os.path.join(settings.BASE_DIR, "static/favicon.ico")
    response = FileResponse(open(path, 'rb'))
    return response

urlpatterns = [
    path("test", TestApi.as_view(), name="testApi"),
    path('admin/', admin.site.urls),
    path("favicon.ico", getFavicon),
    path("users/", include("users.urls")),
    path("topics/", include("topics.urls")),
    path("companies/", include("companies.urls"))
]
