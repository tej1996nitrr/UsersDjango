from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):

    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    email = models.EmailField(_('email address'), unique=True)
    bio = models.CharField(max_length=240, blank=True)
    city = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username
