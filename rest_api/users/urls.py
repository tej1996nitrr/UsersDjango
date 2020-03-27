from django.urls import path
from .views import UserView, UserDetailsView, UserMeView

urlpatterns = [
    path("profiles/", UserView.as_view(), name="all_profiles")
]
