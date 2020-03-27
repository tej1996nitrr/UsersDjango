from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework import permissions
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
User = settings.AUTH_USER_MODEL


class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserMeView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)