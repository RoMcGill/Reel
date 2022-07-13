from django.db import models
from django.contrib.auth.models import User
from post.models import Post


# user files to directory
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    profile_info = models.TextField(max_length=150, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    favourite = models.ManyToManyField(Post)
    image = models.ImageField(upload_to=user_directory_path,blank=True, null=True, verbose_name='picture')

    # def __str__(self):
    #     return self.first_name

# Create your models here.
