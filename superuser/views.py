# from django.http import request
# from django.http.response import HttpResponse
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .custumfunction import getobjecturl
from superuser.templatetags.custumfilter import sidebardata
from .dashboardsettings import appmodels , appslist , getObjectbyAppModelName , getmodelbyappname
from django.core import serializers
from artical.forms import GenForm
from django.contrib.auth import logout
# from django.apps import apps
# from onlineshop.models import *
# from django.contrib import messages
# from .forms import ProductForm,aboutForm,about,GenForm
# Create your views here.
#add all app names you want to oprate in admin
allapps = appslist
def get_all_fields(self):
    """Returns a list of all field names on the instance."""
    fields = []
    for f in self._meta.fields:

        fname = f.name        
        # resolve picklists/choices, with get_xyz_display() function
        get_choice = 'get_'+fname+'_display'
        if hasattr(self, get_choice):
            value = getattr(self, get_choice)()
        else:
            try:
                value = getattr(self, fname)
            except AttributeError:
                value = None

        # only display fields with values and skip some fields entirely
        if f.editable and value and f.name not in ('id', 'status', 'workshop', 'user', 'complete') :

            fields.append(
              {
               'label':f.verbose_name, 
               'name':f.name, 
               'value':value,
              }
            )
    return fields
def index(request):
    res = {}
    res['dashboardheading'] = 'Dashboard'
    # for data in res['modelslist']:
    #     print(res['modelslist'][data])
    #     break
    # for app in allapps:
    #     res.append({app:apps.all_models[app]})
    return render(request,'superuser/index.html',res)
def showmodels(request,appname):
    res = {}
    res['modelname'] ="Home"
    res['appname'] =appname
    res['models'] = getmodelbyappname(appname)
    return render(request,'superuser/listmodels.html',res)
def showObject(request,appname,modelname):
    res = {}
    mymodel = getObjectbyAppModelName(appname,modelname)
    res['modeldata'] = mymodel.objects.all()
    res['fields'] = [f.name for f in mymodel._meta.fields]
    # res['fields'] = [f.name for f in mymodel._meta.get_fields()]
    res['modeldata'] = mymodel.objects.all()
    res['appname'] =appname
    res['modelname'] =modelname
    return render(request , 'superuser/modeldatatable.html' ,res)
def editmodel(request,appname=None,modelname=None,objectid=None,opration=None):
    res = {}
    mymodel = getObjectbyAppModelName(appname,modelname)
    form = GenForm(mymodel,['slug'])
    res['appname'] =appname
    res['modelname'] =modelname
    if objectid is not None and objectid != "newmodel":
        singledata = mymodel.objects.get(pk=objectid)
    if opration == 'add':
        res['form'] = form()
        if request.method == "POST":
            res['form'] = form(request.POST,request.FILES)
            if res['form'].is_valid():
                res['form'].save()
                messages.success(request,str(res['form'].instance) + " is saved successfully")
                return redirect(request.get_full_path())
            messages.error(request,str(getobjecturl(res['form'].instance)) + " data is invalid Check your form")
    elif opration == 'edit':
        res['form'] = form(instance=singledata)
        res['relateddata'] = type(singledata)._meta.related_objects
        res['appname'] = appname
        res['modelname'] = modelname
        res['objectid'] = objectid
        if request.method == "POST":
            res['form'] = form(request.POST,request.FILES,instance=singledata)
            if res['form'].is_valid():
                res['form'].save()
                messages.success(request,str(getobjecturl(res['form'].instance))  + " is saved successfully")
                if request.GET.get('next') is not None:
                    return redirect(request.GET.get('next'))
                return redirect(request.get_full_path())
            messages.error(request,str(res['form'].instance) + " data is invalid Check your form")
            
    elif opration == 'delete':
        confirm = request.GET.get('confirm')
        return alertdelete(request,singledata,confirm)
    return render(request,'superuser/editmodel.html',res)

