from django.db import connection
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from about.models import nortificationMail

from about.views import getEmailBackend
from .forms import GenForm
from django.core.mail import message, send_mail, EmailMessage
from rbscience import settings
from django.contrib import messages
from .models import downloadcount, issue, submenuscripts,artical, vol,year,blogviews

from django.db.models import Q
# Create your views here.


def visitor_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def articleview(request):
    res = {}
    return render(request , "article/journals.html" , res)
def submitarticle(request):
    res = {}
    res['title'] = "Submit Article" 
    if request.method == "POST":
        form = GenForm(submenuscripts)
        form = form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            res['data'] = form.instance
            res['host'] = request.get_host()
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['remark']
            subject = 'RBSCIENCE'
            html_message = render_to_string('about/submenuscript.html',res)
            plain_message = html_message
            from_email = settings.EMAIL_HOST_USER
            to = [data.email for data in nortificationMail.objects.all()]
            backend , config= getEmailBackend()
            from_email = config.email
            email = EmailMessage(
            subject,
            plain_message,
            from_email,
            to,
            headers={'Reply-To': from_email},
            connection=backend
            )
            if request.FILES:
                uploaded_file = request.FILES['filepdf'] # file is the name value which you have provided in form for file field
                email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
            email.content_subtype = 'html' 
            email.send()
            
            messages.success(request , "Your Submission is Successfull")
            return redirect(request.get_full_path())
        else:
            messages.error(request,'Invalid From Submission Check The Form Deatails')
    return render(request , 'article/submitartical.html', res)
def archives(request):
    res = {}
    res['title'] = "Archives"
    yeardata = year.objects.filter()
    years  = issue.objects.values_list('year','vol','issue').order_by("year__year").distinct()
    yearsvol = {d[0] : [] for d in years}
    for data in years:
        yearsvol[data[0]].append([data[1],data[2]])
    reslist = []
    for k,v in yearsvol.items():
        liap = []
        for d in v:
            articaldata = artical.objects.filter(issue__year = k , issue__vol = d[0],issue__issue = d[1])
            if len(articaldata)>0:
                liap.append(articaldata)
        if len(liap)>0:
                reslist.append(liap)
    res['yearsbydata'] = reslist
    return render(request,'article/archives.html', res)
def articallist(request , year , vol ,issue):
    absdata = artical.objects.all()
    # res1 ={'absdata':absdata}
    print(year,vol,issue)
    res = {}
    res['absdata'] = absdata
    res['artical'] = artical.objects.filter(issue=issue , issue__year__year = year , issue__vol = vol)
    res['title'] = "Archives"
    print(res['artical'])
    return render(request ,'article/articallist.html' ,res)
def search(request):
    query = request.GET.get('q')
    if query is not None :
        absdata = artical.objects.all()
        res = {}
        res['absdata'] = absdata
        res['artical'] = absdata.filter(Q(keywords__contains=query) | Q(authors__name=query)| Q(otherauthors__contains=query))
        res['title'] = query
        print(res['artical'])
        return render(request ,'article/articallist.html' ,res)
    return redirect('home')

def currentissue(request):
    res = {}
    latestartical = artical.objects.all()
    print(latestartical)
    if latestartical.exists():
        latestartical = latestartical.order_by('-time')[0]
        res['title'] = latestartical.issue
        year = latestartical.issue.year.year
        issue = latestartical.issue
        vol = latestartical.issue.vol
        return articallist(request,year , vol , issue)
    return redirect('home')

def abstractarticle(request,slug1,download=None):
    
    absdata = artical.objects.get(slug=slug1)
    if download == 'download':
        return downloadartical(absdata)
    viewupdate = blogviews.objects.get_or_create(articalid=absdata,ip = visitor_ip_address(request))
    res = {'absdata':absdata}
    res['title'] = absdata.heading
    res['views'] = blogviews.objects.filter(articalid=absdata.id).count()
    return render(request,'article/abstractarticle.html',res)
from wsgiref.util import FileWrapper
from django.utils.encoding import smart_str
import urllib, mimetypes,os
def downloadartical(file_name):
    file_path = str(settings.MEDIA_ROOT) +'/'+ file_name.pdf.name
    file_wrapper = FileWrapper(open(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name.pdf.name) 
    downcount = downloadcount.objects.filter(articalid = file_name.id)
    downcount = downcount[0] if downcount.exists() else downloadcount(articalid=file_name)
    downcount.dcount += 1
    downcount.save()
    return response

from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
@csrf_exempt
def addartical(request):
    if request.method == "POST":
        pdata = request.POST
        fdata = request.FILES
        yearob, created = year.objects.get_or_create(year=pdata['year'])
        volob, created = vol.objects.get_or_create(vol=pdata['vol'])
        issueob, created = issue.objects.get_or_create(issue=pdata['issue'],year=yearob,vol=volob)
        articalob, created = artical.objects.get_or_create(
            issue=issueob,
            otherauthors=strip_tags(pdata['otherauthors']),
            pdf=fdata['pdf'],
            abstract=pdata['abstract'],
            keywords=pdata['keywords'],
            do=pdata['do'],
            references=pdata['references'],
            heading=pdata['heading'],
            )
    return render(request,'article/addartical.html')