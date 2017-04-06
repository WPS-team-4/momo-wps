from django.db import models

from member.models import MomoUser
from pin.models import Pin


class PostComment(models.Model):
    author = models.ForeignKey(MomoUser)
    pin = models.ForeignKey(Pin)
    content = models.TextField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)


class PostPhoto(models.Model):
    author = models.ForeignKey(MomoUser)
    pin = models.ForeignKey(Pin)
    photo = models.ImageField(upload_to='post')
    created_date = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    pin = models.ForeignKey(Pin)
    comment = models.ForeignKey(PostComment, blank=True)
    photo = models.ForeignKey(PostPhoto, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
