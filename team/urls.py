from django.urls import path
from . import views

urlpatterns = [

    path('', views.team , name='team' ),
    path('<slug:slug>/', views.team , name='singleteam' ),
    
]
