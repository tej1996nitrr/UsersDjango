from django.urls import path, include
from .views import CreateCategoryView, CreatePostView, DetailsCategoryView,DetailsPostView
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserView, UserDetailsView, UserMeView

urlpatterns = [
    path('auth/', include('rest_framework.urls',
                          namespace='rest_framework')),
    path('category/', CreateCategoryView.as_view(), name='create_category'),
    path('posts/', CreatePostView.as_view(), name='create_posts'),
    path('category/<int:pk>', DetailsCategoryView.as_view(), name='category_details'),
    path('posts/<int:pk>', DetailsPostView.as_view(), name='post_details'),
    path('users/', UserView.as_view(), name="users"),
    path('users/<pk>', UserDetailsView.as_view(), name="user_details"),
    path('users/me/', UserMeView.as_view(), name='me_user_details')
]

urlpatterns = format_suffix_patterns(urlpatterns)
