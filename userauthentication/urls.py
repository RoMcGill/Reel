"""
imports
"""
from django.urls import path
from userauthentication.views import UserProfile, editProfile
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    path('profile/update/', views.editProfile, name='editProfile'),
]
