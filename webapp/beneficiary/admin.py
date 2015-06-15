from django.contrib import admin
from panel.admin import site
from django.utils.translation import ugettext as _
from django.core import urlresolvers
from .models import Beneficiary, DeliveryTimeWindows, BeneficiaryGroup
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


class DeliveriesInline(admin.StackedInline):
    model = DeliveryTimeWindows
    max_num = 7
    verbose_name_plural = _('Deliveries')



#@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Basic info'), {
            'fields': ('num_meals', 'group', 'food_category', 'dont_accept', 'accept_meat_issue', 'accept_rel_issue', 'preference_info')
        }),
        (_('Storage capacity'), {
            'fields': ('frozen_capacity', 'refrigerated_capacity', 'drystorage_capacity',)
        }),
        (_('Preferences'), {
            'fields': ('food_category', 'dont_accept', 'accept_meat_issue', 'accept_rel_issue', 'preference_info')
        }),
    )

    readonly_fields = ('group',)
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

    def response_add(self, request, obj, post_url_continue="../%s/"):
        super(BeneficiaryAdmin, self).response_add(request, obj, post_url_continue)

        return HttpResponseRedirect(urlresolvers.reverse('admin:app_index'))

    def response_change(self, request, obj):
        super(BeneficiaryAdmin, self).response_change(request, obj)
        return HttpResponseRedirect(urlresolvers.reverse('admin:index'))

    def get_queryset(self, request):
        qs = super(BeneficiaryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

site.register(BeneficiaryGroup)
site.register(Beneficiary, BeneficiaryAdmin)


