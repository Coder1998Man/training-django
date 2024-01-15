from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Specify the fields to display in the admin list view
    list_display = ['username', 'email', 'is_staff']

    # Specify the fields to use for searching in the admin list view
    search_fields = ['username', 'email']

    # Specify the fields to filter the admin list view by
    list_filter = ['is_staff', 'is_superuser']

    # Specify the fieldsets for the admin detail view
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)