from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import CategorySerializer, PostSerializer
from .models import PostModel, CategoryModel


class CreateCategoryView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class CreatePostView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()