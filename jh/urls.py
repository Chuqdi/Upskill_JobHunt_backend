
from django.contrib import admin
from django.urls import path, include
from users.ApiViews import TestApi

urlpatterns = [
    path("test", TestApi.as_view(), name="testApi"),
    path('admin/', admin.site.urls),
    path("users/", include("users.urls"))
]
