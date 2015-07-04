# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, date
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from model_mommy import mommy
from django.db.models.signals import post_save
from profiles.models import create_defaults

from beneficiary.models import BeneficiaryGroup, Beneficiary, DeliveryTimeWindows
from dictionaries.models import FoodCategory, MeatIssues, ReligiousIssues, PackagingCategory, TemperatureCategory, FoodIngredients, DaysOfTheWeek
from donor.models import Offer, OfferRepetition
from profiles.models import Profile, Organization
from .models import TemporalMatching

import pytz
import logging

logger = logging.getLogger(__name__)

from matcher import find_offers_for, find_beneficiaries_for, find_existing_matches_for, match


class TestFindOffers(TestCase):

    def setUp(self):
        print "setUp"
        post_save.disconnect(create_defaults, sender=User)
        self.user = mommy.make(User)
        post_save.connect(create_defaults, sender=User)

    def test_simple_date(self):
        print "simple"
        today = date.today()
        mommy.make(Offer, date=today+timedelta(days=1), donor=self.user)
        mommy.make(Offer, date=today+timedelta(days=-1), donor=self.user)
        offers = find_offers_for(today)
        self.assertEqual(len(offers), 0)

        mommy.make(Offer, date=today, donor=self.user)
        offers = find_offers_for(today)
        self.assertEqual(len(offers), 1)

    def test_repetitions_from_to(self):
        today = timezone.now()
        offer = mommy.make(Offer, date=None, donor=self.user)
        rep1 = mommy.make(OfferRepetition, day_of_week=today.weekday(),
                                            date_start=today+timedelta(days=-1, hours=-1),
                                            date_stop=today+timedelta(days=1, hours=1),
                                            day_freq=0,
                                            offer=offer)
        # Offer is for the same day as the test is run
        # It's valid since yesterday till tomorrow but since we have day_of_week set it's valid only today
        # It's invalid next week on the same weekday as the date_stop constrain will forbid this.
        self.assertEqual(len(find_offers_for(today)), 1)# today is fine

        self.assertEqual(len(find_offers_for(today-timedelta(days=-1))), 0)# yesterday is a different weekday
        self.assertEqual(len(find_offers_for(today+timedelta(days=1))), 0)# the same tomorrow, different weekday
        self.assertEqual(len(find_offers_for(today+timedelta(days=7))), 0)# next week is too late

        offer.date = today+timedelta(days=7)# we accept food 7 days from now (date_stop contrain is valid only for repetition)
        self.assertEqual(len(find_offers_for(today)), 1) # today is still valid
        self.assertEqual(len(find_offers_for(today-timedelta(days=-1))), 0)# invalid
        self.assertEqual(len(find_offers_for(today+timedelta(days=1))), 0)# invalid
        self.assertEqual(len(find_offers_for(today+timedelta(days=7))), 0)# valid as date in offer accept this

    def test_repetition_day_of_the_week(self):
        # 1st June 2015 is Monday
        # 1st July 2015 is Wednesday, the repetitions ends at Tuesday, 30th of June at 23:59
        start_date = datetime.strptime('2015-06-01', '%Y-%m-%d')
        end_date = datetime.strptime('2015-07-01', '%Y-%m-%d')

        offer = mommy.make(Offer, date=None, donor=self.user)
        # Every Monday:
        mommy.make(OfferRepetition, day_of_week=0,
                                            date_start=start_date, date_stop=end_date,
                                            day_freq=0, offer=offer)
        # First Tuesday:
        mommy.make(OfferRepetition, day_of_week=1,
                                            date_start=start_date, date_stop=end_date,
                                            day_freq=1, offer=offer)
        # Second and Third Wednesday:
        mommy.make(OfferRepetition, day_of_week=2,
                                            date_start=start_date, date_stop=end_date,
                                            day_freq=2, offer=offer)
        mommy.make(OfferRepetition, day_of_week=2,
                                            date_start=start_date, date_stop=end_date,
                                            day_freq=3, offer=offer)
        # Fourth Thursday:
        mommy.make(OfferRepetition, day_of_week=3,
                                            date_start=start_date, date_stop=end_date,
                                            day_freq=4, offer=offer)
        day0 = start_date

        self.assertEqual(len(find_offers_for(day0)), 1)# First Monday
        self.assertEqual(len(find_offers_for(day0+timedelta(days=7))), 1)   # Second Monday
        self.assertEqual(len(find_offers_for(day0+timedelta(days=14))), 1)  # Second Monday
        self.assertEqual(len(find_offers_for(day0+timedelta(days=21))), 1)  # Third Monday
        self.assertEqual(len(find_offers_for(day0+timedelta(days=28))), 1)  # Fourth Monday

        self.assertEqual(len(find_offers_for(day0+timedelta(days=1))), 1)   # First Tuesday
        self.assertEqual(len(find_offers_for(day0+timedelta(days=1+7))), 0)
        self.assertEqual(len(find_offers_for(day0+timedelta(days=1+14))), 0)
        self.assertEqual(len(find_offers_for(day0+timedelta(days=1+28))), 0)

        self.assertEqual(len(find_offers_for(day0+timedelta(days=2))), 0)   # First Wednesday
        self.assertEqual(len(find_offers_for(day0+timedelta(days=2+7))), 1)
        self.assertEqual(len(find_offers_for(day0+timedelta(days=2+14))), 1)
        self.assertEqual(len(find_offers_for(day0+timedelta(days=2+28))), 0)

        self.assertEqual(len(find_offers_for(day0+timedelta(days=3))), 0)   # First Thursday
        self.assertEqual(len(find_offers_for(day0+timedelta(days=3+7))), 0)
        self.assertEqual(len(find_offers_for(day0+timedelta(days=3+14))), 0)
        self.assertEqual(len(find_offers_for(day0+timedelta(days=3+28))), 0)# July

        self.assertEqual(len(find_offers_for(day0+timedelta(days=4))), 0)   # First Friday
        self.assertEqual(len(find_offers_for(day0+timedelta(days=4+7))), 0)
        self.assertEqual(len(find_offers_for(day0+timedelta(days=4+14))), 0)
        self.assertEqual(len(find_offers_for(day0+timedelta(days=4+28))), 0)# July


