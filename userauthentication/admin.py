"""
imports
"""
from django.contrib import admin
from userauthentication.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'created')
