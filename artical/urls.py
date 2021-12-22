from django.urls import path
from . import views
urlpatterns = [
    path('jounrals/', views.articleview , name='article' ),
    path('jounrals/submitartical/', views.submitarticle , name='submitarticle' ),
    path('submissions/', views.submitarticle , name='submitarticle' ),
    path('jounrals/archives/', views.archives , name='archives' ),
    path('jounrals/archives/<slug:year>/<slug:vol>/<slug:issue>/articals' , views.articallist , name="listarticals"),
    path('jounrals/current/' , views.currentissue , name="currentissue"),
    path('jounrals/abstractarticle/<slug:slug1>/' , views.abstractarticle , name="abstractarticle"),
    # path('addartical/' , views.addartical , name="addartical"),
    path('jounrals/abstractarticle/<slug:slug1>/<slug:download>' , views.abstractarticle , name="downloadpdf"),
    path('search/',views.search,name="search")
    # path('abstractarticle/' , views.abstractarticle , name="abstractarticle"),
]
