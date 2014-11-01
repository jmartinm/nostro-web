# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapapp', '0003_auto_20141101_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointofinterest',
            name='public_endorsment',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
