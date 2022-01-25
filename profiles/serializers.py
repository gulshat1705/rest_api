from os import write
from rest_framework import serializers
from .models import UserProfile


class GetUserProfileSerializer(serializers.ModelSerializer):
    """Info about user"""

    # avatar = serializers.ImageField(write_only=True)
    class Meta:
        model = UserProfile
        exclude = (
            "id",
            "password", 
            "email",
            "avatar",
            "first_login",
            "last_login",
            "is_active", 
            "is_staff", 
            "is_superuser",
            "groups",
            "user_permissions",
            "date_joined",

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
        

class UserByFollowerSerializer(serializers.ModelSerializer):
    """ Serializer for subscriber """

    avatar = serializers.ImageField(read_only=True)
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'avatar')