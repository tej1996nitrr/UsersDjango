from django.urls import path, include
from .views import UserViewSet, UserMeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"profiles", UserViewSet)
router.register(r"me", UserMeViewSet, basename="my_profile")
urlpatterns = [
    path("", include(router.urls)),
]
