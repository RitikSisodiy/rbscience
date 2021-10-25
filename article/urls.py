from django.urls import path
from . import views
urlpatterns = [
    path('', views.article , name='article' ),
    path('submitartical/', views.submitarticle , name='submitarticle' ),
    path('archives/', views.archives , name='archives' ),
]
