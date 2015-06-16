# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150610_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='email',
            field=models.EmailField(max_length=75),
            preserve_default=True,
        ),
    ]
