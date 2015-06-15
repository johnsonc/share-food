# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0003_routing_visit_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='routing',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='visit_point',
        ),
        migrations.DeleteModel(
            name='Delivery',
        ),
    ]
