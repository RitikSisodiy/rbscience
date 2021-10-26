from django.shortcuts import render
from . models import *
from django.conf import settings
from django.core.mail import message, send_mail, EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.
def about(request):
    res = {}
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