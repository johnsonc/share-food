# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0007_remove_visitpoint_routing'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitpoint',
            name='visit_points',
            field=models.ManyToManyField(related_name='visit_points', to='matcher.Routing'),
        ),
    ]
