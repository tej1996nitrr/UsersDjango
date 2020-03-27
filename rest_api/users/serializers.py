from api.models import PostModel
from rest_framework import serializers
from django.conf import settings
from .models import CustomUser
User = settings.AUTH_USER_MODEL


class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    posts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=PostModel.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = CustomUser
        fields = ["id","posts","username","email","bio","city","profile_pic","date_of_birth"]


