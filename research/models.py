from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(category, self).save(*args, **kwargs)
    def __str__(self):
        return self.name
class researchModel(models.Model):
    category= models.ForeignKey(category , on_delete= models.CASCADE)
    heading = models.CharField(max_length=300)
    projectDetails = RichTextField(default="<p><strong>RESEARCH NAME</strong> : enter here..</p><p><strong>CLIENT </strong>: enter here..</p><p><strong>CATEGORY :</strong>enter here..</p><p><strong>DELIVERY MODE :</strong>enter here..</p><p><strong>LOCATION :</strong>enter here..</p>")
    overview = models.TextField()
    content = RichTextField()
    processOverview = RichTextField()
    time = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to="research")
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.heading)
        super(researchModel, self).save(*args, **kwargs)
    def __str__(self):
        return self.heading
class process(models.Model):
    researchModel = models.ForeignKey(researchModel,on_delete=models.CASCADE, related_name="process")
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=250)