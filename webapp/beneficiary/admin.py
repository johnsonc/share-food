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

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('user')
        return super(BeneficiaryAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.user = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(BeneficiaryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
admin.site.register(BeneficiaryGroup)
