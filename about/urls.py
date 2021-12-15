from django.urls import path
from . import views
urlpatterns = [
    path('about/', views.about , name='about' ),
    path('contact_us01/', views.contactus , name='contactus' ),
    path('contactus/service/', views.servicecontact , name='servicecontact' ),
    path('subscribe/', views.subscribe , name='subscribe' ),
    path('instructions/', views.instructions , name='instructions' ),
    path('auditorialboard/', views.auditorialboard , name='auditorialboard' ),
    path('cetifications/', views.cetifications , name='cetifications' ),
]
