from django.core.mail import message
from django.db import models
from django.db.models.fields import EmailField
from services.models import services
# Create your models here.



class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=500)
class servicesContact(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    service = models.ForeignKey(services , null=True , on_delete=models.SET_NULL,related_name="servicesContact")
    message = models.TextField()
    time = models.DateTimeField(auto_now=True)
class subscriber(models.Model):
    email = models.EmailField(unique=True)