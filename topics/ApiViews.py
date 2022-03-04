from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Topic
from .serializers import AssignmentSerializer, TopicSerializer
from rest_framework import permissions
from utils.httpResponse import HttpResponse


class AllTopics(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request):
        all_topics = Topic.objects.all().order_by('-id')
        serializer = TopicSerializer(all_topics, many=True)

        return HttpResponse.success("Topics retrieved successfully",{
            "topics":serializer.data
        })

    def post(self, request):
        title = request.data.get("title")
        description = request.data.get("description")
        address_link = request.data.get("address_link")

        if not title:
            return HttpResponse.error("Please enter topic title")
        data = {"title": title}

        if address_link:
            data["address_link"] = address_link

        if description:
            data["description"] = description

        serializer = TopicSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse.success("Topic created successfully", data=serializer.data)
        else:
            return HttpResponse.error(serializer.error_messages)

    def delete(self,request, topicID):
        try:
            topic = Topic.objects.get(id= int(topicID))
        except Topic.DoesNotExist as e:
            return HttpResponse.error("Topic does not exist")
        
        topic.delete()
        return HttpResponse.success("Topic deleted successfully")


class Assignment(APIView):
    def post(self, request):
        title = request.data.get("title")
        address_link = request.data.get("address_link")
        topic_id = request.data.get("topic_id")
        description = request.data.get("description")


        if not title:
            return HttpResponse.error("Please enter topic title")

        if not topic_id:
            return HttpResponse.error("No Topic specified")
        
        data = {"title":title}

        if address_link:
            data["address_link"] = address_link

        if description:
            data["description"] = description
        
        try :
            topic = Topic.objects.get(id= int(topic_id))
            data["topic"] = topic.id
        except Topic.DoesNotExist as e:
            return HttpResponse.error("Sorry, the specified topic does not exist")

        serializer = AssignmentSerializer(data = data )

        if serializer.is_valid():
            serializer.save()
            return HttpResponse.success("Assignment created successfully", { "resource": serializer.data})
        else:
            return HttpResponse.error(serializer.error_messages)


class CreateAssignment(APIView):
    def get(self, request, topicID):
        pass