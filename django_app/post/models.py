from django.db import models

from config import settings


# class PostComment(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL)
#     content = models.TextField(max_length=200)
#
#
# class PostPhoto(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL)
#     photo = models.ImageField(upload_to='post')
from pin.models import Pin


class Post(models.Model):
    pin = models.ForeignKey(Pin)
    comment = models.TextField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='post-photo', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
