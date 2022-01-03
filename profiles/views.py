from .models import UserProfile
from .serializers import GetUserProfileSerializer, GetUserProfilePublicSerializer
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

class UserProfilePublicView(ModelViewSet):
    """Output public user profile """
    queryset = UserProfile.objects.all()
    serializer_class = GetUserProfilePublicSerializer
    permission_classes = [permissions.AllowAny] # AllowAny доступ будет у всех


class UserProfileView(ModelViewSet):
    """ Updateing Profile """
    serializer_class = GetUserProfileSerializer
    permission_classes = [permissions.IsAuthenticated] # only authorized users can edit

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)
