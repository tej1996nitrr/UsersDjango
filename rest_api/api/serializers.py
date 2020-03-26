from rest_framework import serializers
from .models import CategoryModel, PostModel,ContentModel
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    """Serializer to map model instance to json format"""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = CategoryModel
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ('id', 'author', 'title', 'content', 'created_at', 'category')
        read_only_fields = ('created_at',)

class ContentSerializer(serializers.ModelSerializer):
    # print(serializers.CurrentUserDefault())
    class Meta:
        model = ContentModel
        fields = ('id', 'title', 'content', 'created_at', 'category','author')
        read_only_fields = ('created_at','author')


class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    posts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=PostModel.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'posts')