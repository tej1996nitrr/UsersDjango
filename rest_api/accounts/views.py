from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer,ProfilePicSerializer,UserSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import mixins
from .permissions import IsProfileOwner
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User


class ProfilePicUpdateView(generics.UpdateAPIView):
    serializer_class = ProfilePicSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object


class ProfileViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,IsProfileOwner)



class UserViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,IsProfileOwner)

class MyProfileView(APIView):

    def get(self, request):
        serializer = ProfileSerializer(request.user.profile)
        return Response(serializer.data)

