from django.urls import path
from . import views       #из этой же папке импортируем  vid


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about')
]