__author__ = 'darek'
from django.conf.urls import patterns, url

from .views import driver_shedule, confirm_visit_point, match_on_date

urlpatterns = patterns('',
    url(r'^schedule/(?P<routing_id>\d+)?/?$', driver_shedule, name="driver schedule"),
    url(r'^confirm_visit_point/(?P<visit_point>\d+)/?', confirm_visit_point, name="confirm_visit_point"),
    # matching page
    url(r'^match_on', match_on, name="match_on"),
    url(r'^match/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/',
                match_on_date, name="match"),
)
