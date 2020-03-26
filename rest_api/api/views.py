from django.shortcuts import render
from rest_framework import generics
from .serializers import CategorySerializer,ContentSerializer
from .models import CategoryModel,ContentModel
from rest_framework import permissions
from .permissions import IsOwner


class CreateCategoryView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new cat."""
        serializer.save()


class DetailsCategoryView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class CreateContentView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = ContentModel.objects.all()
    serializer_class = ContentSerializer
    permission_classes = (IsOwner, permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        """Save the post data when creating a new post."""
        print(self.request.user)
        serializer.save(author=self.request.user)


class DetailsContentView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = ContentModel.objects.all()
    serializer_class = ContentSerializer
    permission_classes = (IsOwner,)
