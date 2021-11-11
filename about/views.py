from django.http import request
from django.shortcuts import redirect, render
from django.contrib import messages
from team.models import TeamModel
from . models import *
from django.conf import settings
from django.core.mail import message, send_mail, EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from artical.forms import GenForm
from .models import InstuctionsToAuthors

# Create your views here.
def about(request):
    res = {}
    res['teammember'] = TeamModel.objects.all()
    return render(request,'about/about.html',res)



def contactus(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        data = ContactUs(name=name, email=email, phone=phone, subject=subject, message=message)
        data.save()
        # print(name + phone + subject)
        subject = 'RBSCIENCE'
        html_message = render_to_string('about/email.html',{'name':name,'phone':phone,'email':email,'subject':subject, 'message':message})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to = 'ritik.s10120@gmail.com'
        send_mail(subject, plain_message, from_email,[to],
        fail_silently=False,
        )
    return render(request,'about/contactus.html')
def servicecontact(request):
    if request.method == "POST":
        res = {}
        form = GenForm(servicesContact)
        form = form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , "Thanks For Contacting Us We Will Get Back To You Soon :)")
        else:
            messages.error(request,'please make sure you enter the correct Information..:)')
        res['form'] = form
        currenturl = request.POST.get('currenturl')
        currenturl = currenturl if currenturl is not None else "home"
        return redirect(currenturl)
        
def subscribe(request):
    if request.method == "POST":
        form= GenForm(subscriber)
        form = form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"thanks for subscribing We Will nortify you soon :)")   
        currenturl = request.POST.get('currenturl')
        currenturl = currenturl if currenturl is not None else "home"        
        return redirect(currenturl)
    return redirect('home')

def instructions(request):
    res= {}
    res['instructions'] = InstuctionsToAuthors.objects.all().order_by('id')
    return render(request , 'about/instructions.html',res)
def auditorialboard(request):
    res= {}
    res['board'] = {"Chief Editor":auditorialBoard.objects.filter(type='1').order_by('id'),'Editors':auditorialboardModel.objects.filter(type='2').order_by('id')}
    
    return render(request , 'about/auditorialboard.html',res)