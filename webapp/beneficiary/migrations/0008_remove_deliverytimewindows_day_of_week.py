# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0007_auto_20150611_0835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliverytimewindows',
            name='day_of_week',
        ),
    ]
