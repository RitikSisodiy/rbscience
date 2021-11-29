from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class aboutContact(models.Model):
    logo = models.ImageField(upload_to="logo")
    phone = models.CharField(max_length=13,help_text="enter the 10 digit phone with country code example +91987654321")
    email = models.EmailField()
    workingHours = models.CharField(max_length=50, default="Mon to Fri: 9am to 8pm")
    country = models.CharField(max_length=20, default="india")
    state = models.CharField(max_length=50,default="Madhya Pradesh")
    city = models.CharField(max_length=50, default="Indore")
    BuildingNo = models.CharField(max_length=100,blank=True,help_text="Optional")
    address = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200,blank=True)
    twiter = models.CharField(max_length=200,blank=True)
    linkedin = models.CharField(max_length=200,blank=True)
    instagram = models.CharField(max_length=200,blank=True)
    fliker = models.CharField(max_length=200,blank=True)