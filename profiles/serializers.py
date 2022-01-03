from os import write
from django.db import models
from rest_framework import serializers
from .models import UserProfile


class GetUserProfileSerializer(serializers.ModelSerializer):
    """Info about user"""

    avatar = serializers.ImageField(write_only=True)
    class Meta:
        model = UserProfile
        exclude = (
            "password", 
            "last_login",
             "is_active", 
             "is_staff", 
             "is_superuser",
              "groups",
               "user_permissions"
               )


class GetUserProfilePublicSerializer(serializers.ModelSerializer):
    """Info about user"""
    class Meta:
        model = UserProfile
        exclude = (
            "email", 
            "phone",
            "password",
             "last_login", 
             "is_active", 
             "is_staff",
              "is_superuser", 
              "groups", 
              "user_permissions"
              )
        
