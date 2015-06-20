# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0041_auto_20150619_0602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offerrepetition',
            name='date_start',
        ),
        migrations.RemoveField(
            model_name='offerrepetition',
            name='date_stop',
        ),
        migrations.AlterField(
            model_name='offer',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 19, 6, 5, 34, 963291, tzinfo=utc), null=True, verbose_name='Offer available at', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2015, 6, 19, 6, 5, 34, 963324, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2015, 6, 19, 14, 5, 34, 963340, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='valid_to',
            field=models.DateField(default=datetime.datetime(2015, 6, 20, 6, 5, 34, 963364, tzinfo=utc), null=True, blank=True),
            preserve_default=True,
        ),
    ]
