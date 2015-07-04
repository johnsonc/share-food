from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.utils import timezone
from django import forms
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from .models import VisitPoint, TemporalMatching

if "pinax.notifications" in settings.INSTALLED_APPS:
    from pinax.notifications import models as notification
else:
    notification = None

@staff_member_required
def matcher_panel(request):
    return render_to_response('matcher/matcher_panel.html',
                              context_instance=RequestContext(request))


@login_required()
def driver_shedule(request, routing_id=None):
    """
    TODO: throw this away, it looks like unused
    :param request:
    :param routing_id:
    :return:
    """
    return render_to_response('admin/matcher/driver_schedule', {},  context_instance=RequestContext(request))


class MatchConfirm(forms.Form):

    MATCH_REJECT = 0
    MATCH_100 = 1
    MATCH_50 = 2

    MATCH_TYPES = (
        (MATCH_100, _('Confirming the offer')),
        (MATCH_50, _('Confirming 50%')),
        (MATCH_REJECT, _('Rejecting the offer'))
    )

    confirm = forms.IntegerField(widget=forms.RadioSelect(choices=MATCH_TYPES))
    hash = forms.IntegerField(widget=forms.HiddenInput())
    offer_id = forms.IntegerField(widget=forms.HiddenInput())


def confirm_offer(request, offer_id, secret):
    match = get_object_or_404(TemporalMatching,
                              id=offer_id,
                              hash=secret,
                              status=TemporalMatching.STATUS_WAITING)

    if request.method == 'POST':
        form = MatchConfirm(request.POST)
        if form.is_valid():

            if form.cleaned_data['confirm'] == MatchConfirm.MATCH_REJECT:
                match.status = TemporalMatching.STATUS_EXPIRED
                from .matcher import cancel_temporal_match
                cancel_temporal_match(match)

            if form.cleaned_data['confirm'] == MatchConfirm.MATCH_100:
                match.quantity = match.offer.estimated_mass
                match.status = TemporalMatching.STATUS_CONFIRMED

            if form.cleaned_data['confirm'] == MatchConfirm.MATCH_50:
                match.quantity = match.offer.estimated_mass / 2
                match.status = TemporalMatching.STATUS_CONFIRMED

            match.save()
            if notification:
                notification.send([match.beneficiary.user],
                                  "offer_confirmation_thank_you",
                                  {})

            return render_to_response('admin/matcher/confirm_offer_thank_you.html',
                                      {'match': match},
                                      context_instance=RequestContext(request))
    else:

        form = MatchConfirm(initial={'offer_id': offer_id, 'hash': secret})

    return render_to_response('admin/matcher/confirm_offer.html',
                              {'form': form,
                               'offer_id': offer_id,
                               'match': match,
                               'hash': secret},
                               context_instance=RequestContext(request))


@login_required()
def confirm_visit_point(request, visit_point):
    vp = get_object_or_404(VisitPoint, pk=visit_point)
    vp.status = 'c'
    vp.confirmed = timezone.now()
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

