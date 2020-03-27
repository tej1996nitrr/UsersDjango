from rest_framework import generics
from .serializers import CategorySerializer, PostSerializer
from .models import PostModel, CategoryModel
from rest_framework import permissions
from .permissions import IsOwner


class CreateCategoryView(generics.ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save()


class DetailsCategoryView(generics.RetrieveUpdateDestroyAPIView):

    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CreatePostView(generics.ListCreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwner, permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DetailsPostView(generics.RetrieveUpdateDestroyAPIView):

    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwner,)

