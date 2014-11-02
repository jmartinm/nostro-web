from django.shortcuts import render
from mapapp.models import PointOfInterest
from django.core import serializers
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "index.html")


def export(request):
	from tempfile import mkstemp
	import os
	import time
	import subprocess
	import datetime

	pois = PointOfInterest.objects.all()
	serialized_queryset = serializers.serialize('json', pois)
	fd, temp_path = mkstemp()
	myfile = os.fdopen(fd, "w")
	myfile.write(serialized_queryset)
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	myfile.write("\n\ntimestamp: " + str(st) + '\n\n')
	myfile.close()

	fd_return, temp_path_return = mkstemp(dir="/tmp")
	x = subprocess.call(["/home/ubuntu/signdb.sh", temp_path, temp_path_return])
	response = HttpResponse(open(temp_path_return).read(), content_type="text/plain")
	response['Content-Disposition'] = 'attachment; filename=export.txt'
	return response
