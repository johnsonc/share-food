from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import VisitPoint
from .forms import ChooseDateAndDriver

def driver_shedule(request, routing_id=None):
    return render_to_response('admin/matcher/driver_schedule', {},  context_instance=RequestContext(request))


@login_required()
def confirm_visit_point(request, visit_point):
    vp = get_object_or_404(VisitPoint, pk=visit_point)
    vp.status = 'c'
    vp.save()
    return HttpResponseRedirect(reverse('admin:matcher_visitpoint_changelist'))


def match_on(request):
    if request.method == 'POST':
        form = ChooseDateAndDriver(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            TODO!!!!
            return HttpResponseRedirect('/thanks/')
    else:
        form = ChooseDateAndDriver()

    return render(request, 'name.html', {'form': form})


def match_on_date(request, year=None, month=None, day=None):
    pass