class TestBeneficiaryLookupByDate(TestCase):

    def setUp(self):
        post_save.disconnect(create_defaults, sender=User)
        self.user = mommy.make(User)
        self.beneficiary = mommy.make(Beneficiary, user=self.user)
        post_save.connect(create_defaults, sender=User)

    def test_timewindows_day_of_the_week(self):
        # 1st June 2015 is Monday
        # 1st July 2015 is Wednesday, the repetitions ends at Tuesday, 30th of June at 23:59
        day0 = datetime.strptime('2015-06-01', '%Y-%m-%d')

        dtw0 = mommy.make(DeliveryTimeWindows, beneficiary=self.beneficiary,
                                    day_of_week=0)
        # day0, day before, day after
        self.assertEqual(len(find_beneficiaries_for(day0)), 1)
        self.assertEqual(len(find_beneficiaries_for(day0+timedelta(days=-1))), 0)
        self.assertEqual(len(find_beneficiaries_for(day0+timedelta(days=1))), 0)
        self.assertEqual(len(find_beneficiaries_for(day0+timedelta(days=2))), 0)
        # next week Monday
        self.assertEqual(len(find_beneficiaries_for(day0+timedelta(days=7))), 1)# Monday 8th
        self.assertEqual(len(find_beneficiaries_for(day0+timedelta(days=14))), 1)
        self.assertEqual(len(find_beneficiaries_for(day0+timedelta(days=21))), 1)
        self.assertEqual(len(find_beneficiaries_for(day0+timedelta(days=28))), 1)

        dtw1 = mommy.make(DeliveryTimeWindows, beneficiary=self.beneficiary,
                                    day_of_week=1)
        self.assertEqual(len(find_beneficiaries_for(day0)), 1)# Monday 1th
        self.assertEqual(len(find_beneficiaries_for(day0+timedelta(days=1))), 1)# Tuesday
        self.assertEqual(len(find_beneficiaries_for(day0+timedelta(days=8))), 1)
        self.assertEqual(len(find_beneficiaries_for(day0+timedelta(days=22))), 1)

        self.assertEqual(len(find_beneficiaries_for(day0+timedelta(days=2))), 0)# Wednesday
        self.assertEqual(len(find_beneficiaries_for(day0+timedelta(days=3))), 0)
        self.assertEqual(len(find_beneficiaries_for(day0+timedelta(days=4))), 0)
        self.assertEqual(len(find_beneficiaries_for(day0+timedelta(days=2+7))), 0)# Wednesday
        self.assertEqual(len(find_beneficiaries_for(day0+timedelta(days=3+7))), 0)
        self.assertEqual(len(find_beneficiaries_for(day0+timedelta(days=4+7))), 0)


