from django.contrib import admin
from . models import *

# Register your models here.

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title','blog_des','date','img')
@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('cat','slug',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','body')