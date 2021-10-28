from django.urls import path
from . import views

urlpatterns = [

    path('Services/<slug:slug1>', views.servic , name='services' ),
    path('training/<slug:slug>', views.training , name='training' ),
    
]
