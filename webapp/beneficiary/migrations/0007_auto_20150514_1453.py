# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_remove_organization_donor'),
        ('beneficiary', '0006_beneficiary_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiary',
            name='beneficiary',
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='organization_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default='', serialize=False, to='profiles.Organization'),
            preserve_default=False,
        ),
    ]
