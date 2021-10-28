import threading
from django.http import request
from django.shortcuts import render

from blogs.models import Blogs
from team.models import TeamModel
from research.models import researchModel
# Create your views here.

def index(request):
    res = {}
    res['teammember'] = TeamModel.objects.all()
    res['research'] = researchModel.objects.all()
    return render(request, 'index.html',res)
