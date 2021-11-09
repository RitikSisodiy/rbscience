from django.db import models
from django.db.models.fields import CharField
from blogs.models import unique_slug_generator
from ckeditor.fields import RichTextField
from team.models import TeamModel
from django.utils.text import slugify
from blogs.models import category
# Create your models here.

class services(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE,related_name='services')
    type = models.CharField(max_length=10,choices=(('service','service'),('training','training'),))
    title = models.CharField(max_length=100)
    img1 = models.ImageField(upload_to = "services")
    img2 = models.ImageField(upload_to = "services", blank=True)
    tagline = models.CharField(max_length=500,blank=True,null=True,default='')
    details = RichTextField(blank=True, null=True)
    ourresearch = RichTextField(blank=True, null=True)
    associatedfaculty = models.ManyToManyField(TeamModel,blank=True)
    slug = models.SlugField(blank=True)


    def save(self, *args, **kwargs):
        if len(self.slug) < 1:
            self.slug = unique_slug_generator(services,self.title)
        super(services, self).save(*args, **kwargs)
 
    def __str__(self):
        return str(self.title)

class faq(models.Model):
    service = models.ForeignKey(services, related_name="faqs", on_delete=models.CASCADE  )
    ftitle = models.CharField(max_length=100)
    fdetails = models.TextField() 