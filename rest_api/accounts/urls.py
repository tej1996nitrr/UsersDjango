from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/',views.UserCreate.as_view(), name = 'account-create'),
    path('login/', obtain_auth_token, name='account-login'),
    path('allusers/', views.UserView.as_view(), name = 'account-allusers'),
    path('me/',views.UserMeView.as_view(), name = 'account-me'),
    path('detail/<int:pk>',views.UserDetailsView.as_view(), name = 'account-details')
]

