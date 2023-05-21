from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(
        _("username"), max_length=80, blank=True, null=True, unique=True
    )
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(_("phone number"), max_length=15, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
