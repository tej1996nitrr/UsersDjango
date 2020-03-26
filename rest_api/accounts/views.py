from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .models import Profile,ProfileStatus
from .serializers import ProfileSerializer,ProfileStatusSerializer,ProfilePicSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import mixins
from .permissions import IsProfileOwner,IsProfileStatusOwner


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
    permission_classes = (IsAuthenticated,IsProfileOwner)


class ProfileStatusViewset(viewsets.ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = (IsAuthenticated,IsProfileStatusOwner)

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile = user_profile)

