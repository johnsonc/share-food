# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0015_auto_20150519_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='rel_issue',
            field=models.ForeignKey(to='dictionaries.ReligiousIssues'),
            preserve_default=True,
        ),
    ]
