
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.documentation import include_docs_urls # new
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='User API')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('users/', include('users.urls')),
    path("api-auth/", include("rest_framework.urls")),
    path("api/rest-auth/", include("rest_auth.urls")),
    path("api/rest-auth/registration/", include("rest_auth.registration.urls")),
    path('docs/', include_docs_urls(title='User API')),
    path('schema/', schema_view),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, docuent_root=settings.MEDIA_ROOT)