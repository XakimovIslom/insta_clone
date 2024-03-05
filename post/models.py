from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from django.db import models

from common.models import BaseModel
from config.settings.base import AUTH_USER_MODEL


class Post(BaseModel):
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    file_content = models.FileField(upload_to='post/')
    description = models.TextField(validators=[MaxLengthValidator(2000)])
    like = models.ManyToManyField(AUTH_USER_MODEL, related_name='post_likes')

    class Meta:
        db_table = 'posts'
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return f"{self.author} post about {self.description}"


class Comment(BaseModel):
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child',
                               null=True, blank=True)
    like = models.ManyToManyField(AUTH_USER_MODEL, related_name='comment_likes')

    def __str__(self):
        return f"Comments by {self.author}"


class Follow(models.Model):
    follower = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')

    def __str__(self):
        return 'something'
