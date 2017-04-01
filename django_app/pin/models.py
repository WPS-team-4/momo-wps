from django.db import models

from member.models import MomoUser


class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=20)
    google_place_id = models.CharField(max_length=100, blank=True)


class Map(models.Model):
    author = models.ForeignKey(MomoUser)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)


class Pin(models.Model):
    author = models.ForeignKey(MomoUser)
    place = models.ForeignKey(Place)
    map = models.ForeignKey(Map)
    name = models.CharField(max_length=100)
    pin_color = models.CharField(max_length=10, default='0,0,0')
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
