from datetime import datetime, time
from django.contrib import admin
from panel.admin import site
from django.core import urlresolvers
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from donor.models import Offer
from .models import Driver, Routing, TemporalMatching, Matched, VisitPoint
from django.db.models import Q


class MatchAdmin(admin.ModelAdmin):

    model = Matched

    change_form_template = 'admin/matcher/match_details.html'

    list_display = ('date', 'offer', 'beneficiary', 'driver', 'quantity', 'beneficiary_contact_person')

    readonly_fields = ('date', 'driver', 'quantity', 'beneficiary_contact_person')

    exclude = ('offer', 'beneficiary',)

    actions = []

    def get_queryset(self, request):
        qs = super(MatchAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(Q(offer__donor=request.user) |
                         Q(beneficiary__user=request.user) |
                         Q(driver__user=request.user))


class VisitPointsByDriver(admin.SimpleListFilter):
    title = _('driver')
    parameter_name = 'driver'
    template = 'matcher/filter_driver.html'

    def lookups(self, request, model_admin):
        drivers = Driver.objects.all().order_by('user__username')
        return ((a.id, a.user.username) for a in drivers)

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(routing__driver=self.value())


class VisitPointByDate(admin.SimpleListFilter):
    title = _('date')
    parameter_name = 'date'
    template = 'matcher/filter_date.html'

    def lookups(self, request, model_admin):
        from datetime import date
        dates = set()
        routings = Routing.objects.all().order_by('-date')[:100]

        [dates.add(r) for r in routings]

        return ((d, d) for d in dates)

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(routing__date=self.value())

class VisitPointByDateFrom(admin.SimpleListFilter):
    title = _('date from')
    parameter_name = 'date_from'
    template = 'matcher/filter_date.html'

    def lookups(self, request, model_admin):
        from datetime import date
        dates = set()
        routings = Routing.objects.all().order_by('-date')

        [dates.add(r) for r in routings]

        return ((d, d) for d in dates)

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(routing__date__gte=self.value())

class VisitPointByDateTo(admin.SimpleListFilter):
    title = _('date to')
    parameter_name = 'date_to'
    template = 'matcher/filter_date.html'

    def lookups(self, request, model_admin):
        from datetime import date
        dates = set()
        routings = Routing.objects.all().order_by('-date')

        [dates.add(r) for r in routings]

        return ((d, d) for d in dates)

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(routing__date__lte=self.value())


class VisitPointAdmin(admin.ModelAdmin):

    model = VisitPoint

    list_display = ('seq_num', 'name', 'address', 'driver', 'status',
                    'date', 'time', 'details_link', 'confirm', 'up', 'down')

    list_filter = (VisitPointsByDriver, VisitPointByDate, VisitPointByDateFrom, VisitPointByDateTo)

    list_display_links = None

    fields = ('status', 'donor', 'seq_num', 'matched')

    verbose_name = _('Route points')

    def name(self, instance):
        if instance.donor:
            return instance.matched.offer.name
        else:
            return instance.matched.beneficiary.user.organization.name

    def address(self, instance):
        if instance.donor:
            return instance.matched.offer.address
        else:
            return instance.matched.beneficiary.user.organization.address

    def driver(self, instance):
        if instance.routing:
            return instance.routing.driver
        else:
            return _('Not set')

    def date(self, instance):
        if instance.routing:
            return instance.routing.date
        else:
            return _('routing not set, ask administrator')

    def time(self, instance):
        if instance.donor:
            return '%s - %s ' % (datetime.strftime(instance.matched.offer.time_from, "%H:%M"),
                                 datetime.strftime(instance.matched.offer.time_to, "%H:%M"))
        else:
            timewindows = ''
            for tw in instance.matched.beneficiary.get_timewindows():
                timewindows += '%s %s - %s; ' % (str(tw.day_of_week),
                                                 time.strftime(tw.time_from, "%H:%M"),
                                                 time.strftime(tw.time_to, "%H:%M"))

            return timewindows

    def details_link(self, instance):
        print self
        print instance
        #print //window.location.href=location.protocol + '//' + location.host + location.pathname; else window.location.href=location.protocol + '//' + location.host + location.pathname+this.value;
        return mark_safe('<a href="%s">%s</a>' % (urlresolvers.reverse('admin:matcher_matched_change',
                                                                       args=(instance.matched.id,)),
                                                                        _('Details')))
    def confirm(self, instance):
        return mark_safe('<a href="%s">%s</a>' % (urlresolvers.reverse('confirm_visit_point', args=(instance.id,)),
                                                                        _('Confirm')))

    def up(self, instance):

        return mark_safe('<a href="%s">%s</a>' % (urlresolvers.reverse('move_up', args=(instance.id,)),
                                                                        _('Up')))
    def down(self, instance):
        return mark_safe('<a href="%s?%s">%s</a>' % (urlresolvers.reverse('move_down', args=(instance.id, )),
                                                  self.param.urlencode(), _('Down')))
    def get_actions(self, request):
        actions = super(VisitPointAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']

    def changelist_view(self, request, extra_context=None):
        self.param = request.GET

        return super(VisitPointAdmin, self).changelist_view(request, extra_context=extra_context)

class VisitPointInline(admin.TabularInline):
    model = VisitPoint

    fields = ('matched', 'donor', 'seq_num' )

    readonly_fields = ('matched', )


class RoutingAdmin(admin.ModelAdmin):
    model = Routing

    list_display = ('date', 'driver', 'get_visit_points_link', )

    list_filter = ('date',)

    fields = ('date', )

    exclude = ('driver', )

    inlines = [VisitPointInline]


    def get_queryset(self, request):
        qs = super(RoutingAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(driver__user=request.user)

    def get_visit_points_link(self, instance):
        return mark_safe('<a href="%s">%s</a>' % (urlresolvers.reverse('admin:matcher_visitpoint_changelist'),
                                            _('Show route')))


site.register(Driver)
site.register(TemporalMatching)
site.register(VisitPoint, VisitPointAdmin)

site.register(Matched, MatchAdmin)
site.register(Routing, RoutingAdmin)

