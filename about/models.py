from django.core.mail import message
from django.db import models
from django.db.models.fields import EmailField
from services.models import services
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
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

class InstuctionsToAuthors(models.Model):
    title  = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True)
class auditorialBoard(models.Model):
    type = models.CharField(max_length=20 , choices=(('1',"Chief Editor"),('2',"Editors")))
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=300)
    address = models.CharField(max_length=300)