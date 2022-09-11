from django.urls import path
from . import views

urlpatterns = [
    path('', views.flotante_list, name='flotante_list'),
]