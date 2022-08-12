from django.contrib import admin
from post.models import Tag, Post, Follow, Stream, Notification

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Stream)
admin.site.register(Notification)
# Register your models here.
