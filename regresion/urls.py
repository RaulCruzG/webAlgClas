from django.urls import path
from . import views

urlpatterns = [
    path('', views.regresionLog, name='regresionL'),
]