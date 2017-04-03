from django.db import models

from member.models import MomoUser
from place.models import Place


class Map(models.Model):
    author = models.ForeignKey(MomoUser)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.pk


class Pin(models.Model):
    author = models.ForeignKey(MomoUser)
    place = models.ForeignKey(Place)
    map = models.ForeignKey(Map)
    name = models.CharField(max_length=100)
    pin_color = models.CharField(max_length=10, default='0,0,0', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)

    def add_comment(self, user, content):
        return self.pincomment_set.create(
            author=user,
            contnet=content
        )

    def add_photo(self, user, photo):
        return self.pinphoto_set.create(
            author=user,
            photo=photo
        )

    def __str__(self):
        return 'user({}) place({}) map({}) pin_name({})'.format(
            self.author_id, self.place_id, self.map_id, self.name)


class HashTag(models.Model):
    content = models.CharField(max_length=100, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)


class PinHashTag(models.Model):
    hash_tag = models.ForeignKey(HashTag)
    pin = models.ForeignKey(Pin)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('hash_tag', 'pin'),
        )

    def __str__(self):
        return 'tag({}) in pin({})'.format(self.hash_tag.content, self.pin.id)


class Label(models.Model):
    pin = models.ForeignKey(Pin)
    color = models.CharField(max_length=10)
    name = models.CharField(max_length=10)


class PinComment(models.Model):
    author = models.ForeignKey(MomoUser)
    pin = models.ForeignKey(Pin)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


class PinPhoto(models.Model):
    author = models.ForeignKey(MomoUser)
    pin = models.ForeignKey(Pin)
    photo = models.ImageField(upload_to='pin')
    created_date = models.DateTimeField(auto_now_add=True)
