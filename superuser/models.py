from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class about(models.Model):
    content = RichTextField()