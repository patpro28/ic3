from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

from users.models import User

class UserAdmin(BaseUserAdmin):
    readonly_fields = (
        'username',
        'date_joined', 
        'last_login'
    )