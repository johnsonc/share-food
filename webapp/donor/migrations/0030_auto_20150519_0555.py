# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaries', '__first__'),
        ('donor', '0029_auto_20150519_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerrepetition',
            name='days_of_week',
            field=models.ManyToManyField(to='dictionaries.DaysOfTheWeek', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 19, 5, 55, 42, 952757, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_to',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 20, 5, 55, 42, 952785, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
