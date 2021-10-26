from django.urls import path
from . import views
urlpatterns = [
    path('', views.article , name='article' ),
    path('submitartical/', views.submitarticle , name='submitarticle' ),
    path('archives/', views.archives , name='archives' ),
    path('archives/<slug:year>/<slug:vol>/<slug:issue>/articals' , views.articallist , name="listarticals"),
    path('current/' , views.currentissue , name="currentissue"),
    path('abstractarticle/<slug:slug1>/' , views.abstractarticle , name="abstractarticle"),
    # path('abstractarticle/' , views.abstractarticle , name="abstractarticle"),
]
