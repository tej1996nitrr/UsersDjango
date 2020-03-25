from django.urls import path
from .views import ProfileList

urlpatterns = [
    path('', ProfileList.as_view(), name="profile-list"),
]
