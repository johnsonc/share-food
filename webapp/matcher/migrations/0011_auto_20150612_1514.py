# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0010_routing_visit_points'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matched',
            options={'verbose_name': 'Delivery schedule', 'verbose_name_plural': 'Delivery schedules', 'permissions': (('readonly', 'Can read matches'),)},
        ),
        migrations.RemoveField(
            model_name='routing',
            name='visit_points',
        ),
    ]
