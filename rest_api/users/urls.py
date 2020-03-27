from django.urls import path,include
from .views import UserView, UserDetailsView, UserMeView, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"profiles", UserViewSet)
# router.register(r"me", UserMeView)
urlpatterns = [
    path("", include(router.urls)),
    # path("me/", UserMeView.as_view(), name="my_profile")
]
