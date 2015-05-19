from django.contrib.gis import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.conf import settings
from .models import Profile, Organization
from donor.models import Donor
from beneficiary.models import Beneficiary


class ProfileInline(admin.StackedInline):
    model = Profile
    verbose_name_plural = _('Profiles')
    exclude = ('location',)


class DonorProfileInline(admin.StackedInline):
    model = Donor
    verbose_name = _('Donor profile')


class BeneficiaryProfileInline(admin.StackedInline):
    model = Beneficiary
    verbose_name = _('Beneficiary profile')


class UserWithProfileAdmin(UserAdmin):
    inlines = (ProfileInline, DonorProfileInline, BeneficiaryProfileInline)


admin.site.unregister(User)
admin.site.register(User, UserWithProfileAdmin)

admin.site.register(Organization, admin.OSMGeoAdmin)