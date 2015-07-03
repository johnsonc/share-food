# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0018_auto_20150702_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temporalmatching',
            name='confirmed_at',
        ),
    ]
