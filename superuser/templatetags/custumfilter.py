from django import template
from superuser.dashboardsettings import appslist,appmodels,getTitle
register = template.Library()
@register.filter(name='sidebardata')
def sidebardata(value):
    return appmodels(appslist)
@register.filter(name='cemelcase')
def cemelcase(value):
    res = ''
    count = 0
    for s in str(value):
        if count != 0 and s == s.upper():
            s = " "+s
        res+=s
        count+=1
    return res
@register.filter(name='getattribute')
def getattribute(value,arg):
    try:    
        data = getattr(value , arg)
        if len(str(data))>0:
            return data
        else:
            return "-"
    except Exception as e:
        return "-"
@register.filter(name='split')
def splitdata(value,args):
    return value.split(args)
@register.filter(name="getpercent")
def getpercent(value,arg):
    value = float(value)
    arg = float(arg)
    percent = (arg*100)/value
    return str(percent)[:5]
@register.filter(name="showrelated")
def showrelated(value,args):
    return "showing related"
@register.filter(name="getTitle")
def showrelated(value):
    if len(getTitle)>0:
        return getTitle
    else:
        return "Admin"