# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0046_auto_20150702_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 2, 20, 49, 4, 576973, tzinfo=utc), null=True, verbose_name='Offer available at', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2015, 7, 2, 20, 49, 4, 577008, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2015, 7, 3, 4, 49, 4, 577026, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='valid_to',
            field=models.DateField(default=datetime.datetime(2015, 7, 3, 20, 49, 4, 577050, tzinfo=utc), null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offerrepetition',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 20, 49, 4, 579143, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offerrepetition',
            name='date_stop',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 20, 49, 4, 579166, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
