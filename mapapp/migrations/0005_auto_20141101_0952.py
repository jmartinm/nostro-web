# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapapp', '0004_auto_20141101_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointofinterest',
            name='verified_date',
            field=models.DateField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
