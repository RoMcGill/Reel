from django.contrib import admin
from comment.models import Comment


# admin.site.register(Comment)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('date', 'body')
