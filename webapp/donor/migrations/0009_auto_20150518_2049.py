# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0008_donnor_default_beneficiary_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donnor',
            name='default_beneficiary_group',
        ),
        migrations.AlterField(
            model_name='offerrepetition',
            name='day_freq',
            field=models.PositiveSmallIntegerField(verbose_name='Day frequency'),
            preserve_default=True,
        ),
    ]
