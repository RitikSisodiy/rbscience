from django.shortcuts import redirect, render
from .models import researchModel
# Create your views here.
def research(request,slug=None):
    res = {}
    res = {}
    res['headertitle'] = 'Our Research'
    if slug is None:  
        res['allresearch'] = researchModel.objects.all()
        return render(request,'research/researchlist.html',res)
    res['research'] = researchModel.objects.get(slug = slug)
    res['relatedtpost'] = researchModel.objects.filter(category = res['research'].category.id).order_by("-time")
    res['headertitle'] = res['research'].heading

    return render(request,"research/research.html", res)
def category(request,slug=None):
    res = {}
    if slug is None:
        return redirect("research")
    res['allresearch'] = researchModel.objects.filter(category__slug=slug)
    res['headertitle'] = res['allresearch'][0].category
    return render(request,'research/researchlist.html',res)