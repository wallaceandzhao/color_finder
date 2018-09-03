from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context

from . import models
# Create your views here.

def void(request):
    return HttpResponse('home')
def show(request):
    list = models.color.objects.all()
    c = {"list":list}
    return render_to_response('all.html',c)
def try_upload(request):
    return render_to_response('try-upload.html')