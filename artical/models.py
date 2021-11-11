from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from blogs.models import unique_slug_generator
# Create your models here.
class submenuscripts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    filepdf = models.FileField(upload_to='submenupdf')
    remark = models.CharField(max_length=1000,blank=True)
class authors(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = "authors" , blank = True)
    def __str__(self):
        return self.name
class year(models.Model):
    year = models.CharField(max_length=4,unique=True)
    def __str__(self):
        return self.year
class vol(models.Model):
    vol = models.IntegerField(primary_key=True)
    def __str__(self):
        return 'Vol '+ str(self.vol)
class issue(models.Model):
    issue = models.IntegerField()
    year = models.ForeignKey(year, on_delete=models.CASCADE , related_name='articalbyyear')
    vol = models.ForeignKey(vol, on_delete=models.CASCADE,related_name="yearbyvol")
    def __str__(self):
        return  self.year.year +" | "+ str(self.vol) +" | issue " + str(self.issue)

        
class artical(models.Model):
    issue = models.ForeignKey(issue, on_delete=models.SET_NULL, null=True,related_name="yearbyissue")
    boardimg = models.ImageField(upload_to='articalimg',default='default.jpg')
    authors = models.ManyToManyField(authors)
    otherauthors = models.CharField(max_length=1000,blank=True)
    pdf = models.FileField(upload_to="achivesPdf")
    heading = models.CharField(max_length=500)
    abstract = RichTextUploadingField()
    keywords = RichTextUploadingField()
    doi = models.CharField(max_length=1000,blank=True)
    references = RichTextUploadingField(blank=True)
    time = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True,max_length=50)

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = unique_slug_generator(artical,self.heading)
        super(artical, self).save(*args, **kwargs)
 

