from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Beneficiary, DeliveryTimeWindows, BeneficiaryGroup


class DeliveriesInline(admin.StackedInline):
    model = DeliveryTimeWindows
    max_num = 1
    verbose_name_plural = _('Deliveries')


@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Basic info'), {
            'classes': ('collapse',),
            'fields': ('num_meals', 'food_category', 'dont_accept', 'accept_meat_issue', 'accept_rel_issue', 'preference_info')
        }),
        (_('Storage capacity'), {
#            'classes': ('collapse',),
            'fields': ('frozen_capacity', 'refrigerated_capacity', 'drystorage_capacity',)
        }),

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
