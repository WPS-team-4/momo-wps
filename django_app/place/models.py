from django.db import models


class Place(models.Model):
    place_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=20, decimal_places=16)
    lng = models.DecimalField(max_digits=20, decimal_places=16)

    def __str__(self):
        name = self.name
        place_id = self.place_id

        return '{} : {}'.format(name, place_id)