def relatedmodel(request,appname=None,modelname=None,objectid=None,relatedfield=None):
    res= {}
    mymodel = getObjectbyAppModelName(appname,modelname)
    singledata = mymodel.objects.get(pk=objectid)
    relatedfieldobject = getattr(singledata,relatedfield)
    res['availbledata'] = relatedfieldobject.all()
    relmodel = relatedfieldobject.model
    relatedfieldobjectFieldname = relatedfieldobject.field.name
    form = GenForm(relmodel,[relatedfieldobjectFieldname,'slug'])
    res['currentmodelname'] = relatedfieldobject.model._meta.verbose_name
    res['currentappname'] = relatedfieldobject.model._meta.app_label
    res['currentmodelfieldname'] = relatedfieldobject.model._meta.model_name
    if request.method == "POST":
        form = form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"new "+ res['currentmodelname'] + "is added in "+modelname +" Successfully"  )
            return redirect(request.get_full_path())
        else:
            messages.error(request,'Invalid data please cheack your form')
    if relmodel is not None:
        res['fields'] = [f.name for f in relmodel._meta.fields]
    res['appname'] = appname
    res['modelname'] = modelname
    res['objectid'] = objectid
    res['currentmodel'] = singledata
    res['currentmodelobjectid'] = singledata.pk
    res['form'] = form(initial={relatedfieldobjectFieldname: singledata.pk})
    return render(request,'superuser/relatedmodel.html',res)



from django.contrib.admin.utils import NestedObjects
def alertdelete(request,singledata,confirm="None"):
    appname = type(singledata)._meta.app_label
    modelname = singledata._meta.model_name
    if confirm == "delete":
        name = str(singledata)
        singledata.delete()
        messages.success(request,name + " is deleted successfully")
        return redirect('showdatamodel',appname=appname,modelname=modelname )
    res = {}
    using = 'default'
    nested_object = NestedObjects(using)
    nested_object.collect([singledata])
    res['deletedata'] = nested_object.nested()
    res['appname'] = appname
    res['modelname'] = modelname
    res['currentmodel'] = singledata
    return render(request , 'superuser/confirmdelete.html',res)
def Logout(request):
    try:
        logout(request)
    except Exception as e:
        return redirect('home')
    return redirect('home')
# def allproducts(request):
#     prods = Product.objects.all()
#     return render(request,'superuser/products.html',{'prods':prods,'title':"View Product"})
# def editproduct(request,id=None,task=None):
#     res = {}
#     if task == 'add':
#         res['form'] = ProductForm()
#         instan = None
#     if task == 'edit':
#         instan = Product.objects.get(id=id)
#         res['form'] = ProductForm(instance=instan)
#     if request.method == "POST":
#         res['form'] = ProductForm(request.POST,request.FILES,instance=instan)
#         if res['form'].is_valid():
#             res['form'].save()
#             messages.success(request,"Prouduct is added successfully :)")
#         return render(request,'superuser/addprod.html',res)
#     if task == 'del':
#         return delproduct(request,id)
#     return render(request,'superuser/addprod.html',res)


# def delproduct(request,id=None):
#     if id is not None:
#         Product.objects.get(id=id).delete()
#         return redirect('allproducts')

