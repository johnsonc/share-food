# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matched',
            options={'verbose_name': 'Match', 'verbose_name_plural': 'Matches', 'permissions': (('readonly', 'Can read matches'),)},
        ),
    ]
