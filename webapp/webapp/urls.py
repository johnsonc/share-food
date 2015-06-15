from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
#from django.contrib.gis import admin
from panel.admin import site
from django.conf import settings

urlpatterns = patterns('',

    url(r'^admin/', include(site.urls), name="admin"),
    url(r'^m/', include('matcher.urls')),
    url(r'^/?$', RedirectView.as_view(url='/admin/', permanent=True), name='index'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
