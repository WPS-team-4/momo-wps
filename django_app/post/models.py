from django.db import models
from django.dispatch import receiver
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer

from pin.models import Pin


class Post(models.Model):
    pin = models.ForeignKey(Pin)
    photo = VersatileImageField(
        'post',
        upload_to='post/',
        blank=True,
    )
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


@receiver(models.signals.post_save, sender=Post)
def warm_post_headshot_images(sender, instance, **kwargs):
    post_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='post',
        image_attr='photo',
        verbose=True
    )
    num_created, failed_to_create = post_img_warmer.warm()

