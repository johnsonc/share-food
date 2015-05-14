# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150513_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='default_mass_unit',
            field=models.CharField(default=b'kg', max_length=5, choices=[(b'kg', b'kg'), (b'lb', b'lb')]),
            preserve_default=True,
        ),
    ]
