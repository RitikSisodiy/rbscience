from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    res = {}
    return render(request, 'index.html',res)