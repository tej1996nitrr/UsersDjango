from django.urls import path, include
from .views import CreateCategoryView, CreatePostView, DetailsCategoryView,DetailsPostView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('category/', CreateCategoryView.as_view(), name='create_category'),
    path('posts/', CreatePostView.as_view(), name='create_posts'),
    path('category/<int:pk>',DetailsCategoryView.as_view(),name='category_details'),
    path('posts/<int:pk>',DetailsPostView.as_view(),name='post_details')
]
urlpatterns = format_suffix_patterns(urlpatterns)
