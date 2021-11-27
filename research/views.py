from django.shortcuts import redirect, render
from .models import researchModel
# Create your views here.
def getNextPrev(currentblog,all):
    res = {}
    current = all.filter(id__lt = currentblog.id).count()
    res['nextblog'] = all[current+1] if len(all)-1 > current else False
    res['prevblog'] = all[current-1] if current > 0 else False
    return res


def research(request,slug=None):
    res = {}
    res['headertitle'] = 'Our Research'
    res['allresearch'] = researchModel.objects.all()
    if slug is None: 
        res['title'] = "RESEARCH" 
        return render(request,'research/researchlist.html',res)
    res['research'] = researchModel.objects.get(slug = slug)
    res['title'] = res['research'].heading     
    res['relatedtpost'] = researchModel.objects.filter(category = res['research'].category.id).order_by("-time")
    res['headertitle'] = res['research'].heading
    res.update(getNextPrev(res['research'],res['allresearch']))
    return render(request,"research/research.html", res)
def category(request,slug=None):
    res = {}
    if slug is None:
        return redirect("research")
    res['allresearch'] = researchModel.objects.filter(category__slug=slug)
    res['headertitle'] = res['allresearch'][0].category
    res['title'] = res['allresearch'][0].category
    return render(request,'research/researchlist.html',res)