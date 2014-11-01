from django.db import models
from geoposition.fields import GeopositionField


class PointOfInterest(models.Model):
    REFUGEE = 'REFUGEE'
    HEALTH = 'HEALTH'
    EDUCATION = 'EDUCATION'
    EMBASSY = 'EMBASSY'
    CONSULATE = 'CONSULATE'
    OTHER = 'OTHER'
    POI_TYPE_CHOICES = (
        (REFUGEE, 'Refugee Camp'),
        (HEALTH, 'Health Center'),
        (EDUCATION, 'Education Center'),
        (EDUCATION, 'Embassy'),
        (EDUCATION, 'Consulate'),
        (OTHER, 'Other'),
    )
    name = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=100,
                            choices=POI_TYPE_CHOICES,
                            default=HEALTH)
    public_endorsment = models.IntegerField(default=0, null=True, blank=True)
    verified = models.BooleanField(default=False, blank=True)
    verified_date = models.DateField(max_length=100,
                                     null=True,
                                     blank=True)
    website = models.CharField(max_length=100, blank=True)
    num_people = models.IntegerField(max_length=100, null=True, blank=True)
    owner = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    comments = models.CharField(max_length=1000, null=True, blank=True)
    position = GeopositionField()

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.type)
