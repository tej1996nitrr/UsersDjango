from django.contrib import admin
from .models import PostModel,CategoryModel,ContentModel

admin.site.register(PostModel)
admin.site.register(CategoryModel)
admin.site.register(ContentModel)
