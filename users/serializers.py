from .models import User, UserPaymentManager
from rest_framework import  serializers
from companies.serializers import CompanySerializer




class UserPaymentManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserPaymentManager
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    payment = UserPaymentManagerSerializer()
    class Meta:
        model =User
        fields = ["email", "full_name", "age","slug", "is_super", "is_active", "is_admin", "is_staff", "company", "payment"]