from django.db import models

# Create your models here.



class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=500)