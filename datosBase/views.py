from django.shortcuts import render
from .models import Dato

# Create your views here.
def datos_list(request):
    consulta = Dato.objects.all()
    listaSuma = calculaSuma(consulta)
    contexto = zip(consulta, listaSuma)
    return render(request, 'datosBase/tablaDatos.html', {'datos': contexto})

def calculaSuma(lista):
    listaSuma = []
    for i in lista:
        listaSuma.append(i.var1 + i.var3 + i.var4)
    return listaSuma