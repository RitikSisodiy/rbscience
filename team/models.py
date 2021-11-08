from django.db import models
from blogs.models import unique_slug_generator
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.
class TeamModel(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    twiter = models.CharField(max_length=100,blank=True)
    facebook = models.CharField(max_length=100,blank=True)
    google = models.CharField(max_length=100,blank=True)
    linkedin = models.CharField(max_length=100,blank=True)
    profile = models.ImageField(upload_to="teamprofile")
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=150 , blank=True)
    address = models.CharField(max_length=150)
    education = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    experience = RichTextField()
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = unique_slug_generator(TeamModel,self.cat)
        super(TeamModel, self).save(*args, **kwargs)
    def __str__(self):
        return self.name + " ("+ self.position + " )"
 