from django.urls import path
from . import views
urlpatterns = [
    path('blogs/', views.blogs , name='blogs' ),
    # path('<slug:slug1>/', views.singleblog , name='singleblog' ),
    path('blogs/postcomment/',views.postcomment , name='postcomment' ),
    path('singleblog/<slug:slug1>/', views.singleblog , name='singleblog' ),
    
]
