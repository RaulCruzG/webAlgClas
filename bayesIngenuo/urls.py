from django.urls import path
from . import views

urlpatterns = [
    path('', views.clasificacion_Bayes, name='bayes'),
]