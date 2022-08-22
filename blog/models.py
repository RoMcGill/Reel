"""
    Imports
"""
from django.db import models


class blogpost(models.Model):
    """
    A class for the blog post model
    """
    title = models.CharField(
        max_length=250
    )
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(
        auto_now_add=True
    )
    picture = models.ImageField(
        verbose_name="Picture",
        null=True
    )

    class Meta:

        """
        A Meta class for the order of posts to be displayed
        """
        ordering = ['-date_added']
