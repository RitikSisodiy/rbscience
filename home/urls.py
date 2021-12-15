from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name='home' ),
    path('home/', views.changenav , name='changenav' ),
    path('rbsciencehome/', views.rbsciencehome , name='rbsciencehome' ),
    path('logindashboard/', views.logindashboard, name="logindashboard"),
]
