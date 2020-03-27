from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework import permissions
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from rest_framework import viewsets
from .permissions import IsOwnProfileOrReadOnly
User = settings.AUTH_USER_MODEL
from rest_framework import mixins
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404


class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """View to retrieve a user instance."""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'put', 'delete', 'head']
    permission_classes = [IsOwnProfileOrReadOnly, permissions.IsAuthenticated]


class UserMeViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'update', 'delete', 'head']
    permission_classes = [IsOwnProfileOrReadOnly, permissions.IsAuthenticated]


    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(username=self.request.user)
        return query_set
