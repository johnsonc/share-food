# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0044_auto_20150619_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 2, 11, 22, 50, 933372, tzinfo=utc), null=True, verbose_name='Offer available at', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2015, 7, 2, 11, 22, 50, 933405, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2015, 7, 2, 19, 22, 50, 933424, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='valid_to',
            field=models.DateField(default=datetime.datetime(2015, 7, 3, 11, 22, 50, 933448, tzinfo=utc), null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offerrepetition',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 11, 22, 50, 935615, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offerrepetition',
            name='date_stop',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 11, 22, 50, 935643, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
