# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0005_auto_20150612_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routing',
            name='visit_points',
        ),
        migrations.AddField(
            model_name='visitpoint',
            name='routing',
            field=models.ForeignKey(related_name='visit_points', blank=True, to='matcher.Routing', null=True),
        ),
    ]
