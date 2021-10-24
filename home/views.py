from django.http import request
from django.shortcuts import render

from blogs.models import Blogs

# Create your views here.
def index(request):
    res = {}
    res['blogs'] = Blogs.objects.all()
    return render(request, 'index.html',res)