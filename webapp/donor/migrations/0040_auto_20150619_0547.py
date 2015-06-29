# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0039_auto_20150619_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2015, 6, 19, 5, 47, 16, 568994, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offer',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2015, 6, 19, 13, 47, 16, 569012, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 19, 5, 47, 16, 568963, tzinfo=utc), verbose_name='Offer available at'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='valid_to',
            field=models.DateField(default=datetime.datetime(2015, 6, 20, 5, 47, 16, 569034, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
