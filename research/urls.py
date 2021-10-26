from django.urls import path
from . import views

urlpatterns = [
    path('', views.research , name='research' ),
    path('category/<slug:slug>', views.category , name='catresearch' ),
    path('<slug:slug>/', views.research , name='singleresearch' ),
    
]
