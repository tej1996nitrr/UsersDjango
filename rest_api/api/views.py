from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import CategorySerializer, PostSerializer
from .models import PostModel, CategoryModel
from rest_framework import permissions
from .permissions import IsOwner
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class CreateCategoryView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class DetailsCategoryView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class CreatePostView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwner, permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class DetailsPostView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwner,)


class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserMeView(APIView):

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)