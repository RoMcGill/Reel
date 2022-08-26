"""
imports:
"""
from django.contrib import admin
from post.models import Tag, Post, Follow, Stream, Likes

admin.site.register(Tag)
admin.site.register(Follow)
admin.site.register(Stream)
admin.site.register(Likes)
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    add searchbar to admin post.
    """
    search_fields = ('posted', 'caption')
