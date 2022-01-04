from rest_framework import permissions, generics, serializers

from base.classes import CreateRetrieveUpdateDestroy, CreateUpdateDestroy
from base.permissions import IsAuthor
from .models import Post, Comment
from .serializers import PostSerializer, CreateCommentSerializer, ListPostSerializer


class PostListView(generics.ListAPIView):
    """ List of post for user wall's """
    serializer_class = ListPostSerializer

    def get_queryset(self):
        return Post.objects.filter(user_id=self.kwargs.get('pk'))


class PostView(CreateRetrieveUpdateDestroy):
    """ CRUD posts """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_classes = PostSerializer
    permission_classes_by_action = {'get': [permissions.AllowAny],
                                    'update': [IsAuthor], # if author he can update, delete post
                                    'destroy': [IsAuthor]}


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class CommentsView(CreateUpdateDestroy):
    """ Editing comments to entries """ 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_classes = CreateCommentSerializer
    permission_classes_by_action = {'update': [IsAuthor],
                                    'destroy': [IsAuthor]}


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


    def perform_destroy(self, instance):
         instance.deleted = True
         instance.save()                                                                              