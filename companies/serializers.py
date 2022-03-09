from rest_framework import serializers
from .models import Company



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields ="__all__"
        depth=2
        read_on_fields = ("registered_by",)