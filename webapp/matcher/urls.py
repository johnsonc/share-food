__author__ = 'darek'
from django.conf.urls import patterns, url

from .views import driver_shedule, confirm_visit_point, move_up, move_down, confirm_offer, matcher_panel

urlpatterns = patterns('',
    url(r'^matcher_panel/$', matcher_panel, name="matcher_panel"),
    url(r'^confirm_offer/(?P<offer_id>\d+)/(?P<hash>\d+)/?', confirm_offer, name="confirm_offer"),
    url(r'^schedule/(?P<routing_id>\d+)?/?$', driver_shedule, name="driver schedule"),
    url(r'^confirm_visit_point/(?P<visit_point>\d+)/?', confirm_visit_point, name="confirm_visit_point"),
    url(r'^move_up/(?P<visit_point>\d+)/?', move_up, name='move_up'),
    url(r'^move_down/(?P<visit_point>\d+)/?', move_down, name='move_down'),

)
