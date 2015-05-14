# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0003_auto_20150514_0509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='time_from',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='time_to',
        ),
    ]
