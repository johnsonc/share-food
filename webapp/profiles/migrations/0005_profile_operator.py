# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='operator',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
