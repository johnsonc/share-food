# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0002_auto_20150514_0602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'verbose_name': 'Driver', 'verbose_name_plural': 'Drivers'},
        ),
        migrations.AlterModelOptions(
            name='routing',
            options={'verbose_name': 'Routing', 'verbose_name_plural': 'Routings'},
        ),
        migrations.AlterModelOptions(
            name='temporalmatching',
            options={'verbose_name': 'Temporal match', 'verbose_name_plural': 'Temporal matchings'},
        ),
        migrations.AlterModelOptions(
            name='visitpoint',
            options={'verbose_name': 'Visit point', 'verbose_name_plural': 'Visit points'},
        ),
        migrations.RenameField(
            model_name='visitpoint',
            old_name='matched_id',
            new_name='matched',
        ),
    ]
