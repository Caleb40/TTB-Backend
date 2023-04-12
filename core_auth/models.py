from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from core_auth.managers import UserManager


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    phone = models.CharField(max_length=14, null=True, blank=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to='customers/profiles/')
