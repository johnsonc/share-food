# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0003_auto_20150514_0607'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery',
            options={'verbose_name': 'Delivery', 'verbose_name_plural': 'Delivery points'},
        ),
        migrations.AlterModelOptions(
            name='matched',
            options={'verbose_name': 'Match', 'verbose_name_plural': 'Matches'},
        ),
    ]
