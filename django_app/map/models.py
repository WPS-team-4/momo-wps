from django.db import models

from member.models import MomoUser


class Map(models.Model):
    author = models.ForeignKey(MomoUser)
    map_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_private = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        name = self.map_name
        pk = self.pk

        return '{} : {}'.format(name, pk)
