from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import OfferRepetition, Offer, Donnor


class RepetitionInline(admin.StackedInline):
    model = OfferRepetition
    verbose_name_plural = _('Repetitions')


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'beneficiary_group', 'food_category', 'estimated_mass', 'date', 'active')
    inlines = [
        RepetitionInline
        ]

    def active(self, obj):
        return True

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('donor') #here!
        return super(OfferAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.donor = request.user.profile.organization
        obj.save()

    def get_queryset(self, request):
        qs = super(OfferAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(donor=request.user)

@admin.register(Donnor)
class DonorAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'address',
        'first_name',
        'last_name',
        'tel_1',
        'tel_2',
        'email',
        'default_mass_unit',
        'default_beneficiary_group',
        'location',

    )
