from .serializers import UserSerializer
from rest_framework import permissions
from .models import CustomUser
from rest_framework import viewsets
from .permissions import IsOwnProfileOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """View for a user instance."""
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
