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
	print temp_path
	myfile = os.fdopen(fd, "w")
	myfile.write(serialized_queryset)
	ts = time.time()
	myfile.write("timestamp: " + str(ts))
	myfile.close()

	fd_return, temp_path_return = mkstemp()
	subprocess.call(["/home/ubuntu/signdb.sh", temp_path, temp_path_return])
	return open(temp_path_return).read()
