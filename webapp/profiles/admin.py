from django.contrib.gis import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from .models import Profile, Organization, Dictionary


class ProfileInline(admin.StackedInline):
    model = Profile
    verbose_name_plural = _('Profiles')


class UserWithProfileAdmin(UserAdmin):
    inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserWithProfileAdmin)

admin.site.register(Organization, admin.OSMGeoAdmin)
admin.site.register(Dictionary)