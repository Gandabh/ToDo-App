
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from account.models import User
from django.contrib.auth.admin import UserAdmin



User = get_user_model()
admin.site.register(User, UserAdmin)