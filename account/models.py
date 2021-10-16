from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import  password_validation
from django import forms
# from django.contrib.auth import get_user_model
from django.utils.translation import gettext, gettext_lazy as _
# from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm

# User = get_user_model()

class User(AbstractUser):
    email = models.EmailField(_('email'), unique=True,)
    phone = models.CharField(max_length=50, null=True,blank=True)
