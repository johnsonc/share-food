__author__ = 'darek'
from django.conf import settings
from django.db.models import signals
from django.utils.translation import ugettext_noop as _

if "pinax.notifications" in settings.INSTALLED_APPS:
    from pinax.notifications.models import NoticeType

    def create_notice_types(app, created_models, verbosity, **kwargs):
        NoticeType.create("offer_send", _("New offer"), _("you have received a new offer"))
        NoticeType.create("offer_notified", _("We are shipping food for you"), _("we would like to confirm your offer request"))
        NoticeType.create("offer_canceled", _("Your transaction has been canceled"), _("we've canceled your transaction, contact our support for more details."))

    signals.post_syncdb.connect(create_notice_types, sender=NoticeType)
else:
    print "Skipping creation of NoticeTypes as notification app not found"
