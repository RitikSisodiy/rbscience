from django.shortcuts import render
from .models import *

# Create your views here.

def servic(request,slug1):
    servall = services.objects.all()
    servsingle = services.objects.get(slug=slug1)
    res={}
    res['servall'] = servall
    res['servsingle'] = servsingle
    return render(request,'services/services.html',res)
