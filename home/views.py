import threading
from django.http import request
from django.shortcuts import redirect, render
from django.http.response import HttpResponse, JsonResponse
from blogs.models import Blogs
from team.models import TeamModel
from .models import abstratingAndIndexing, homeSlider
from research.models import researchModel
# Create your views here.
from django.contrib.auth import authenticate,login
def index(request):
    res = {}
    journal = request.session.get('jounral')
    typ = '2' if journal else '1'
    res['slider'] = homeSlider.objects.filter(type=typ)
    res['title'] = "RBscience : Home "
    res['teammember'] = TeamModel.objects.all()
    res['absindex'] = abstratingAndIndexing.objects.all().order_by('id')
    res['research'] = researchModel.objects.all()
    return render(request, 'index.html',res)
def changenav(request):
    request.session['jounral'] = True
    return redirect('home')
def rbsciencehome(request):
    request.session['jounral'] = False
    return redirect('home')
def logindashboard(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('dashboardindex')
    if request.method=="POST":
        print(request.POST,"this is working")
        username = request.POST.get('username')
        password = request.POST.get('password')
        USER = authenticate(request,username=username, password=password)
        if USER is not None:
            login(request, USER)
            if request.user.is_superuser:
                return JsonResponse({'status':'ok','msg':'Login Success','next':request.GET.get('next'),'type':'success'})
            return JsonResponse({"status":'invaliduser','msg':'invalid user','type':'danger'})
    return render(request,'logindashboard.html')