class TestExistingMatchFilter(TestCase):

    def setUp(self):
        post_save.disconnect(create_defaults, sender=User)
        self.user0 = mommy.make(User)
        self.user1 = mommy.make(User)
        self.user3 = mommy.make(User)

        self.beneficiary = mommy.make(Beneficiary, user=self.user3)
        post_save.connect(create_defaults, sender=User)

    def test_existing_matches(self):
        day0 = date.today()
        self.assertEqual(len(find_existing_matches_for(day0)), 0)

        offer0 = mommy.make(Offer, donor=self.user0)
        # old match
        mommy.make(TemporalMatching, offer=offer0, beneficiary=self.beneficiary, date=day0+timedelta(days=-1))
        self.assertEqual(len(find_existing_matches_for(day0)), 0)
        # future match, should be ignored as we are looking for matches for day0
        mommy.make(TemporalMatching, offer=offer0, beneficiary=self.beneficiary, date=day0+timedelta(days=1))
        self.assertEqual(len(find_existing_matches_for(day0)), 0)

        # match for today
        mommy.make(TemporalMatching, offer=offer0, beneficiary=self.beneficiary, date=day0)
        matches = find_existing_matches_for(day0)
        self.assertEqual(len(matches), 1)
        self.assertTrue('%d-%d' % (offer0.id, self.beneficiary.id) in matches)
        # tomorrow
        matches = find_existing_matches_for(day0+timedelta(days=1))
        self.assertEqual(len(matches), 1)
        self.assertTrue('%d-%d' % (offer0.id, self.beneficiary.id) in matches)

        offer1 = mommy.make(Offer, donor=self.user1)
        mommy.make(TemporalMatching, offer=offer1, beneficiary=self.beneficiary, date=day0)
        matches = find_existing_matches_for(day0)
        self.assertEqual(len(matches), 2)
        self.assertTrue('%d-%d' % (offer0.id, self.beneficiary.id) in matches)
        self.assertTrue('%d-%d' % (offer1.id, self.beneficiary.id) in matches)


