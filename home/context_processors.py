from services.models import *
from blogs.models import *
def regfunc(request):
    serv = services.objects.all()
    res= {
       'serv':serv,
    }
    res['blogs'] = Blogs.objects.all().order_by('date')
    return res