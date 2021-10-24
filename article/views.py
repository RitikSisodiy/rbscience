from django.shortcuts import redirect, render
from .forms import GenForm
from django.contrib import messages
from .models import issue, submenuscripts,artical,year
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
    yeardata = year.objects.filter()
    years  = issue.objects.values_list('year','vol').order_by("year__year").distinct()
    yearsvol = {d[0] : [] for d in years}
    for data in years:
        yearsvol[data[0]].append(data[1])
    reslist = []
    for k,v in yearsvol.items():
        liap = []
        for d in v:
            articaldata = artical.objects.filter(issue__year = k , issue__vol = d)
            if len(articaldata)>0:
                liap.append(articaldata)
        if len(liap)>0:
                reslist.append(liap)
    res['yearsbydata'] = reslist
    return render(request,'article/archives.html', res)
def articallist(request , year , vol ,issue):
    print(year,vol,issue)
    res = {}
    res['artical'] = artical.objects.filter(issue=issue , issue__year__year = year , issue__vol = vol)
    print(res['artical'])
    return render(request , "article/articallist.html" , res)
def singleartical(request,slug):
    res = {}
    return render(request, 'article/singleartical.html' , res)