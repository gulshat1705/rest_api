from django.db import models
from django.db.models import fields
from rest_framework import serializers
from base.serializers import RecursiveSerializer, FilterCommentListSerializer
# from wall.views import EntryGroupVie
from .models import Post, Comment


class CreateCommentSerializer(serializers.ModelSerializer):
    """ Adding comments to post """
    class Meta:
        model = Comment
        fields = ("post", "text", "parent")


class ListCommentSerializer(serializers.ModelSerializer):
    """ List of comments """
    text = serializers.SerializerMethodField()
    children = RecursiveSerializer(many=True)

    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text


    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ("id", "post", "text", "created_date", "update_date", "deleted", "children")


class PostSerializer(serializers.ModelSerializer):
    """ Output and edit posts """
    user = serializers.ReadOnlyField(source='user.username')
    comment = ListCommentSerializer(many=True, read_only=True) 

    class Meta:
        model = Post
        fields = ("id", "create_date", "user", "text", "comment", "view_account")


class ListPostSerializer(serializers.ModelSerializer):
    """ list of posts"""
    user = serializers.ReadOnlyField(source='user.username')


    class Meta:
        model = Post
        fields = ("id", "create_date", "user", "text", "comments_count")                                       