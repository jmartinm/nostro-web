# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapapp', '0002_auto_20141031_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointofinterest',
            name='contact',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='name',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='num_people',
            field=models.IntegerField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='owner',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='public_endorsment',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='type',
            field=models.CharField(default=b'HEALTH', max_length=100, choices=[(b'REFUGEE', b'Refugee Camp'), (b'HEALTH', b'Health Center'), (b'EDUCATION', b'Education Center'), (b'OTHER', b'Other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='verified_date',
            field=models.DateField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='website',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
