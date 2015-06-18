# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0034_auto_20150618_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerrepetition',
            name='day_of_week',
            field=models.CharField(default='Mon', max_length=3, choices=[(b'Mon', 'Monday'), (b'Tue', 'Tuesday'), (b'Wed', 'Wednesday'), (b'Thu', 'Thursday'), (b'Fri', 'Friday'), (b'Sat', 'Saturday'), (b'Sun', 'Sunday')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 10, 30, 38, 369215, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_to',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 19, 10, 30, 38, 369241, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='valid_to',
            field=models.DateField(default=datetime.datetime(2015, 6, 19, 10, 30, 38, 369266, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
