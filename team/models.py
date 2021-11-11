from django.db import models
from blogs.models import unique_slug_generator
from ckeditor_uploader.fields import RichTextUploadingField
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
    experience = RichTextUploadingField()
    def save(self, *args, **kwargs):
        if len(self.slug)<1:
            self.slug = unique_slug_generator(TeamModel,self.name)
        super(TeamModel, self).save(*args, **kwargs)
    def __str__(self):
        return self.name + " ("+ self.position + " )"
 