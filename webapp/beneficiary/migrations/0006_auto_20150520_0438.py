# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaries', '__first__'),
        ('beneficiary', '0005_auto_20150520_0435'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiary',
            name='accept_meat_issue',
            field=models.ManyToManyField(related_name='meat_issues_by_beneficiaries', verbose_name='We accept:', to='dictionaries.MeatIssues'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='accept_rel_issue',
            field=models.ManyToManyField(related_name='rel_issues_by_beneficiaries', verbose_name='We accept:', to='dictionaries.ReligiousIssues'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='last_delivery',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
