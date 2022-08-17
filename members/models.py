"""
imports
"""
from django.db import models


class displayusername(models.Model):
    """
    class to create users username model
    """
    username = models.CharField(max_length=100)
