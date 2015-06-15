# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0009_remove_visitpoint_visit_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='routing',
            name='visit_points',
            field=models.ManyToManyField(related_name='routings', to='matcher.VisitPoint'),
        ),
    ]
