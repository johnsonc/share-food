__author__ = 'darek'
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.conf import settings

if "pinax.notifications" in settings.INSTALLED_APPS:
    from pinax.notifications import models as notifications
else:
    notifications = None

from beneficiary.models import Beneficiary

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        people = User.objects.filter(is_superuser=True)
        print [p.email for p in people]
        if notifications:
            print 'notification ok'
            beny = Beneficiary.objects.all()[0]
            print notifications.send_now(people, "offer_to_beneficiary", {'beneficiary': beny})