class TestMatch(TestCase):

    def setUp(self):
        post_save.disconnect(create_defaults, sender=User)
        self.user0 = mommy.make(User)
        self.user1 = mommy.make(User)
        self.user2 = mommy.make(User)
        self.user3 = mommy.make(User)
        self.user4 = mommy.make(User)
        self.beneficiary = mommy.make(Beneficiary, user=self.user3)
        post_save.connect(create_defaults, sender=User)

        self.category0 = mommy.make(FoodCategory)
        self.category1 = mommy.make(FoodCategory)

        self.group0 = mommy.make(BeneficiaryGroup)
        self.group1 = mommy.make(BeneficiaryGroup)

    def test_food_group_match(self):
        beneficiary0 = mommy.make(Beneficiary, user=self.user0,
                                    group=self.group0)
        beneficiary0.food_category.add(self.category0)
        beneficiary0.save()
        beneficiary1 = mommy.make(Beneficiary, user=self.user1,
                                    group=self.group1)
        beneficiary1.food_category.add(self.category0)
        beneficiary1.save()

        offer0 = mommy.make(Offer, donor=self.user2, food_category=self.category0)

        self.assertFalse(match(offer0, beneficiary0))
        self.assertFalse(match(offer0, beneficiary1))

        offer0.beneficiary_group.add(self.group0)

        self.assertTrue(match(offer0, beneficiary0))
        self.assertFalse(match(offer0, beneficiary1))

        offer0.beneficiary_group.add(self.group1)

        self.assertTrue(match(offer0, beneficiary0))
        self.assertTrue(match(offer0, beneficiary1))

        offer1 = mommy.make(Offer, donor=self.user4, food_category=self.category1)
        offer1.beneficiary_group.add(self.group0)

        # group correct, food category not
        self.assertFalse(match(offer1, beneficiary0))
        self.assertFalse(match(offer1, beneficiary1))

        beneficiary0.food_category.add(self.category1)
        self.assertTrue(match(offer1, beneficiary0))
        self.assertFalse(match(offer1, beneficiary1))


class TestQuantityMonitor(TestCase):

    def setUp(self):
        post_save.disconnect(create_defaults, sender=User)
        self.user0 = mommy.make(User)
        self.user1 = mommy.make(User)
        self.user2 = mommy.make(User)

        self.category0 = mommy.make(FoodCategory)
        self.group0 = mommy.make(BeneficiaryGroup)

    def test_quantity_correct_full(self):
        from donor.models import process_new_offer
        from beneficiary.models import process_new_beneficiary

        post_save.disconnect(process_new_offer, sender=Offer)
        post_save.disconnect(process_new_beneficiary, sender=Beneficiary)

        # beneficiary for today
        beneficiary0 = mommy.make(Beneficiary, user=self.user0, group=self.group0)

        # new offer
        offer0 = mommy.make(Offer,
                            estimated_mass=100,
                            donor=self.user1,
                            food_category=self.category0,
                            date=date.today())

        match0 = mommy.make(TemporalMatching,
                           offer=offer0,
                           beneficiary=beneficiary0,
                           date=date.today(),
                           quantity=0,
                           status=TemporalMatching.STATUS_PENDING)

        match1 = mommy.make(TemporalMatching,
                           offer=offer0,
                           date=date.today(),
                           quantity=0,
                           status=TemporalMatching.STATUS_PENDING)

        match0.status = TemporalMatching.STATUS_WAITING
        match0.save()
        self.assertIsNotNone(match0.waiting_since)

        match1.status = TemporalMatching.STATUS_WAITING
        match1.save()
        self.assertIsNotNone(match0.waiting_since)

        match0.status = TemporalMatching.STATUS_CONFIRMED
        match0.quantity = offer0.estimated_mass
        match0.save()
        print 'back to test'
        match1 = TemporalMatching.objects.get(id=match1.id)
        self.assertEqual(match1.status, TemporalMatching.STATUS_TOOLATE)

    def test_quantity_correct_half(self):
        from donor.models import process_new_offer
        from beneficiary.models import process_new_beneficiary

        post_save.disconnect(process_new_offer, sender=Offer)
        post_save.disconnect(process_new_beneficiary, sender=Beneficiary)

        # beneficiary for today
        beneficiary0 = mommy.make(Beneficiary, user=self.user0, group=self.group0)

        # new offer
        offer0 = mommy.make(Offer,
                            estimated_mass=7,
                            donor=self.user1,
                            food_category=self.category0,
                            date=date.today())

        match0 = mommy.make(TemporalMatching,
                           offer=offer0,
                           beneficiary=beneficiary0,
                           date=date.today(),
                           quantity=0,
                           status=TemporalMatching.STATUS_WAITING)

        match1 = mommy.make(TemporalMatching,
                           offer=offer0,
                           date=date.today(),
                           quantity=0,
                           status=TemporalMatching.STATUS_WAITING)

        match2 = mommy.make(TemporalMatching,
                           offer=offer0,
                           date=date.today(),
                           quantity=0,
                           status=TemporalMatching.STATUS_WAITING)

        match0.status = TemporalMatching.STATUS_CONFIRMED
        match0.quantity = offer0.estimated_mass / 2
        match0.save()
        self.assertEqual(TemporalMatching.objects.get(id=match1.id).status,
                         TemporalMatching.STATUS_WAITING)
        self.assertEqual(TemporalMatching.objects.get(id=match2.id).status,
                         TemporalMatching.STATUS_WAITING)

        match1.status = TemporalMatching.STATUS_CONFIRMED
        match1.quantity = offer0.estimated_mass / 2
        match1.save()
        self.assertEqual(TemporalMatching.objects.get(id=match2.id).status, TemporalMatching.STATUS_TOOLATE)


