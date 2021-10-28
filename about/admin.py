from django.contrib import admin
from . models import *



@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'message')
@admin.register(servicesContact)
class servicesContactAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'phone', 'service', 'message','time')
@admin.register(subscriber)
class subscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'id',)