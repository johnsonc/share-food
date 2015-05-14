from django.db import models
from django.utils.translation import ugettext as _
from profiles.models import Organization


class BeneficiaryGroup(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Beneficiary(Organization):
    group = models.ForeignKey(BeneficiaryGroup, related_name='beneficiaries', blank=True, null=True)
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

    class Meta:
        verbose_name = _('Beneficiary')
        verbose_name_plural = _('Beneficiaries')

    def __unicode__(self):
        return self.beneficiary.name


class DeliveryTimeWindows(models.Model):
    DAYS_OF_THE_WEEK = (
        ('Mon', _('Monday')),
        ('Tue', _('Tuesday')),
        ('Wed', _('Wednesday')),
        ('Thu', _('Thursday')),
        ('Fri', _('Friday')),
        ('Sat', _('Saturday')),
        ('Sun', _('Sunday'))

    )
    beneficiary = models.ForeignKey(Beneficiary, related_name='deliveries')
    day_of_week = models.CharField(max_length=3, choices=DAYS_OF_THE_WEEK)
    time_from = models.TimeField()
    time_to = models.TimeField()

    class Meta:
        verbose_name = _('Delivery')
        verbose_name_plural = _('Deliveries')

    def __unicode__(self):
        return 'delivery for %s' % self.beneficiary

