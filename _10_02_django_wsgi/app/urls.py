from django.conf.urls.i18n import urlpatterns
from django.urls import path

from app import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
]