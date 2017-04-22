from django.db import models

from map.models import Map
from place.models import Place

PIN_LABEL_CHOICE = (
    ('0', 'place'),
    ('1', 'food'),
    ('2', 'cafe'),
    ('3', 'shop'),
    ('4', 'etc'),
)


class Pin(models.Model):
    place = models.ForeignKey(Place)
    map = models.ForeignKey(Map)
    pin_name = models.CharField(max_length=100)
    pin_label = models.CharField(choices=PIN_LABEL_CHOICE, max_length=1, default=0)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        name = self.pin_name
        pk = self.pk

        return '{} : {}'.format(name, pk)


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
