# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0020_temporalmatching_waiting_since'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matched',
            name='beneficiary',
        ),
        migrations.RemoveField(
            model_name='matched',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='matched',
            name='offer',
        ),
        migrations.AlterField(
            model_name='temporalmatching',
            name='status',
            field=models.PositiveSmallIntegerField(max_length=1, choices=[(1, 'pending'), (2, 'waiting'), (3, 'confirmed'), (4, 'accepted'), (5, 'assigned'), (6, 'notified'), (7, 'expired')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visitpoint',
            name='matched',
            field=models.ForeignKey(to='matcher.TemporalMatching'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Matched',
        ),
    ]
