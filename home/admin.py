from django.contrib.auth.models import Group
from django.contrib import admin
from . import models

# Register your models here.

admin.site.unregister(Group)

@admin.register(models.Password)
class PasswordAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')