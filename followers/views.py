from django.conf import settings
from rest_framework import generics, permissions, response,  views
from .models import Follower
from .serializers import ListFollowerSerializer
from profiles.models import UserProfile


class ListFollowerView(generics.ListAPIView):
    """ Output list of subscribers """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListFollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)


class AddFollowerView(views.APIView):
    """ Adding to subscriber"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user = UserProfile.objects.filter(id=pk)
        if user.exists():
            Follower.objects.create(subscriber=request.user, user=user)
            return response.Response(status=201)
        return response.Response(status=404)    