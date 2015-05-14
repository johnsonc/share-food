# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dictionary',
            options={'verbose_name': 'Dictionary', 'verbose_name_plural': 'Dictionaries'},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'verbose_name': 'Organization', 'verbose_name_plural': 'Organizations'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.RemoveField(
            model_name='organization',
            name='address_lat',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='address_lon',
        ),
        migrations.AddField(
            model_name='organization',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True),
            preserve_default=True,
        ),
    ]
