from django.db import models
from django.utils.translation import ugettext as _

"""
TODO remove this class, ask Jacek
"""
"""
class Donnor(models.Model):
    id = models.ForeignKey('Organization', to_field='id')
    default_beneficiary_group = models.PositiveIntegerField()
"""


class Offer(models.Model):
    donor = models.ForeignKey('profiles.Organization', to_field='id')
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
    time_from = models.TimeField()
    time_to = models.TimeField()
    address = models.CharField(max_length=255)
    driver_info = models.TextField()
    repeating = models.BooleanField(default=False)
    open = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Offer')
        verbose_name_plural = _('Offers')

    def __unicode__(self):
        return self.name


class OfferRepetition(models.Model):
    DAYS_OF_THE_WEEK = (
        ('Mon', _('Monday')),
        ('Tue', _('Tuesday')),
        ('Wed', _('Wednesday')),
        ('Thu', _('Thursday')),
        ('Fri', _('Friday')),
        ('Sat', _('Saturday')),
        ('Sun', _('Sunday'))

    )
    offer = models.ForeignKey(Offer)
    day_freq = models.PositiveSmallIntegerField()
    date_start = models.DateField()
    date_stop = models.DateField()
    day_of_week = models.CharField(max_length=3, choices=DAYS_OF_THE_WEEK)

    class Meta:
        verbose_name = _('Repetition')
        verbose_name_plural = _('Repetitions')

    def __unicode__(self):
        return '%s repetition' % self.offer.name