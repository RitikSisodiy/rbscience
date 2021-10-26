from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

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
    authors = models.ManyToManyField(authors)
    pdf = models.FileField(upload_to="achivesPdf")
    heading = models.CharField(max_length=500)
    abstract = RichTextField()
    keywords = RichTextField()
    do = models.CharField(max_length=1000,blank=True)
    references = RichTextField(blank=True)
    time = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True,max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.heading)[:50]
        super(artical, self).save(*args, **kwargs)


class wp_posts(models.Model):
    post_author	= models.BigIntegerField()
    post_date	= models.DateTimeField(auto_now=True)
    post_date_gmt = models.DateTimeField(auto_now=True)
    post_content = RichTextField()
    post_title	= models.CharField(max_length = 500)
    post_excerpt = models.CharField(max_length= 500)
    post_status = models.CharField(max_length=30 )
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()
    post_parent = models.BigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.CharField(max_length=200)
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    menu_order = models.CharField(max_length=200)
    comment_count = models.BigIntegerField()