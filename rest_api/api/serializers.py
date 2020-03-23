from rest_framework import serializers
from .models import CategoryModel, PostModel


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
