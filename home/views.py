import threading
from django.http import request
from django.shortcuts import redirect, render

from blogs.models import Blogs
from team.models import TeamModel
from .models import homeSlider
from research.models import researchModel
# Create your views here.

def index(request):
    res = {}
    journal = request.session.get('jounral')
    typ = '2' if journal else '1'
    res['slider'] = homeSlider.objects.filter(type=typ)
    res['title'] = "RBscience : Home "
    res['teammember'] = TeamModel.objects.all()

    res['research'] = researchModel.objects.all()
    return render(request, 'index.html',res)
def changenav(request):
    request.session['jounral'] = True
    return redirect('home')
def rbsciencehome(request):
    request.session['jounral'] = False
    return redirect('home')