from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db.models import signals
from django.utils.translation import ugettext_noop as _


def create_notices():
    if "pinax.notifications" in settings.INSTALLED_APPS:
        from pinax.notifications.models import NoticeType
        NoticeType.objects.get_or_create(label="offer_to_beneficiary", display=_("New food offer"), description=_("we've found a good match for you"), default=100)
        NoticeType.objects.get_or_create(label="transaction_notify",  display=_("New food transaction"), description=_("deal! Check details"), default=100)
        NoticeType.objects.get_or_create(label="transaction_canceled",  display=_("Transaction has been canceled"), description=_("transaction has been canceled by one of the parties"), default=100)
        NoticeType.objects.get_or_create(label="transaction_timeout",  display=_("Transaction has expired"), description=_("transaction has been canceled by one of the parties"), default=0)
        NoticeType.objects.get_or_create(label="offer_toolate",  display=_("Food donation offer has already expired"), description=_("Food donation offer has already expired"), default=0)
    else:
        print "Skipping creation of NoticeTypes as notification app not found"


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        create_notices()
