__author__ = 'darek'
from django.utils.translation import ugettext as _
from datetime import date
from django import forms

from matcher.models import Driver

class ChooseDateAndDriver(forms.Form):
    date = forms.DateField(_('Choose date for matching'), initial=date.today())
    driver = forms.Select(choices=Driver.objects.all())