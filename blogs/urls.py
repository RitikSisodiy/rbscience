from django.urls import path
from . import views
urlpatterns = [
    path('blogs/', views.blogs , name='blogs' ),
    path('categogy/<slug:slug>', views.categoryblog , name='catblogs' ),
    # path('<slug:slug1>/', views.singleblog , name='singleblog' ),
    path('blogs/postcomment/',views.postcomment , name='postcomment' ),
    path('singleblog/<slug:slug1>/', views.singleblog , name='singleblog' ),
    path('gethostname', views.gethost , name='gethost' ),
    
]
