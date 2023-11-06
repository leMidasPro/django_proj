from django.contrib import admin
from django.urls import path,include
import articles.urls
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('', views.homepage, name='homepage'),
    path('articles/', include(articles.urls)),
]
