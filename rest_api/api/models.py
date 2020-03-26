from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class CategoryModel(models.Model):
    name = models.CharField(max_length=255,blank=False,unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PostModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField('CategoryModel')

    def __str__(self):
        return self.title

class ContentModel(models.Model):
    author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, related_name='content')
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField('CategoryModel')

    def __str__(self):
        return self.title

