from rest_framework import serializers
from .models import CategoryModel, PostModel
from django.contrib.auth.models import User
from users.models import CustomUser


class CategorySerializer(serializers.ModelSerializer):
    """Serializer to map model instance to json format"""
    class Meta:
        model = CategoryModel
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField('get_username_from_author')
    category  = serializers.SlugRelatedField(
        many=True,
        queryset= CategoryModel.objects.all(),
        slug_field='name'
    )
    class Meta:
        model = PostModel
        fields = ('id', 'author', 'title', 'content', 'created_at', 'category','image')
        read_only_fields = ('created_at','author')

    def get_username_from_author(self,post_name):
        """Get username instead of default id"""
        username = post_name.author.username
        return username

