from django.db import models

from pin.models import PinComment, PinPhoto, Pin


class Post(models.Model):
    pin = models.ForeignKey(Pin)
    comment = models.ForeignKey(PinComment, blank=True)
    photo = models.ForeignKey(PinPhoto, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
