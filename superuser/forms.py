from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from onlineshop.models import *
from .models import about


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('id',)    
        widgets = {'reg_title': forms.HiddenInput()}  
class aboutForm(ModelForm):
    class Meta:
        model = about
        exclude = ('id',) 
def GenForm(Model):
    class newform(ModelForm):
        class Meta:
            model = Model
            exclude = ('id',)
    return newform