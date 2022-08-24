"""
imports
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from post.models import Post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# user files to directory
def user_directory_path(instance, filename):
    """
    function to get user files to directory
    """
    return 'user_{0}/{1}'.format(
        instance.user.id,
        filename
        )


class Profile(models.Model):
    """
    class for profile model
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
        )
    first_name = models.CharField(
        max_length=50,
        null=True,
        blank=True
        )
    last_name = models.CharField(
        max_length=50,
        null=True,
        blank=True
        )
    location = models.CharField(
        max_length=50,
        null=True,
        blank=True
        )
    url = models.CharField(
        max_length=100,
        null=True,
        blank=True
        )
    profile_info = models.TextField(
        max_length=150,
        null=True,
        blank=True
        )
    created = models.DateField(
        auto_now_add=True
        )
    favourite = models.ManyToManyField(
        Post
        )
    image = models.ImageField(
        upload_to=user_directory_path,
        blank=True,
        null=True,
        verbose_name='picture',
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        """
        shows user and username in admin panel
        """
        return f'{self.user.username} - Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


def create_user_profile(sender, instance, created, **kwargs):
    """
    function to create user profiles
    """
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    """
    function to save user profiles
    """
    instance.profile.save()


post_save.connect(
    create_user_profile,
    sender=User
    )
post_save.connect(
    save_user_profile,
    sender=User
    )
