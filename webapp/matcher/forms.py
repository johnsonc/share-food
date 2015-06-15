__author__ = 'darek'
from django.utils.translation import ugettext as _
from datetime import date
from django import forms

from matcher.models import Driver

class ChooseDateAndDriver(forms.Form):
    date = forms.DateField(label=_('Choose date for matching'), default=date.today())
    driver = forms.Select(queryset=Driver.objects.all())