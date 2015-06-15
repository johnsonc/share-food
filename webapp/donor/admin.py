from django.contrib import admin
from panel.admin import site
from django.utils.translation import ugettext as _

from .models import OfferRepetition, Offer#, Donnor


class RepetitionInline(admin.StackedInline):
    model = OfferRepetition
    verbose_name_plural = _('Repetitions')
    max_num = 1


class OfferAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General', {
            'fields': ('name', ('food_category', 'estimated_mass',), 'contact_person')
        }),
        ('Beneficiary groups', {
            'fields': ('beneficiary_group',),
        }),
        ('Food type', {
            'fields': (('meat_issue', 'rel_issue',),
                       ('temperature', 'packaging', ),)
        }),
        ('Food ingredients', {
            'fields': ('not_contain',)
        }),
        ('Driver info', {
            'fields': (('address', 'driver_info',),)
        }),
        ('Time info', {
            'fields': (('time_from', 'time_to',),)
        }),
        ]

    inlines = [
        RepetitionInline
        ]

    list_display = ('name', 'estimated_mass', 'temperature', 'time_from', 'time_to', 'packaging')

    #list_filter = ('food_category', 'temperature', 'packaging')

    def active(self, obj):
        return True

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('donor') #here!
            if self.fieldsets[0][0] == 'Donor':
                self.fieldsets = self.fieldsets[1:]
        else:
            if self.fieldsets[0][0] == 'General':
                self.fieldsets.insert(0, ('Donor', {'fields': ('donor',)}))

        return super(OfferAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.donor = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(OfferAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(donor=request.user)

site.register(Offer, OfferAdmin)

"""
@admin.register(Donnor)
class DonorAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'address',)
        }),
        ('Contact person', {
            'fields': ('first_name', 'last_name', 'email',),
        }),
        ('Telephone numbers', {
            'fields': ('tel_1', 'tel_2',)
        }),
        ('Others', {
            'fields': ('default_mass_unit', 'default_beneficiary_group', 'location',)
        })
        )
"""