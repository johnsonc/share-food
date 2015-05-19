# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0016_auto_20150519_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='temperature',
            field=models.ForeignKey(to='dictionaries.TemperatureCategory'),
            preserve_default=True,
        ),
    ]
