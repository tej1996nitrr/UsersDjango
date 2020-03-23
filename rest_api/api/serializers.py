from rest_framework import serializers
from .models import CategoryModel


class CategorySerializer(serializers.ModelSerializer):
    """Serializer to map model instance to json format"""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = CategoryModel
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
