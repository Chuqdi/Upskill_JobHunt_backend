
from django.urls import path
from .ApiViews import AllTopics, Assignment


urlpatterns = [
    path("", AllTopics.as_view(), name="all_topics"),
    path("topic/", AllTopics.as_view(), name="add_topics"),
    path("assignment/", Assignment.as_view(), name="assignment")
]
