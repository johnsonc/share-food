from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response
from django.template import RequestContext

@staff_member_required
def matcher_panel(request):
    print 'matcher_panel exist'
    return render_to_response('matcher/matcher_panel.html',
        context_instance=RequestContext(request))



from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import VisitPoint
from .forms import ChooseDateAndDriver
from django.utils.http import urlencode



def driver_shedule(request, routing_id=None):
    return render_to_response('admin/matcher/driver_schedule', {},  context_instance=RequestContext(request))


@login_required()
def confirm_visit_point(request, visit_point):
    vp = get_object_or_404(VisitPoint, pk=visit_point)
    vp.status = 'c'
    vp.save()
    return HttpResponseRedirect('%s?%s' % (reverse('admin:matcher_visitpoint_changelist'),
                                           request.GET.urlencode()))

@login_required()
def move_up(request, visit_point):
    vp = get_object_or_404(VisitPoint, pk=visit_point)
    visit_points = [v for v in vp.routing.visitpoints.all()]

    for x in range(len(visit_points)):
        if visit_points[x] == vp and x > 0:
            visit_points[x] = visit_points[x-1]
            visit_points[x-1] = vp

    for x in range(len(visit_points)):
        visit_points[x].seq_num = x
        visit_points[x].save()

    return HttpResponseRedirect(u'%s?%s' % (reverse('admin:matcher_visitpoint_changelist'),
                                                    request.GET.urlencode()))

@login_required()
def move_down(request, visit_point):
    vp = get_object_or_404(VisitPoint, pk=visit_point)
    visit_points = [v for v in vp.routing.visitpoints.all()]
    for x in range(1, len(visit_points)):
        if visit_points[x-1] == vp:
            visit_points[x-1] = visit_points[x]
            visit_points[x] = vp

    for x in range(len(visit_points)):
        visit_points[x].seq_num = x
        visit_points[x].save()
    return HttpResponseRedirect('%s?%s' % (reverse('admin:matcher_visitpoint_changelist'),
                                            request.GET.urlencode()))


def match_on(request):
    if request.method == 'POST':
        form = ChooseDateAndDriver(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #TODO!!!!
            return HttpResponseRedirect('/thanks/')
    else:
        form = ChooseDateAndDriver()

    return render(request, 'name.html', {'form': form})


def match_on_date(request, year=None, month=None, day=None):
    pass
