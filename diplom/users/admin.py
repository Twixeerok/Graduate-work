from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User



@admin.register(User)
class AdminUser(admin.ModelAdmin):
    fields = ('username', 'email', 'first_name', 'last_name', 'patronymic', 'avatar', 'is_active', 'instagram', 'twitter', 'facebook', 'description',)

    list_display = ('username', 'first_name', 'last_name', 'patronymic', 'email', 'is_active',)

    list_display_links = ('username',)
