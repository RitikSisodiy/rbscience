from django.contrib import admin
from . models import *



@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'message')