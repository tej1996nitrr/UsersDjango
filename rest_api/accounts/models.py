from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=240, blank=True)
    city = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.user.username



