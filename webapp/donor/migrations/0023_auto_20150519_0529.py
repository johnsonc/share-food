# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0022_auto_20150519_0525'),
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
