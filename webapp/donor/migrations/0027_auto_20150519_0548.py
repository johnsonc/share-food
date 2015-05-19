# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0026_auto_20150519_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 19, 5, 48, 7, 319093, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offer',
            name='time_to',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 20, 5, 48, 7, 319125, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
