from datetime import datetime
from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models.signals import post_save, post_delete
from profiles.models import Organization
from django.contrib.auth.models import User
from beneficiary.models import BeneficiaryGroup
from dictionaries.models import FoodCategory, MeatIssues, ReligiousIssues, PackagingCategory, TemperatureCategory, FoodIngredients, DaysOfTheWeek
from profiles.models import DAYS_OF_THE_WEEK
from datetime import date
import pytz


class Donor(models.Model):
    default_beneficiary_group = models.ManyToManyField(BeneficiaryGroup, verbose_name=_('Beneficiary group'))
    user = models.OneToOneField(User, related_name='donor_group')


class Offer(models.Model):
    donor = models.ForeignKey(User, related_name='donor_profile')
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

    date = models.DateField(default=timezone.now(), verbose_name=_('Offer available at'), blank=True, null=True)

    time_from = models.TimeField(default=timezone.now())
    time_to = models.TimeField(default=(timezone.now() + timedelta(hours=8)))

    valid_to = models.DateField(default=(timezone.now() + timedelta(days=1)), blank=True, null=True)

    repeating = models.BooleanField(default=False)
    open = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Offer')
        verbose_name_plural = _('Offers')

    def __unicode__(self):
        return self.name


def process_new_offer(sender, instance, created, **kwargs):
    from matcher.matcher import match_offers_to_beneficiaries
    match_offers_to_beneficiaries(instance, date.today(), 7)

post_save.connect(process_new_offer, sender=Offer)


class OfferRepetition(models.Model):
    DAYWEEK_OF_THE_MONTH = (
        (0, _('Every week')),
        (1, _('1st in the month')),
        (2, _('2nd in the month')),
        (3, _('3rd in the month')),
        (4, _('4th in the month')),
    )
    offer = models.ForeignKey(Offer, related_name='repetitions')
    date_start = models.DateTimeField(default=timezone.now())
    date_stop = models.DateTimeField(default=timezone.now())
    day_of_week = models.IntegerField(choices=DAYS_OF_THE_WEEK)
    day_freq = models.PositiveSmallIntegerField(verbose_name=_('Day frequency'), choices=DAYWEEK_OF_THE_MONTH)

    class Meta:
        verbose_name = _('Repetition')
        verbose_name_plural = _('Repetitions')

    def __unicode__(self):
        return '%s repetition' % self.offer.name


def repetition_added(sender, instance, created, **kwargs):
    if created:
        instance.offer.repeating = True
        instance.save()


def repetition_deleted(sender, instance, **kwargs):
    if instance.offer.repetitions.count() > 0:
        instance.offer.repeating = True
    else:
        instance.offer.repeating = False

post_save.connect(repetition_added, sender=OfferRepetition)
post_delete.connect(repetition_deleted, sender=OfferRepetition)