# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0021_offer_not_contain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='date',
        ),
        migrations.AlterField(
            model_name='offer',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Pick up address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='driver_info',
            field=models.TextField(null=True, verbose_name='Driver information', blank=True),
            preserve_default=True,
        ),
    ]
