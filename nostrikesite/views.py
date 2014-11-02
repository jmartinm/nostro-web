from django.shortcuts import render
from mapapp.models import PointOfInterest
from django.core import serializers


# Create your views here.
def home(request):
    return render(request, "index.html")


def export(request):
	from tempfile import mkstemp
	import os
	import time
	import subprocess

	pois = PointOfInterest.objects.all()
	serialized_queryset = serializers.serialize('json', pois)
	fd, temp_path = mkstemp()
	myfile = os.fdopen(fd, "w")
	myfile.write(serialized_queryset)
	ts = time.time()
	myfile.write("timestamp: " + str(ts))
	myfile.close()

	fd_return, temp_path_return = mkstemp(dir="/tmp")
	x = subprocess.call(["/home/ubuntu/signdb.sh", temp_path, temp_path_return])
	response = HttpResponse(open(temp_path_return).read(), content_type="text/plain")
	response['Content-Disposition'] = 'attachment; filename=export.txt'
	return response
