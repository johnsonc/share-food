from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response
from django.template import RequestContext

@staff_member_required
def matcher_panel(request):
    print 'matcher_panel exist'
    return render_to_response('matcher/matcher_panel.html',
        context_instance=RequestContext(request))
