from django.db import models

from map.models import Map
from place.models import Place


class Pin(models.Model):
    place = models.ForeignKey(Place)
    map = models.ForeignKey(Map)
    name = models.CharField(max_length=100)
    pin_color = models.CharField(max_length=10, default='0,0,0', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return 'pin: {}'.format(
            self.pk
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
