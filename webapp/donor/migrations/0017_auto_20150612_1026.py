# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0016_auto_20150611_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 10, 26, 54, 274073, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_to',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 10, 26, 54, 274111, tzinfo=utc)),
        ),
    ]
