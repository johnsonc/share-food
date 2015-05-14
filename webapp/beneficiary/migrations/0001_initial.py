# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20150514_0501'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('beneficiary', models.OneToOneField(primary_key=True, serialize=False, to='profiles.Organization')),
                ('group', models.CharField(max_length=255)),
                ('num_meals', models.PositiveIntegerField()),
                ('frozen_capacity', models.PositiveIntegerField()),
                ('refrigerated_capacity', models.PositiveIntegerField()),
                ('drystorage_capacity', models.PositiveIntegerField()),
                ('food_category', models.PositiveIntegerField()),
                ('dont_accept', models.PositiveIntegerField()),
                ('accept_meat_issue', models.PositiveSmallIntegerField()),
                ('accept_rel_issue', models.PositiveSmallIntegerField()),
                ('preference_info', models.TextField()),
                ('last_delivery', models.DateField()),
            ],
            options={
                'verbose_name': 'Beneficiary',
                'verbose_name_plural': 'Beneficiaries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeliveryTimeWindows',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day_of_week', models.PositiveSmallIntegerField()),
                ('time_from', models.PositiveIntegerField()),
                ('time_to', models.PositiveIntegerField()),
                ('beneficiary', models.ForeignKey(related_name='deliveries', to='beneficiary.Beneficiary')),
            ],
            options={
                'verbose_name': 'Delivery',
                'verbose_name_plural': 'Deliveries',
            },
            bases=(models.Model,),
        ),
    ]
