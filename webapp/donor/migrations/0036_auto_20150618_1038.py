# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0035_auto_20150618_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offerrepetition',
            name='day_of_week',
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 10, 38, 2, 359608, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_to',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 19, 10, 38, 2, 359653, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='valid_to',
            field=models.DateField(default=datetime.datetime(2015, 6, 19, 10, 38, 2, 359687, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
