from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Assignment, Topic


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"


class TopicSerializer(serializers.ModelSerializer):
    assignment = AssignmentSerializer(read_only=True, many=True)
    class Meta:
        model = Topic
        fields = ['id','description', 'assignment', 'title']
       
