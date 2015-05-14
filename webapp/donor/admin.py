from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import OfferRepetition, Offer


class RepetitionInline(admin.StackedInline):
    model = OfferRepetition
    verbose_name_plural = _('Repetitions')


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    inlines = [
        RepetitionInline
        ]
