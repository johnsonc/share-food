# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0002_auto_20150611_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='routing',
            name='visit_points',
            field=models.ManyToManyField(to='matcher.VisitPoint'),
        ),
    ]
