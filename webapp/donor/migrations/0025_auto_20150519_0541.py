# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0024_offer_time_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='time_to',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 20, 5, 41, 2, 501832)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 19, 5, 41, 2, 501808)),
            preserve_default=True,
        ),
    ]
