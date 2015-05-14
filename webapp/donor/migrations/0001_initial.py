# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150513_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('beneficiary_group', models.PositiveIntegerField()),
                ('food_category', models.PositiveIntegerField()),
                ('estimated_mass', models.PositiveIntegerField()),
                ('contact_person', models.CharField(max_length=255)),
                ('not_contain', models.PositiveIntegerField()),
                ('meat_issue', models.PositiveSmallIntegerField()),
                ('rel_issue', models.PositiveSmallIntegerField()),
                ('temperature', models.PositiveSmallIntegerField()),
                ('packaging', models.PositiveSmallIntegerField()),
                ('date', models.DateField()),
                ('time_from', models.PositiveIntegerField()),
                ('time_to', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=255)),
                ('driver_info', models.TextField()),
                ('repeating', models.BooleanField(default=False)),
                ('open', models.BooleanField(default=False)),
                ('donor', models.ForeignKey(to='profiles.Organization')),
            ],
            options={
                'verbose_name': 'Offer',
                'verbose_name_plural': 'Offers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OfferRepetition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day_freq', models.PositiveSmallIntegerField()),
                ('date_start', models.DateField()),
                ('date_stop', models.DateField()),
                ('day_of_week', models.PositiveSmallIntegerField()),
                ('offer_id', models.ForeignKey(to='donor.Offer')),
            ],
            options={
                'verbose_name': 'Repetition',
                'verbose_name_plural': 'Repetitions',
            },
            bases=(models.Model,),
        ),
    ]
