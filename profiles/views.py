from django.shortcuts import get_object_or_404
from .models import UserProfile
from .serializers import GetUserProfileSerializer, GetUserProfilePublicSerializer
from rest_framework import permissions, generics, response, mixins
from rest_framework.viewsets import ModelViewSet

from profiles import serializers

class UserProfilePublicView(ModelViewSet):
    """Output public user profile """
    queryset = UserProfile.objects.all()
    serializer_class = GetUserProfilePublicSerializer
    permission_classes = [permissions.AllowAny] # AllowAny доступ будет у всех


class UserProfilePrivateView(generics.RetrieveAPIView):
    """ Output user's profile or Updateing Profile """
    serializer_class = GetUserProfileSerializer
    permission_classes = [permissions.IsAuthenticated] # only authorized users can edit

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

    def get_object(self):
        obj = get_object_or_404(self.get_queryset())
        self.check_object_permissions(self.request, obj)
        return obj 