class TestTemporalMatchCreation(TestCase):
    def setUp(self):
        post_save.disconnect(create_defaults, sender=User)
        self.user0 = mommy.make(User)
        self.user1 = mommy.make(User)

        self.category0 = mommy.make(FoodCategory)
        self.group0 = mommy.make(BeneficiaryGroup)

    def test_beneficiaries(self):
        from donor.models import process_new_offer
        from beneficiary.models import process_new_beneficiary
        from .matcher import match_offers_to_beneficiaries

        post_save.disconnect(process_new_offer, sender=Offer)
        post_save.disconnect(process_new_beneficiary, sender=Beneficiary)

        # beneficiary for today
        beneficiary0 = mommy.make(Beneficiary, user=self.user0, group=self.group0)
        beneficiary0.food_category.add(self.category0)
        beneficiary0.save()
        mommy.make(DeliveryTimeWindows, beneficiary=beneficiary0, day_of_week=date.today().weekday())

        # new offer
        offer0 = mommy.make(Offer, donor=self.user1, food_category=self.category0, date=date.today())
        offer0.beneficiary_group.add(self.group0)
        offer0.save()
        offer1 = mommy.make(Offer, donor=self.user1, food_category=self.category0, date=date.today()+timedelta(days=1))
        offer1.beneficiary_group.add(self.group0)
        offer1.save()

        match_offers_to_beneficiaries(offer0, date.today())

        matches = TemporalMatching.objects.all()
        self.assertEqual(len(matches), 1)
        mommy.make(DeliveryTimeWindows, beneficiary=beneficiary0, day_of_week=date.today().weekday()+1)

        match_offers_to_beneficiaries(offer0, date.today())
        matches = TemporalMatching.objects.all()
        self.assertEqual(len(matches), 1)

        match_offers_to_beneficiaries(offer0, date.today(), 1)
        matches = TemporalMatching.objects.all()
        self.assertEqual(len(matches), 2)
        """
        match_offers_to_beneficiaries(offer1, date.today())
        matches = TemporalMatching.objects.all()
        self.assertEqual(len(matches), 2)

        match_offers_to_beneficiaries(offer1, date.today())
        matches = TemporalMatching.objects.all()
        self.assertEqual(len(matches), 2)
        """
        match_offers_to_beneficiaries(offer1, date.today()+timedelta(days=1))
        matches = TemporalMatching.objects.all()
        self.assertEqual(len(matches), 3)

        post_save.connect(process_new_offer, sender=Offer)
        post_save.connect(process_new_beneficiary, sender=Beneficiary)

    def test_donors(self):
        from donor.models import process_new_offer
        from beneficiary.models import process_new_beneficiary
        from .matcher import match_beneficiaries_to_offers
        post_save.disconnect(process_new_offer, sender=Offer)
        post_save.disconnect(process_new_beneficiary, sender=Beneficiary)

        offer1 = mommy.make(Offer, date=None, donor=self.user1,
                                food_category=self.category0)
        offer1.beneficiary_group.add(self.group0)
        offer1.save()
        mommy.make(OfferRepetition, day_of_week=date.today().weekday(),
                                            date_start=date.today(),
                                            date_stop=date.today()+timedelta(days=100),
                                            day_freq=0,
                                            offer=offer1)
        mommy.make(OfferRepetition, day_of_week=date.today().weekday()+1,
                                            date_start=date.today(),
                                            date_stop=date.today()+timedelta(days=100),
                                            day_freq=0,
                                            offer=offer1)

        beneficiary0 = mommy.make(Beneficiary, user=self.user0, group=self.group0)
        beneficiary0.food_category.add(self.category0)
        beneficiary0.save()
        mommy.make(DeliveryTimeWindows, beneficiary=beneficiary0, day_of_week=date.today().weekday())

        beneficiary1 = mommy.make(Beneficiary, user=self.user1, group=self.group0)
        beneficiary1.food_category.add(self.category0)
        beneficiary1.save()
        mommy.make(DeliveryTimeWindows, beneficiary=beneficiary1, day_of_week=date.today().weekday()+1)

        match_beneficiaries_to_offers(beneficiary0, date.today())

        matches = TemporalMatching.objects.all()
        self.assertEqual(len(matches), 1)

        # second call, no new objects
        match_beneficiaries_to_offers(beneficiary0, date.today())
        matches = TemporalMatching.objects.all()
        self.assertEqual(len(matches), 1)
        """
        # wrong day
        match_beneficiaries_to_offers(beneficiary1, date.today())
        matches = TemporalMatching.objects.all()
        self.assertEqual(len(matches), 1)
        """
        print 360
        match_beneficiaries_to_offers(beneficiary1, date.today()+timedelta(days=1))
        matches = TemporalMatching.objects.all()
        self.assertEqual(len(matches), 2)

        post_save.connect(process_new_offer, sender=Offer)
        post_save.connect(process_new_beneficiary, sender=Beneficiary)


