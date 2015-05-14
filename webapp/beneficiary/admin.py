from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Beneficiary, DeliveryTimeWindows


class DeliveriesInline(admin.StackedInline):
    model = DeliveryTimeWindows
    verbose_name_plural = _('Deliveries')


@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    inlines = [
        DeliveriesInline
        ]
