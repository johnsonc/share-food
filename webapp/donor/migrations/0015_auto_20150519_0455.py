# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0014_auto_20150519_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='meat_issue',
            field=models.ForeignKey(to='dictionaries.MeatIssues'),
            preserve_default=True,
        ),
    ]
