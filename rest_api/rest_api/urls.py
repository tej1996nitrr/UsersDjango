from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),

    path('', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/rest-auth/', include('rest_auth.urls'), name="rest_auth_urls"),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls'), name="register"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
