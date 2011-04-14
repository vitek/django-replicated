from django.http import HttpResponse

from replicated.decorators import use_master, use_slave
from testapp.models import Stat

# Create your views here.
def test_request(request):
    q = Stat.objects.all()
    return HttpResponse(content=q.db, content_type="text/plain")

@use_slave
def test_use_slave(request):
    q = Stat.objects.all()
    return HttpResponse(content=q.db, content_type="text/plain")

@use_master
def test_use_master(request):
    q = Stat.objects.all()
    return HttpResponse(content=q.db, content_type="text/plain")
