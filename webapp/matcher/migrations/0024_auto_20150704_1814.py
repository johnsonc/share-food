# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matcher', '0023_auto_20150704_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporalmatching',
            name='canceled_by',
            field=models.ForeignKey(related_name='canceler', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='temporalmatching',
            name='driver',
            field=models.ForeignKey(related_name='match_driver', default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='temporalmatching',
            name='status',
            field=models.PositiveSmallIntegerField(max_length=1, choices=[(1, 'pending'), (2, 'waiting'), (3, 'confirmed'), (4, 'accepted'), (5, 'assigned'), (6, 'notified'), (7, 'expired'), (8, 'canceled')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visitpoint',
            name='status',
            field=models.CharField(default=b'p', max_length=1, choices=[(b'p', 'Pending'), (b'c', 'Confirmed'), (b'x', 'Canceled')]),
            preserve_default=True,
        ),
    ]
