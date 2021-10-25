from django.urls import path
from . import views

urlpatterns = [

    path('JournalPublication/', views.jpublication , name='jpublication' ),
    
]
