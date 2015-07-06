# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0010_auto_20150704_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiary',
            name='accept_meat_issue',
            field=models.ManyToManyField(related_name='meat_issues_by_beneficiaries', null=True, verbose_name='We accept:', to='dictionaries.MeatIssues', blank=True),
            preserve_default=True,
        ),
    ]
