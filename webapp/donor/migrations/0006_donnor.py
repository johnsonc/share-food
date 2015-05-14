# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20150514_0501'),
        ('donor', '0005_auto_20150514_0527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donnor',
            fields=[
                ('organization_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='profiles.Organization')),
                ('default_beneficiary_group', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=('profiles.organization',),
        ),
    ]
