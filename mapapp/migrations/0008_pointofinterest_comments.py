# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapapp', '0007_auto_20141101_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointofinterest',
            name='comments',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
