# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0012_visitpoint_routing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitpoint',
            name='status',
            field=models.CharField(max_length=1, choices=[(b'p', 'Pending'), (b'c', 'Confirmed')]),
        ),
    ]
