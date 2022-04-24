from .models import User, UserPaymentManager, Profile
from rest_framework import serializers
from companies.serializers import CompanySerializer


class UserPaymentManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPaymentManager
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    payment = UserPaymentManagerSerializer(read_only=True)
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "password", "slug", "is_super",
                  "is_active", "is_admin", "is_staff", "company", "payment","phoneNumber","profile", "username"]
