__author__ = 'darek'

from donor.models import Offer
from beneficiary.models import Beneficiary


def match_preferences(offer, beneficiary):
    pass


def get_offer_for(date):
    return Offer.objects.filter(Q(repetitions__day_of_week=1) & (Q(repetitions__day_freq=0)|Q(repetitions__day_freq=3)))
    pass


def get_beneficiaries_for(date):
    pass

