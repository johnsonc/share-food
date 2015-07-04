# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0022_auto_20150704_1325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='temporalmatching',
            options={'verbose_name': 'Match', 'verbose_name_plural': 'Matches'},
        ),
        migrations.AddField(
            model_name='visitpoint',
            name='confirmed',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
