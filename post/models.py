"""
imports
"""
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.urls import reverse


def user_directory_path(instance, filename):
    """
    function to get user files to directory
    """
    return 'user_{0}/{1}'.format(
        instance.user.id,
        filename
        )


class Tag(models.Model):
    """
    class for hashtag model
    """
    title = models.CharField(
        max_length=100,
        verbose_name="Tag"
        )
    slug = models.SlugField(
        null=False,
        unique=True,
        default=uuid.uuid1
        )

    class Meta:
        """
        class for hashtag(plural) to be known as tags
        """
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def get_absolute_url(self):
        """
        function to get each tags absolute url
        """
        return reverse(
            'tags',
            args=[self.slug]
            )

    def __str__(self):
        """
        shows tag title in admin panel
        """
        return self.title

    def save(self, *args, **kwargs):
        """
        saves hashtags
        """
        if not self.slug:
            self.slug - slugify(self.slug)
        return super().save(*args, **kwargs)


class Post(models.Model):
    """
    class for post model
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=True
        )
    picture = models.ImageField(
        upload_to=user_directory_path,
        verbose_name="Picture",
        null=True
        )
    caption = models.CharField(
        max_length=10000,
        verbose_name="Caption"
        )
    posted = models.DateTimeField(
        auto_now_add=True
        )
    tag = models.ManyToManyField(
        Tag,
        related_name="tags"
        )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    likes = models.IntegerField(
        default=0
        )

    def get_absolute_url(self):
        """
        gets url of post
        """
        return reverse(
            "post-detail",
            args=[str(self.id)]
            )

    def __str__(self):
        """
        shows post caption in admin panel
        """
        return self.caption


class Follow(models.Model):
    """
    class for follow model
    """
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower"
        )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following"
        )

    def __str__(self):
        """
        shows who is now following who in admin panel
        """
        return self.follower, " is now following ", self.following


class Stream(models.Model):
    """
    class for stream model (the feed)
    """
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="stream_following"
        )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="stream_user"
        )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=True
        )
    date = models.DateTimeField()

    def __str__(self):
        """
        shows who posted what post in admin panel
        """
        return self.user, self.post

    def add_post(sender, instance, *args, **kwargs):
        """
        function for users to create posts
        """
        post = instance
        user = post.user
        followers = Follow.objects.all().filter(following=user)
        for follower in followers:
            stream = Stream(
                post=post,
                user=follower.follower,
                date=post.posted,
                following=user
            )
            stream.save()


class Likes(models.Model):
    """
    class for the like model
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_likes'
        )

    def __str__(self):
        """
        shows who liked what post in admin panel
        """
        return self.user, " Likes ", self.post
# ##################################################################
# ###################### solved button ############################
# ##################################################################
# class Solves(models.Model):
#     """
#     class for the like model
#     """
#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE
#         )
#     post = models.ForeignKey(
#         Post,
#         on_delete=models.CASCADE,
#         related_name='post_solves'
#         )

#     def __str__(self):
#         """
#         shows who solved what post in admin panel
#         """
#         return self.user, " Solved ", self.post
# ##################################################################
# ###################### solved button ############################
# ##################################################################


post_save.connect(Stream.add_post, sender=Post)
