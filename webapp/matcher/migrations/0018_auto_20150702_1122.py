# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0017_auto_20150619_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporalmatching',
            name='confirmed_at',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='temporalmatching',
            name='status',
            field=models.PositiveSmallIntegerField(max_length=1, choices=[(1, 'pending'), (2, 'waiting'), (3, 'confirmed'), (4, 'accepted'), (5, 'assigned'), (6, 'notified'), (7, 'expired'), (8, 'canceled')]),
            preserve_default=True,
        ),
    ]
