from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Driver, Routing, TemporalMatching, Matched, VisitPoint, Delivery

admin.site.register(Driver)
#admin.site.register(Routing)
admin.site.register(TemporalMatching)
admin.site.register(Matched)
#admin.site.register(VisitPoint)
#admin.site.register(Delivery)
