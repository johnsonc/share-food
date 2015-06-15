# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0011_auto_20150612_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitpoint',
            name='routing',
            field=models.ForeignKey(related_name='visitpoints', blank=True, to='matcher.Routing', null=True),
        ),
    ]
