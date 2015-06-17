# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0006_auto_20150612_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitpoint',
            name='routing',
        ),
    ]
