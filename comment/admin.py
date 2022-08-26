"""
    Imports
"""
from django.contrib import admin
from comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    class to add search functionality to comments in admin panel
    """
    search_fields = ('date', 'body')
