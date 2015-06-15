# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0004_auto_20150612_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routing',
            name='visit_points',
            field=models.ManyToManyField(related_name='routes', to='matcher.VisitPoint'),
        ),
    ]
