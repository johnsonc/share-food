from django.db import models


class Donnor(models.Model):
    id = models.ForeignKey('Organization', to_field='id')
    default_beneficiary_group = models.PositiveIntegerField()


class Offer(models.Model):
    donnor_id = models.ForeignKey('Organization', to_field='id')
    name = models.CharField(max_length=255)
    beneficiary_group = models.PositiveIntegerField()
    food_category = models.PositiveIntegerField()
    estimated_mass = models.PositiveIntegerField()
    contact_person = models.CharField(max_length=255)
    not_contain = models.PositiveIntegerField()
    meat_issue = models.PositiveSmallIntegerField()
    rel_issue = models.PositiveSmallIntegerField()
    temperature = models.PositiveSmallIntegerField()
    packaging = models.PositiveSmallIntegerField()
    date = models.DateField()
    time_from = models.PositiveIntegerField()
    time_to = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    driver_info = models.TextField()
    reapeating = models.BooleanField()
    open = models.BooleanField()


class OfferRepetition(models.Model):
    offer_id = models.ForeignKey('Offer', to_field='id')
    day_freq = models.PositiveSmallIntegerField()
    date_start = models.DateField()
    date_stop = models.DateField()
    day_of_week = models.PositiveSmallIntegerField()
