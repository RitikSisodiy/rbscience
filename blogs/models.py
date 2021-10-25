from django.db import models
from django.db.models import fields
from django.db.models.fields import TextField
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.



class Blogs(models.Model):
    title = models.CharField(max_length=100)
    blog_des = models.CharField(max_length=200)
    blog_detail = RichTextField(blank=True, null=True)
    date = models.DateField(auto_now=True)
    img =models.ImageField(upload_to="img")
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blogs, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    blog = models.ForeignKey(Blogs, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    website = models.CharField(max_length=200,blank=True)
    body = models.TextField()
    date = models.DateField(auto_now=True)

    # def __str__(self):
    #     return '%s - %s' % (self.blog.title, self.name)
