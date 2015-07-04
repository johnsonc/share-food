# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0050_auto_20150704_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 4, 18, 14, 18, 343141, tzinfo=utc), null=True, verbose_name='Offer available at', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2015, 7, 4, 18, 14, 18, 343172, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2015, 7, 5, 2, 14, 18, 343189, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='valid_to',
            field=models.DateField(default=datetime.datetime(2015, 7, 5, 18, 14, 18, 343212, tzinfo=utc), null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offerrepetition',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 18, 14, 18, 345300, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offerrepetition',
            name='date_stop',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 18, 14, 18, 345327, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
