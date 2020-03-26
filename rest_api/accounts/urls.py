from django.urls import path,include
from .views import ProfileViewSet,ProfileStatusViewset,ProfilePicUpdateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profiles', ProfileViewSet)
router.register('status', ProfileStatusViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('pic/', ProfilePicUpdateView.as_view(), name='pic_update')
]
