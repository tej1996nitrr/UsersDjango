from django.urls import path, include
from .views import CreateCategoryView, DetailsCategoryView, CreateContentView,DetailsContentView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_urls')),
    path('category/', CreateCategoryView.as_view(), name='create_category'),
    path('category/<int:pk>', DetailsCategoryView.as_view(), name='category_details'),
    path('content/', CreateContentView.as_view(), name='create_content'),
    path('content/<int:pk>', DetailsContentView.as_view(), name='content_details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
