from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(services)
class servicesadmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(faq)
class faqadmin(admin.ModelAdmin):
    list_display = ('service','ftitle')