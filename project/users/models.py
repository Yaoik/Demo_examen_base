from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from users.managers import UserManager
# Create your models here.


class CustomUser(AbstractUser):
    
    fio = models.CharField(max_length=255)
    email = models.EmailField(_("email address"), blank=False, null=False, unique=True)
    
    username = None
    
    REQUIRED_FIELDS = ['fio']
    USERNAME_FIELD = 'email'
    
    objects = UserManager()
    
    
    def __str__(self):
        return self.email
