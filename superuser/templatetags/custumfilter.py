from django import template
from superuser.dashboardsettings import appslist,appmodels
register = template.Library()
@register.filter(name='sidebardata')
def sidebardata(value):
    return appmodels(appslist)

@register.filter(name='getattribute')
def getattribute(value,arg):
    try:    
        return getattr(value , arg)
    except Exception as e:
        return "-"