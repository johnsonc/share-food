from django.conf.urls import patterns, include, url
from django.contrib.gis import admin
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from api.view_sets import router

urlpatterns = patterns('',

    url(r'^admin/matcher_panel/$', 'matcher.views.matcher_panel'),                   
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^/?$', RedirectView.as_view(url='/admin/', permanent=True), name='index'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
