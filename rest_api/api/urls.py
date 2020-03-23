from django.urls import path, include
from .views import CreateCategoryView, CreatePostView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('category/', CreateCategoryView.as_view(), name='create_category'),
    path('posts/', CreatePostView.as_view(), name='create_posts'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
