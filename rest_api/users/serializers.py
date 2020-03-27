from api.models import PostModel
from rest_framework import serializers
from django.conf import settings
from .models import CustomUser
User = settings.AUTH_USER_MODEL


class UserSerializer(serializers.ModelSerializer):
    """A user serializer for authentication and authorization."""

    posts = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='post_details')

    class Meta:
        model = CustomUser
        fields = ["id", "posts", "username", "email", "bio", "city", "profile_pic", "date_of_birth"]


