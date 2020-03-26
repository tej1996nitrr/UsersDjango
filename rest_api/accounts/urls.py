from django.urls import path,include
from .views import ProfileViewSet,ProfilePicUpdateView,MyProfileView,UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profiles', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('pic/', ProfilePicUpdateView.as_view(), name='pic_update'),
    path('me/', MyProfileView.as_view(), name='my_profile')
]
