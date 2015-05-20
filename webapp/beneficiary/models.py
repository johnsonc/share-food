from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from profiles.models import Organization
from dictionaries.models import FoodCategory, FoodIngredients, MeatIssues, ReligiousIssues

class BeneficiaryGroup(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Beneficiary(models.Model):
    group = models.ForeignKey(BeneficiaryGroup, blank=True, null=True)
    num_meals = models.PositiveIntegerField(_('Number of meals served every day'))
    frozen_capacity = models.PositiveIntegerField(_('frozen'))
    refrigerated_capacity = models.PositiveIntegerField(_('refrigerated'))
    drystorage_capacity = models.PositiveIntegerField(_('dry storage'))
    food_category = models.ManyToManyField(FoodCategory, related_name='food_accepted_by_beneficiaries',
                                           verbose_name=_('We would like to receive:'))
    dont_accept = models.ManyToManyField(FoodIngredients, related_name='ingredients_rejected_by_beneficiaries',
                                         verbose_name=_("We don't accept food CONTAINING:"))
    accept_meat_issue = models.ManyToManyField(MeatIssues, related_name='meat_issues_by_beneficiaries',
                                         verbose_name=_("We accept:"))

    accept_rel_issue = models.ManyToManyField(ReligiousIssues, related_name='rel_issues_by_beneficiaries',
                                         verbose_name=_("We accept:"))
    preference_info = models.TextField(_('Additional info:'))
    last_delivery = models.DateField(blank=True, null=True)

    user = models.OneToOneField(User)

    class Meta:
        verbose_name = _('Beneficiary')
        verbose_name_plural = _('Beneficiaries')

    def __unicode__(self):
        return self.user.username


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

