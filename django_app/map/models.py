from django.db import models

from member.models import MomoUser

# description: blank=True, null=True 설정 필요

class Map(models.Model):
    author = models.ForeignKey(MomoUser)
    map_name = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        name = self.map_name
        pk = self.pk

        return '{} : {}'.format(name, pk)
