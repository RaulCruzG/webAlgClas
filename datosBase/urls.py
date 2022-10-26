from django.urls import path
from . import views

urlpatterns = [
    path('', views.datos_list, name='tablaDatos'),
]