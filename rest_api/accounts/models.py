from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend
from django.conf import settings
from django.contrib.auth.hashers import check_password

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,unique=True)
    bio = models.CharField(max_length=240, blank=True)
    city = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.user.username



