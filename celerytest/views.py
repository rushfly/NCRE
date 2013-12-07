from django.shortcuts import render
from django.http import HttpResponse
from celerytest.tasks import *

# Create your views here.


def test(request):
    writefile.delay()
    return HttpResponse()
