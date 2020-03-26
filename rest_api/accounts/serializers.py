from rest_framework import serializers
from .models import Profile
from api.models import ContentModel
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)
    profile_pic = serializers.ImageField(read_only=True)
    content = serializers.PrimaryKeyRelatedField(
        many=True, queryset=ContentModel.objects.all())

    class Meta:
        model = Profile
        fields = "__all__"


class ProfilePicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ("profile_pic",)

class UserSerializer(serializers.ModelSerializer):
    """A user serializer for authentication and authorization."""
    profile_pic = serializers.ImageField(read_only=True)
    posts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'posts','profile_pic')


