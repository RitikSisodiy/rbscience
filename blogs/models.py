from django.db import models
from django.db.models import fields
from django.db.models.fields import TextField
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
import random ,string
def get_random_string(size):
    return ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = size))
def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    slug=slugify(new_slug)[:50]
    Klass = instance
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = slugify(str(slug)[:46]+get_random_string(4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


class category(models.Model):
    cat = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = unique_slug_generator(category,self.cat)
        super(category, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.cat)


class Blogs(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE,related_name="Blogs")
    title = models.CharField(max_length=100)
    blog_des = models.CharField(max_length=200)
    blog_detail = RichTextUploadingField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    img =models.ImageField(upload_to="img")
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = unique_slug_generator(Blogs,self.title)
        super(Blogs, self).save(*args, **kwargs)
 
    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    blog = models.ForeignKey(Blogs, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    website = models.CharField(max_length=200,blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return '%s - %s' % (self.blog.title, self.name)
