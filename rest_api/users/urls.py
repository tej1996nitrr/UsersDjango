from django.urls import path, include
from .views import UserView, UserDetailsView, UserViewSet, UserMeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"profiles", UserViewSet)
router.register(r"me", UserMeViewSet
                )
urlpatterns = [
    path("", include(router.urls)),
]
