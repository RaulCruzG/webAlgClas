from django.urls import path
from . import views

urlpatterns = [
    path('', views.entero_list, name='entero_list'),
]