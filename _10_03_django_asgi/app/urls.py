from django.urls import path

from app import views

app_name = 'app'

urlpatterns = [
    path('sync/', views.sync_view),
    path('async/', views.async_view),
]