from django.urls import path
from . import views

urlpatterns = [
    path('', views.algKNN_list, name='algKNN'),
]