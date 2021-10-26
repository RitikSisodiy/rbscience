from django.shortcuts import render
from .models import TeamModel
# Create your views here.
def team(request,slug=None):
    res = {}
    res['membername'] = 'Our Team'
    if slug is None:  
        res['teammember'] = TeamModel.objects.all()
        return render(request,'team/teamlist.html',res)
    res['memberdetail'] = TeamModel.objects.get(slug = slug)
    res['membername'] = 'Samantha Wood'
    return render(request,'team/team.html',res)
