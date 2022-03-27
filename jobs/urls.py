from django.urls import path
from .ApiViews import CreateJob

urlpatterns = [
    path("create",CreateJob.as_view(), name="createJob")
]
