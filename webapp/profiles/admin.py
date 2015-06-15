from django.contrib.gis import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext as _
from django.conf import settings
from .models import Profile, Organization
from donor.models import Donor
from beneficiary.models import Beneficiary
from panel.admin import site
from django.http import HttpResponseRedirect
from django.core import urlresolvers

class ProfileInline(admin.StackedInline):
    model = Profile
    verbose_name_plural = _('Profiles')
    exclude = ('location',)


class DonorProfileInline(admin.StackedInline):
    model = Donor
    verbose_name = _('Donor profile')


class BeneficiaryProfileInline(admin.StackedInline):
    model = Beneficiary
    exclude = ('last_delivery',)
    verbose_name = _('Beneficiary profile')


class UserWithProfileAdmin(UserAdmin):
    inlines = (ProfileInline, DonorProfileInline, BeneficiaryProfileInline)


class ProfileForUser(admin.ModelAdmin):
    model = Profile

    exclude = ('user',)

    def response_add(self, request, obj, post_url_continue="../%s/"):
        super(ProfileForUser, self).response_add(request, obj, post_url_continue)

        return HttpResponseRedirect(urlresolvers.reverse('admin:app_index'))

    def response_change(self, request, obj):
        super(ProfileForUser, self).response_change(request, obj)
        return HttpResponseRedirect(urlresolvers.reverse('admin:index'))

    def get_queryset(self, request):
        qs = super(ProfileForUser, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

#site.unregister(User)
site.register(User, UserWithProfileAdmin)
site.register(Group)
site.register(Organization, admin.OSMGeoAdmin)
site.register(Profile, ProfileForUser)