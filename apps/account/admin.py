from django.contrib import admin
from django.contrib.auth.models import Permission

from apps.account.models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "is_superuser", "last_login"]


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    pass
