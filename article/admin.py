from django.contrib import admin
from . models import *

# Register your models here.



@admin.register(submenuscripts)
class submenuscriptsAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','filepdf',)
@admin.register(year)
class yearsAdmin(admin.ModelAdmin):
    list_display = ('year',)
@admin.register(vol)
class volAdmin(admin.ModelAdmin):
    list_display = ('vol',)
@admin.register(issue)
class issueAdmin(admin.ModelAdmin):
    list_display = ('issue',)
@admin.register(artical)
class articalAdmin(admin.ModelAdmin):
    list_display = ('heading','pdf',)
@admin.register(authors)
class authorsAdmin(admin.ModelAdmin):
    list_display = ('name',)
@admin.register(wp_posts)
class wp_postsAdmin(admin.ModelAdmin):
    list_display = ('id',)
    