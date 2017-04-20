from django.db import models

from pin.models import Pin


class Post(models.Model):
    pin = models.ForeignKey(Pin)
    photo = models.ImageField(upload_to='post', blank=True)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(
            self.pk
        )

    def to_dict(self):
        ret = {
            'pk': self.pk,
            'photo': self.photo.url,
        }
        return ret
