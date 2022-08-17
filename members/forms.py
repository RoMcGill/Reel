"""
imports
"""
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models


class UserRegisterForm(UserCreationForm):
    """
    class for form for user registration
    """
    email = models.EmailField()

    class Meta:
        """
        meta for form fields
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']
