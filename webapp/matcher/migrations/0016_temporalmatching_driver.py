# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0015_auto_20150616_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporalmatching',
            name='driver',
            field=models.ForeignKey(default=None, blank=True, to='matcher.Driver', null=True),
            preserve_default=True,
        ),
    ]
