from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from django.db.models.base import Model
from django.conf import settings
from django.shortcuts import render

from rbscience.settings import INSTALLED_APPS
def appmodels(listofappname:list):
    resli = {}
    for name in listofappname:
        app_models = apps.get_app_config(name).get_models()
        Modellist = [mod.__name__ for mod in app_models]
        if len(Modellist)>0:
            resli[name] = Modellist
    return resli
# add appname is sequence you want to see in dashboard  
def getObjectbyAppModelName(appname , modelname):
    app_models = apps.get_app_config(appname).get_model(modelname)
    return app_models
#get model list by app name
def getmodelbyappname(appname):
    app_models = apps.get_app_config(appname).get_models()
    Modellist = [mod.__name__ for mod in app_models]
    return Modellist


#get app list
appslist = []
#exclude app name
exclude = (

)
#write in string like "appname.modelname"
showRelatedOnEditPage=(
    'gallary.Gallery',
)

for data in INSTALLED_APPS:
    if '.' not in data and data not in exclude:
        appslist.append(data)
appslist.insert(0,'auth')

getTitle = '' #add your admin app title