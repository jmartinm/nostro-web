from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms import ModelForm, TextInput, Select, Textarea

from .models import PointOfInterest


@csrf_protect
def get_pois(request):
    pois = PointOfInterest.objects.all()
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
    # formset = POIFormSet(queryset=PointOfInterest.objects.none())
    if request.method == 'POST':
        formset = POIFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return render_to_response("mapapp/manage_poi_success.html", {}, context_instance=RequestContext(request))

    else:
        formset = POIFormSet(queryset=PointOfInterest.objects.none())
    return render_to_response("mapapp/manage_poi.html", {
        "formset": formset}, context_instance=RequestContext(request))
