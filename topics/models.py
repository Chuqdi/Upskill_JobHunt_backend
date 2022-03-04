from pyexpat import model
from django.db import models
from django.utils import timezone

class Topic(models.Model):
    title = models.TextField(null=False, blank=False, unique=True)
    description = models.TextField(null=True, blank=True)
    address_link = models.TextField(null=True, blank=True)
    material_type = models.TextField(default="topic")
    created_on = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title


class Assignment(models.Model):
    title = models.TextField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    address_link = models.TextField(null=True, blank=True)
    material_type = models.TextField(default="assignment")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="assignment")
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
