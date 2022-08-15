from django.contrib import admin
from post.models import Tag, Post, Follow, Stream, Notification, Likes

admin.site.register(Tag)
#admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Stream)
admin.site.register(Notification)
admin.site.register(Likes)
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('posted', 'caption')