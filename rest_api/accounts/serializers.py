from rest_framework import  serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from api.models import PostModel

class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=6, write_only=True)
    confirm_password = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = User
        fields =('id','username','email','password','confirm_password')

    def validate(self, data):
        """ validate received password and confirm_password"""
        if data['password'] != data.pop('confirm_password'):
            raise serializers.ValidationError("Passwords do not match")
        return data

class UserSerializer(serializers.ModelSerializer):
    """A user serializer for authentication and authorization."""

    posts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=PostModel.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')






