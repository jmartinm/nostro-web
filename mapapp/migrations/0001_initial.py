# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PointOfInterest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=100)),
                ('public_endorsment', models.IntegerField()),
                ('verified', models.BooleanField()),
                ('verified_date', models.DateField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('num_people', models.IntegerField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
