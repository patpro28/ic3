from django.contrib import admin

# ModelAdmin classes
from .user import UserAdmin

# Model classes
from users.models import User

admin.site.register(User, UserAdmin)