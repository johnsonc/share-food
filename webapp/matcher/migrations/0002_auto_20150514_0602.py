# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitpoint',
            name='donor',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
