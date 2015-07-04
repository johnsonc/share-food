__author__ = 'darek'
from django.db.models import Q

from datetime import datetime, timedelta, date
from django.utils import timezone
import logging
import random
from django.conf import settings
from django.conf import settings

from donor.models import Offer
from beneficiary.models import Beneficiary
from .models import TemporalMatching, Driver, Routing, VisitPoint

logger = logging.getLogger(__name__)

if "pinax.notifications" in settings.INSTALLED_APPS:
    from pinax.notifications import models as notification
else:
    notification = None


def cancel_temporal_match(temporalmatching):
    print 'cancel from matcher'
    to_notify = [temporalmatching.offer.donor, temporalmatching.beneficiary.user]
    print to_notify
    if temporalmatching.status in [TemporalMatching.STATUS_ASSIGNED, TemporalMatching.STATUS_NOTIFIED]:
        # temporal matching has a driver and visit points
        to_notify.append(temporalmatching.driver)
        visitpoints = VisitPoint.objects.filter(matched=temporalmatching)
        for vp in visitpoints:
            vp.status = VisitPoint.STATUS_CANCELED
            vp.save()

    temporalmatching.status = TemporalMatching.STATUS_CANCELED
    temporalmatching.save()
    print 'status seted up'
    if notification:
        notification.send(to_notify, 'transaction_canceled', {})


def assign_driver_to_match(driver, temporal_matching):
    routing, created = Routing.objects.get_or_create(driver=driver, date=temporalmatching.date)
    visit_points = VisitPoint.objects.filter(routing=routing).order_by('-seq_num')
    seq_num = 0 if len(visit_points) == 0 else visit_points[0].seq_num + 1
    start = VisitPoint(seq_num=seq_num,
                       matched=temporal_matching,
                       status=VisitPoint.STATUS_PENDING,
                       donor=True,
                       routing=routing)
    start.save()
    stop = VisitPoint(seq_num=seq_num+1,
                      matched=temporal_matching,
                      status=VisitPoint.STATUS_PENDING,
                      donor=False,
                      routing=routing)
    stop.save()


def find_offers_for(date):
    logger.info("find_offers_for:%s" % str(date))
    offers_for_today = set()
    # days methoned directly in offer
    [offers_for_today.add(x) for x in Offer.objects.filter(date=date)]
    logger.info("found %d based on Offer.date" % len(offers_for_today))

    # days based on repetition
    day_position_in_month = (date.day / 7) + 1
    repetition_offers = Offer.objects.filter(Q(repetitions__day_of_week=date.weekday()) &
                                             Q(repetitions__date_start__lte=date) &
                                             Q(repetitions__date_stop__gte=date) &
                    (Q(repetitions__day_freq=0) | Q(repetitions__day_freq=day_position_in_month)))
    logger.info("found based on repetitions %d" % len(repetition_offers))

    [offers_for_today.add(x) for x in repetition_offers]

    return offers_for_today


def find_beneficiaries_for(for_date):
    return Beneficiary.objects.filter(Q(deliveries__day_of_week=for_date.weekday()))


def find_existing_matches_for(for_date):
    existing_matches = set()
    for x in TemporalMatching.objects.filter(date=for_date):
        existing_matches.add('%d-%d' % (x.offer.id, x.beneficiary.id))
    return existing_matches


def match(offer, beneficiary):
    #offer.beneficiary_group * -- beneficiary.group 1
    if beneficiary.group not in offer.beneficiary_group.all():
        return False

    #offer.food_category 1 -- beneficiary.food_category *
    if offer.food_category not in beneficiary.food_category.all():
        return False

    return True


def match_offers_to_beneficiaries(offer, start_date, delta=0):
    random.seed(start_date)
    # TODO maybe we should check if offer is for today
    for d in range(delta+1):
        day = start_date + timedelta(days=d)
        existing_matches = find_existing_matches_for(day)
        beneficiaries_for_day = find_beneficiaries_for(day)
        for beny in beneficiaries_for_day:
            if '%d-%d' % (offer.id, beny.id) in existing_matches:
                continue
            if match(offer, beny):
                tm = TemporalMatching(offer=offer,
                                      beneficiary=beny,
                                      date=day,
                                      beneficiary_contact_person=beny.user.username,
                                      quantity=0,
                                      status=TemporalMatching.STATUS_PENDING,
                                      driver=None,
                                      hash=random.randint(1000, 1000000))
                tm.save()


def match_beneficiaries_to_offers(beneficiary, start_date, delta=0):
    # TODO maybe we should check if beneficiary is for today
    for d in range(delta+1):
        day = start_date + timedelta(days=d)
        existing_matches = find_existing_matches_for(day)
        offers_for_day = find_offers_for(day)
        for offer in offers_for_day:
            if '%d-%d' % (offer.id, beneficiary.id) in existing_matches:
                continue
            if match(offer, beneficiary):
                tm = TemporalMatching(offer=offer,
                                      beneficiary=beneficiary,
                                      date=day,
                                      beneficiary_contact_person=beneficiary.user.username,
                                      quantity=0,
                                      status=TemporalMatching.STATUS_PENDING,
                                      driver=None,
                                      hash=random.randint(1000, 1000000))
                tm.save()


def find_temporal_matches_to_check():
    time_range = timezone.now() - timedelta(hours=settings.CONFIRMATION_EXPIRE_TIME_RANGE)
    return TemporalMatching.objects.filter(waiting_since__lte=time_range, status=TemporalMatching.STATUS_WAITING)


def check_temporal_matches():
    temp_matches = find_temporal_matches_to_check()
    for temp_match in temp_matches:
        cancel_temporal_match(temp_match)

    if notification:
        notification.send([tm.beneficiary.user for tm in temp_matches],
                          "transaction_timeout", {})

