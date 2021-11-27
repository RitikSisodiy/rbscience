from django.db import models

# Create your models here.
class homeSlider(models.Model):
    type = models.CharField(max_length=1 ,choices=(('1','mainsite'),('2','Journal Publication')), default='1')
    slider_image = models.ImageField(upload_to='sliders')
    title = models.CharField(max_length=50)
    keys = models.CharField(max_length=200,default="-,-,-")
    learnMoreurl = models.CharField(max_length=500)
class abstratingAndIndexing(models.Model):
    title = models.CharField(max_length=60)
    logo = models.ImageField(upload_to="abstractIndexing")