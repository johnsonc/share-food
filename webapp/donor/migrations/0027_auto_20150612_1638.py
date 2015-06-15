# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0026_auto_20150612_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 16, 38, 12, 38714, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_to',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 16, 38, 12, 38749, tzinfo=utc)),
        ),
    ]
