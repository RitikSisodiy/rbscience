from django.contrib import admin
from . models import *
# Register your models here.
@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('name','id')
@admin.register(researchModel)
class researchModelAdmin(admin.ModelAdmin):
    list_display = ('heading','category')
@admin.register(process)
class processAdmin(admin.ModelAdmin):
    list_display = ('title','researchModel')
    