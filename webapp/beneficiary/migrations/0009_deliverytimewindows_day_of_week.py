# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0008_remove_deliverytimewindows_day_of_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverytimewindows',
            name='day_of_week',
            field=models.IntegerField(default=0, choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')]),
            preserve_default=False,
        ),
    ]
