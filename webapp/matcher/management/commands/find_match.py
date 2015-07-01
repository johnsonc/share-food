__author__ = 'darek'
from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils import timezone
from datetime import date, timedelta
import logging
import random
import pytz

logger = logging.getLogger(__name__)

TIME_WINDOW = 7

from matcher.matcher import find_offers_for, match_offers_to_beneficiaries, find_existing_matches_for, find_beneficiaries_for, match
from matcher.matcher import TemporalMatching


class Command(BaseCommand):
    # TODO add timezone!!!
    def handle(self, *args, **options):

        timezone.activate(pytz.timezone(settings.TIME_ZONE))

        today = date.today()
        logger.info("Matching started for %s" % str(today))
        for d in range(TIME_WINDOW):

            today = today + timedelta(days=d)
            logger.info("Scan for %s" % str(today))

            existing_matches = find_existing_matches_for(today)

            offers = find_offers_for(today)
            beneficiaries = find_beneficiaries_for(today)

            for o in offers:
                for b in beneficiaries:
                    if '%d-%d' % (o.id, b.id) in existing_matches:
                        continue
                    if match(o, b):
                        tm = TemporalMatching(
                            offer=o,
                            beneficiary=b,
                            date=today,
                            beneficiary_contact_person=b.user.username,
                            quantity=0,
                            status=1,#pending
                            driver=None,
                            hash=random.randint(1000, 10000000)
                        )
                        tm.save()
            logger.info("Day %s done" % str(today))
        logger.info("done")