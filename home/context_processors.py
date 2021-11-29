from services.models import *
from blogs.models import *
from artical.models import artical
from superuser.models import aboutContact
from services.views import training
def regfunc(request):
    serv = services.objects.filter(type='service')
    training = services.objects.filter(type='training')
    res= {
       'serv':serv,
    }
    res['blogs'] = Blogs.objects.all().order_by('date')
    res['training'] =training
    res['latestartical'] = artical.objects.all().order_by('-time')[0]
    abtc = aboutContact.objects.all()
    res['aboutcontact'] = abtc[0] if abtc.exists() else []
    return res