
# code
from django.db import connection
from django.db.models.signals import post_save, pre_delete
from django.http import request

from about.views import getEmailBackend
from .models import artical
from about.models import subscriber
from blogs.models import Blogs
from threading import Thread
from django.dispatch import receiver
from rbscience import settings
from django.core.mail import message, send_mail, EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import inspect, os
@receiver(post_save, sender=artical)
def create_profile(sender, instance, created, **kwargs):
    if created:
        for entry in reversed(inspect.stack()):
                try:
                    request = entry[0].f_locals['request']
                    if str(type(request))=="<class 'django.core.handlers.wsgi.WSGIRequest'>":
                        break
                except:
                    request = None
        print(request.get_host())
        print('thread is working')
        Thread(target=sendmail, args=(instance,request,)).start()
def sendmail(instance,request):
    emailli = subscriber.objects.values_list('email')
    emailli = [data[0] for data in emailli]
    res = {}
    res['artical'] = instance
    res['recenttwo'] = Blogs.objects.all().order_by('date')[:2]
    res['host'] = 'http://'+request.get_host()
    subject = 'RBSCIENCE'
    html_message = render_to_string('blognortification.html',res)
    plain_message = html_message
    to = 'ritik.s10120@gmail.com'
    backend , config= getEmailBackend()
    from_email = config.email
    email = EmailMessage(
            subject,
            plain_message,
            from_email,
            emailli,
            headers={'Reply-To': from_email},
            connection=backend
    )
    email.content_subtype = 'html' 
    email.send()