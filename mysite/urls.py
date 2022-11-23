"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from algKNN import views as vk
from bayesIngenuo import views as vb
from regresion import views as vr
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('datosBase', include('datosBase.urls')),
    path('algKNN', include('algKNN.urls')),
    path('bayesIngenuo', include('bayesIngenuo.urls')),
    path('regresion', include('regresion.urls')),
    path('buscar/', vk.buscar),
    path('clasificar/', vb.clasificar),
    path('equivalente/', vr.interpretar),
]