# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0037_auto_20150618_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 11, 1, 50, 526292, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_to',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 19, 11, 1, 50, 526323, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='valid_to',
            field=models.DateField(default=datetime.datetime(2015, 6, 19, 11, 1, 50, 526345, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offerrepetition',
            name='day_freq',
            field=models.PositiveSmallIntegerField(verbose_name='Day frequency', choices=[(0, '1st in the month'), (1, '2nd in the month'), (2, '3rd in the month'), (3, '4th in the month')]),
            preserve_default=True,
        ),
    ]
