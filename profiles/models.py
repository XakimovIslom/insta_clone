from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from config.settings.base import AUTH_USER_MODEL
from post.models import Post


class Profile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile", null=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    favourite = models.ManyToManyField(Post, blank=True)

    def __str__(self):
        return f'{self.user.username} - Profile'


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