# def addspecs(request,id,update=False,remove = False):
#     prod = Product.objects.get(id=id)
#     specsob = specs.objects.filter(Product=prod.id)
#     if request.method == "POST":
#         title = request.POST['title']
#         oldtitle = request.POST.get('oldtitle')
#         key = request.POST.getlist('key')
#         value = request.POST.getlist('value')
#         data = {}
#         data[title] = [[key[i],value[i]] for i in range(0,len(key))]
#         if specsob.exists():                
#             specsobnew = specsob[0]
#             updata= specsobnew.jsondata()
#             if update == False:
#                 try:
#                     a = updata[title]
#                     print(a,updata)
#                     messages.error(request,title+" is already exist please change the title")
#                     return redirect('addspecs',id)
#                 except Exception as e:
#                     pass
#             updata[title] = data[title]
#             if oldtitle is not None and oldtitle != title:
#                 updata.pop(oldtitle, None)
#             specsobnew.listele = updata
#             specsobnew.save()
#             redirect('addspecs',id)
#         else:
#             specs(Product=prod,listele=data).save()
#     return render(request, 'superuser/addspecs.html', {'product':prod,"specs":specsob})
# def updatespecs(request,id,update=True):
#     return addspecs(request,id,update=True)
# def deletespecs(request,id,update=True):
#     title = request.GET.get('deltitle')
#     if title is not None:
#         prod = Product.objects.get(id=id)
#         specsob = specs.objects.filter(Product=prod.id)
#         specsobnew = specsob[0]
#         updata= specsobnew.jsondata()
#         updata.pop(title, None)
#         specsobnew.listele = updata
#         specsobnew.save()
#     return redirect('addspecs',id)

# def About(request):
#     res = {}
#     ins = about.objects.all()
#     ins = ins[0] if ins.exists() else None
#     res['form'] = aboutForm(instance=ins)
#     if request.method == 'POST':
#         res['form'] = aboutForm(request.POST,request.FILES,instance=ins)
#         if res['form'].is_valid():
#             res['form'].save()
#             messages.success(request ,'Changes is successfully saved :)')
#     return render(request,'superuser/about.html',res)


# def testdrivebooking(request):
#     res = {}
#     form = GenForm(TestDrive)
#     res['form'] = form()
#     if request.method == "POST":
#         res['form'] = form(request.POST,request.FILES)
#         if res['form'].is_valid():
#             res['form'].save()
#     return render(request,'superuser/testbooking.html',res)
# def alltestdrive(request):
#     res = {}
#     res['testdrives'] = TestDrive.objects.all().order_by('time')
#     return render(request,'superuser/alltestdrive.html',res)
# def contacts(request):
#     res = {}
#     res['contacts'] = Contact.objects.all().order_by('time')
#     return render(request,'superuser/contacts.html',res)
# def addcontact(request):
#     res = {}
#     form = GenForm(Contact)
#     res['form'] = form()
#     if request.method == "POST":
#         res['form'] = form(request.POST,request.FILES)
#         if res['form'].is_valid():
#             res['form'].save()
#     return render(request,'superuser/addcontact.html',res)
# def addinfo(request):
#     res = {}
#     form = GenForm(contactinfo)
#     ins = contactinfo.objects.all()
#     ins = ins[0] if ins.exists() else None
#     res['form'] = form(instance=ins)
#     if request.method == "POST":
#         res['form'] = form(request.POST,request.FILES,instance=ins)
#         if res['form'].is_valid():
#             res['form'].save()
#     return render(request,'superuser/addinfo.html',res)
# def orders(request,slug=None):
#     res = {}
#     res['choices'] = STATUS_CHOICE
#     if slug is None:
#         res['orders'] = OrderPlaced.objects.all().order_by('order_date')
#     else:
#         res['orders'] = OrderPlaced.objects.filter(status=slug).order_by('order_date')
#     return render(request,'superuser/orders.html',res)
# def addorders(request,id=None):
#     res = {}
#     form = GenForm(OrderPlaced)
#     ins = OrderPlaced.objects.filter(id=id)
#     ins = ins[0] if ins.exists() else None
#     res['form'] = form(instance=ins)
#     if request.method == "POST":
#         res['form'] = form(request.POST,request.FILES,instance=ins)
#         if res['form'].is_valid():
#             res['form'].save()
#     return render(request,'superuser/addorders.html',res)


# def users(request,slug=None):
#     res={}
#     if slug is  None:
#         res['users'] = User.objects.all()
#     return render(request,'superuser/users.html',res)
