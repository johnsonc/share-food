# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0009_deliverytimewindows_day_of_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiary',
            name='accept_rel_issue',
            field=models.ManyToManyField(related_name='rel_issues_by_beneficiaries', null=True, verbose_name='We accept:', to='dictionaries.ReligiousIssues', blank=True),
            preserve_default=True,
        ),
    ]
