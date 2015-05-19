# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0028_auto_20150519_0549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offerrepetition',
            name='day_of_week',
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 19, 5, 54, 48, 468099, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_to',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 20, 5, 54, 48, 468128, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
