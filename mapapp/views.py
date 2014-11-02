from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.forms import ModelForm, TextInput, Select, Textarea

from .models import PointOfInterest


@csrf_protect
def get_pois(request):
    verified_map = {
        'verified': True,
        'non verified': False,
        'both': ""
    }
    query = {}
    if "verified" in request.POST:
        if request.POST["verified"] != "both":
            query["verified"] = verified_map[request.POST["verified"]]
    if "type" in request.POST:
        if request.POST["type"] != "All":
            query["type"] = request.POST["type"]

    pois = PointOfInterest.objects.all().filter(**query)

    serialized_queryset = serializers.serialize('json', pois)
    return HttpResponse(serialized_queryset, content_type="application/json")


class POIForm(ModelForm):
    class Meta:
        model = PointOfInterest
        fields = ['name', 'type', 'website', 'contact', 'comments', 'position']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'type': Select(attrs={'class': 'form-control'}),
            'website': TextInput(attrs={'class': 'form-control'}),
            'contact': TextInput(attrs={'class': 'form-control'}),
            'comments': Textarea(attrs={'class': 'form-control'}),
        }


@login_required
@require_http_methods(["GET", "POST"])
def add(request):
    from django.forms.models import modelformset_factory
    POIFormSet = modelformset_factory(PointOfInterest, form=POIForm)
    # import ipdb; ipdb.set_trace()
    # formset = POIFormSet(queryset=PointOfInterest.objects.none())
    if request.method == 'POST':
        formset = POIFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return redirect("home")
            # {}, context_instance=RequestContext(request))

    else:
        formset = POIFormSet(queryset=PointOfInterest.objects.none())

    ctx = {}
    if request.is_secure() and request.SSL_CLIENT_VERIFY == "SUCCESS":
        ctx['issuer_name'] = request.get("SSL_CLIENT_I_DN_CN")
        ctx['client_name'] = request.get("SSL_CLIENT_S_DN_CN")
        ctx['client_org'] = request.get("SSL_CLIENT_S_DN_O")

    ctx["formset"] = formset
    return render_to_response("mapapp/manage_poi.html", ctx,
                              context_instance=RequestContext(request))