class TestCheckTemporalMatches(TestCase):
    def setUp(self):
        post_save.disconnect(create_defaults, sender=User)
        self.user0 = mommy.make(User)
        self.user1 = mommy.make(User)

        self.category0 = mommy.make(FoodCategory)
        self.group0 = mommy.make(BeneficiaryGroup)

    def test_searching(self):
        from donor.models import process_new_offer
        from beneficiary.models import process_new_beneficiary
        from .matcher import check_temporal_matches, find_temporal_matches_to_check
        from random import randint

        # ???
        post_save.disconnect(process_new_offer, sender=Offer)
        post_save.disconnect(process_new_beneficiary, sender=Beneficiary)

        # beneficiary for today
        beneficiary0 = mommy.make(Beneficiary, user=self.user0, group=self.group0)
        beneficiary0.food_category.add(self.category0)
        beneficiary0.save()
        mommy.make(DeliveryTimeWindows, beneficiary=beneficiary0, day_of_week=date.today().weekday())

        # new offerts
        offerts = []
        for n in range(10):
            tmp_offer = mommy.make(Offer, donor=self.user1, food_category=self.category0, date=date.today()+timedelta(days = randint(0, 10)))
            tmp_offer.beneficiary_group.add(self.group0)
            tmp_offer.save()
            offerts.append(tmp_offer)

        mommy.make(DeliveryTimeWindows, beneficiary=beneficiary0, day_of_week=date.today().weekday()+1)

        mins = 0
        for offert in offerts:
            tmp_matching = mommy.make(TemporalMatching, offer=offert, beneficiary=beneficiary0, date=date.today(), status=3)
            tmp_matching.waiting_since = datetime.now()-timedelta(minutes=mins)
            tmp_matching.save()
            mins+=20

        self.assertEqual(len(find_temporal_matches_to_check()),10)

        check_temporal_matches()

        self.assertEqual(len(find_temporal_matches_to_check()),3)

        #co to jest?
        post_save.connect(process_new_offer, sender=Offer)
        post_save.connect(process_new_beneficiary, sender=Beneficiary)

