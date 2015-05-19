from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime, timedelta
from django.utils import timezone
from profiles.models import Organization
from beneficiary.models import BeneficiaryGroup
from dictionaries.models import FoodCategory, MeatIssues, ReligiousIssues, PackagingCategory, TemperatureCategory, FoodIngredients, DaysOfTheWeek
import pytz

class Donnor(Organization):
    default_beneficiary_group = models.ManyToManyField(BeneficiaryGroup, verbose_name=_('Beneficiary group'))


class Offer(models.Model):
    donor = models.ForeignKey('profiles.Organization', to_field='id')
    name = models.CharField(_('Delivery name'), max_length=255)

    food_category = models.ForeignKey(FoodCategory, verbose_name=_('Food category'))
    estimated_mass = models.PositiveIntegerField()
    contact_person = models.CharField(max_length=255)

    beneficiary_group = models.ManyToManyField(BeneficiaryGroup, verbose_name=_('Beneficiary group'))

    meat_issue = models.ForeignKey(MeatIssues)
    rel_issue = models.ForeignKey(ReligiousIssues)

    packaging = models.ForeignKey(PackagingCategory)
    temperature = models.ForeignKey(TemperatureCategory)
    not_contain = models.ManyToManyField(FoodIngredients, blank=True, null=True)

    address = models.CharField(max_length=255, verbose_name=_('Pick up address'))
    driver_info = models.TextField(blank=True, null=True, verbose_name=_('Driver information'))

    time_from = models.DateTimeField(default=timezone.now())
    time_to = models.DateTimeField(default=(timezone.now() + timedelta(days=1)))

    repeating = models.BooleanField(default=False)
    open = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Offer')
        verbose_name_plural = _('Offers')

    def __unicode__(self):
        return self.name


class OfferRepetition(models.Model):
    """
    DAYS_OF_THE_WEEK = (
        ('Mon', _('Monday')),
        ('Tue', _('Tuesday')),
        ('Wed', _('Wednesday')),
        ('Thu', _('Thursday')),
        ('Fri', _('Friday')),
        ('Sat', _('Saturday')),
        ('Sun', _('Sunday'))

    )
    """
    offer = models.ForeignKey(Offer)
    day_freq = models.PositiveSmallIntegerField(verbose_name=_('Day frequency'))
    date_start = models.DateField()
    date_stop = models.DateField()
    days_of_week = models.ManyToManyField(DaysOfTheWeek, blank=True, null=True)
    #day_of_week = models.CharField(max_length=3, choices=DAYS_OF_THE_WEEK)

    class Meta:
        verbose_name = _('Repetition')
        verbose_name_plural = _('Repetitions')

    def __unicode__(self):
        return '%s repetition' % self.offer.name