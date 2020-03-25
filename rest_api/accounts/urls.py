from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.UserCreate.as_view(), name = 'account-create'),
    path('allusers/', views.UserView.as_view(), name = 'account-allusers'),
    path('users/me/',views.UserMeView.as_view(), name = 'account-me'),
    path('users/<int:pk>',views.UserDetailsView.as_view(), name = 'account-details')
]

