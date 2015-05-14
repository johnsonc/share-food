from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Beneficiary, DeliveryTimeWindows, BeneficiaryGroup


class DeliveriesInline(admin.StackedInline):
    model = DeliveryTimeWindows
    verbose_name_plural = _('Deliveries')


@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('num_meals', 'frozen_capacity', 'refrigerated_capacity', 'drystorage_capacity',
                        'food_category', 'dont_accept', 'accept_meat_issue', 'accept_rel_issue',
                        'preference_info')
        }),
        ('Organization options', {
            'classes': ('collapse',),
            'fields': ('name', 'address', 'first_name', 'last_name', 'tel_1', 'tel_2',
                       'email', 'default_mass_unit', 'location')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('group', 'last_delivery')
        })

    )
    inlines = [
        DeliveriesInline
        ]

admin.site.register(BeneficiaryGroup)
