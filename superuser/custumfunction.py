from django.urls import reverse
def getobjecturl(value):
    modelclass = type(value)
    modelname = modelclass._meta.model_name
    objectid = value.id
    applabel = modelclass._meta.app_label
    url = reverse('editdatamodel', args = [applabel, modelname , objectid,'edit'])
    atag = f"<a href='{url}'>{str(value)}</a>"
    print(modelname,objectid,applabel,url)
    return atag