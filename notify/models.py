from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Notification(models.Model):
    COMMENT = 'comment'
    FOLLOW = 'follow'

    CHOICES = (
        (COMMENT, 'comment'),
        (FOLLOW, 'follow')
    )

    to_user = models.ForeignKey(
        User,
        related_name='notifications',
        on_delete=models.CASCADE
        )
    Notification_type = models.CharField(
        max_length=20,
        choices=CHOICES
        )
    is_read = models.BooleanField(
        default=False
        )
    extra_id = models.IntegerField(
        null=True,
        blank=True
        )
    created_at = models.DateTimeField(
        auto_now_add=True
        )
    created_by = models.ForeignKey(
        User,
        related_name='creatednotification',
        on_delete=models.CASCADE
        )

    def __unicode__(self):
        try:
            return "{0}".format(self.to_user)
        except ObjectDoesNotExist:
            return "[MyModel instance]"


    class Meta:
        ordering = ['-created_at']






    # # 1 = like, 3= follow
    # notification_type = models.IntegerField()
    # to_user = models.ForeignKey(User, related_name='notification_to', on_delete=models.CASCADE, null=True)
    # from_user = models.ForeignKey(User, related_name='notification_from', on_delete=models.CASCADE, null=True)
    # post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    # follow = models.ForeignKey(Follow, on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    # date = models.DateTimeField(default=timezone.now)
    # user_has_seen = models.BooleanField(default=False)