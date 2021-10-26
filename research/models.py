from django.db import models
from django.utils.text import slugify

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
    time = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to="research")
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.heading)
        super(researchModel, self).save(*args, **kwargs)
    def __str__(self):
        return self.heading