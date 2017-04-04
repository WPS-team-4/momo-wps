from django.db import models

from member.models import MomoUser


class Map(models.Model):
    author = models.ForeignKey(MomoUser)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.pk
