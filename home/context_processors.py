from services.models import *
from blogs.models import *
from services.views import training
def regfunc(request):
    serv = services.objects.filter(type='service')
    training = services.objects.filter(type='training')
    res= {
       'serv':serv,
    }
    res['blogs'] = Blogs.objects.all().order_by('date')
    res['training'] =training
    return res