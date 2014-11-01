# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapapp', '0006_auto_20141101_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointofinterest',
            name='type',
            field=models.CharField(default=b'HEALTH', max_length=100, choices=[(b'REFUGEE', b'Refugee Camp'), (b'HEALTH', b'Health Center'), (b'EDUCATION', b'Education Center'), (b'EDUCATION', b'Embassy'), (b'EDUCATION', b'Consulate'), (b'OTHER', b'Other')]),
            preserve_default=True,
        ),
    ]
