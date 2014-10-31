from django.db import models
from geoposition.fields import GeopositionField


class PointOfInterest(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    public_endorsment = models.IntegerField()
    verified = models.BooleanField(default=False)
    verified_date = models.DateField(max_length=100)
    website = models.CharField(max_length=100)
    num_people = models.IntegerField(max_length=100)
    owner = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    position = GeopositionField()
