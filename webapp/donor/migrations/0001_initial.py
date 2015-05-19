# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaries', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beneficiary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('default_beneficiary_group', models.ManyToManyField(to='beneficiary.BeneficiaryGroup', verbose_name='Beneficiary group')),
                ('user', models.OneToOneField(related_name='donor_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Delivery name')),
                ('estimated_mass', models.PositiveIntegerField()),
                ('contact_person', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255, verbose_name='Pick up address')),
                ('driver_info', models.TextField(null=True, verbose_name='Driver information', blank=True)),
                ('time_from', models.DateTimeField(default=datetime.datetime(2015, 5, 19, 9, 43, 13, 125268, tzinfo=utc))),
                ('time_to', models.DateTimeField(default=datetime.datetime(2015, 5, 20, 9, 43, 13, 125300, tzinfo=utc))),
                ('repeating', models.BooleanField(default=False)),
                ('open', models.BooleanField(default=False)),
                ('beneficiary_group', models.ManyToManyField(to='beneficiary.BeneficiaryGroup', verbose_name='Beneficiary group')),
                ('donor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('food_category', models.ForeignKey(verbose_name='Food category', to='dictionaries.FoodCategory')),
                ('meat_issue', models.ForeignKey(to='dictionaries.MeatIssues')),
                ('not_contain', models.ManyToManyField(to='dictionaries.FoodIngredients', null=True, blank=True)),
                ('packaging', models.ForeignKey(to='dictionaries.PackagingCategory')),
                ('rel_issue', models.ForeignKey(to='dictionaries.ReligiousIssues')),
                ('temperature', models.ForeignKey(to='dictionaries.TemperatureCategory')),
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
                ('day_freq', models.PositiveSmallIntegerField(verbose_name='Day frequency')),
                ('date_start', models.DateField()),
                ('date_stop', models.DateField()),
                ('days_of_week', models.ManyToManyField(to='dictionaries.DaysOfTheWeek', null=True, blank=True)),
                ('offer', models.ForeignKey(to='donor.Offer')),
            ],
            options={
                'verbose_name': 'Repetition',
                'verbose_name_plural': 'Repetitions',
            },
            bases=(models.Model,),
        ),
    ]
