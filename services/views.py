from django.shortcuts import render
from .models import *

# Create your views here.

def servic(request,slug1):
    servall = services.objects.filter(type='service')
    servsingle = services.objects.get(slug=slug1)
    res={}
    res['title'] = servsingle.title
    res['servall'] = servall
    res['servsingle'] = servsingle
    res['headertitle'] = servsingle.title
    return render(request,'services/services.html',res)
def training(request,slug):
    servall = services.objects.filter(type='training')
    servsingle = services.objects.get(slug=slug)
    res={}
    res['title'] = servsingle.title
    res['servall'] = servall
    res['servsingle'] = servsingle
    res['headertitle'] = servsingle.title
    return render(request,'services/training.html',res)
