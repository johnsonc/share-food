from django.contrib.gis.admin import AdminSite
from django.utils.translation import ugettext as _


class MainAdminSite(AdminSite):
    index_template = 'admin/panel/index.html'
    index_title = _('Dashboard')

site = MainAdminSite(name='admin')
