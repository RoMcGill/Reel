from django.db import models
from django.contrib.auth.models import User
from post.models import Post
from django.db.models.signals import post_save, post_delete
# Create your models here.


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def user_comment_post(sender, instance, *args, **kwargs):
        comment = instance
        post = comment.post
        sender = comment.user
        

post_save.connect(Comment.user_comment_post, sender=Comment)

