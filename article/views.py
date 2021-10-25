from django.shortcuts import redirect, render
from .forms import GenForm
from django.contrib import messages
from .models import submenuscripts,artical,year
# Create your views here.
def article(request):
    res = {}
    return render(request , "article/journals.html" , res)
def submitarticle(request):
    res = {}
    if request.method == "POST":
        form = GenForm(submenuscripts)
        form = form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request , "Your Submission is Successfull")
            return redirect(request.get_full_path())
        else:
            messages.error(request,'Invalid From Submission Check The Form Deatails')
    return render(request , 'article/submitartical.html', res)
def archives(request):
    res = {}
    res['yearsbydata']  = year.objects.all() 
    return render(request,'article/archives.html', res)