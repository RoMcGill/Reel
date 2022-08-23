"""
    Imports
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from post.models import Post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Comment(models.Model):
    """
    A class for the comment model
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

    body = models.TextField()

    date = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        """
        returns users name and comment body in admin panel
        """
        return '{}/{}'.format(self.user, self.body)


    def user_comment_post(sender, instance, *args, **kwargs):
        """
        A function for user to post comment
        """
        comment = instance
        post = comment.post
        sender = comment.user


post_save.connect(
    Comment.user_comment_post,
    sender=Comment)

