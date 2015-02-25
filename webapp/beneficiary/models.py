from django.db import models


class Beneficiary(models.Model):
    id = models.ForeignKey('Organization', to_field='id', unique=True)
    group_id = models.AutoField()
    num_meals = models.PositiveIntegerField()
    frozen_capacity = models.PositiveIntegerField()
    refrigerated_capacity = models.PositiveIntegerField()
    drystorage_capacity = models.PositiveIntegerField()
    food_category = models.PositiveIntegerField()
    dont_accept = models.PositiveIntegerField()
    accept_meat_issue = models.PositiveSmallIntegerField()
    accept_rel_issue = models.PositiveSmallIntegerField()
    preference_info = models.TextField()
    last_delivery = models.DateField()


class DeliveryTimeWindows(models.Model):
    beneficiary_id = models.ForeignKey('Beneficiary', to_field='id')
    day_of_week = models.PositiveSmallIntegerField()
    time_from = models.PositiveIntegerField()
    time_to = models.PositiveIntegerField()

