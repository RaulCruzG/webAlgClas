from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
from datosBase.models import Dato
# Create your views here.
def regresionLog(request):
    return render(request, 'regresion/regresionLogis.html')

def interpretar(request):
    if request.GET["x1"].isdigit() and request.GET["x2"].isdigit():
        x1 = int(request.GET["x1"])
        x2 = int(request.GET["x2"])
        datos = Dato.objects.all()
        b = calcConstante(datos)
        resultado  = valorReferente(datos, x1, x2, b)
        return render(request, 'regresion/equivalente.html', {'consulta': resultado} )
    else:
        mensaje = "Te falto llenar o llenaste incorrectamente, recuerda que deben ser valores numericos"
    return HttpResponse(mensaje)

def valorReferente(datos, x1, x2, b):
    caracter = ''
    for i in datos:
        a1 = i.var1
        caracter = i.var2
        a2 = i.var3
        break
    salida = 1/(1 + np.exp(-(a1*x1 + a2*x2 + b)))
    if salida > 0.5:
        respuesta = f'Es el caracter: {caracter}'
    else:
        respuesta = f'NO es el caracter: {caracter}'
    return respuesta

def calcConstante(datos):
    x = []
    y = []
    xCuadrada = 0
    xy = 0
    for i in datos:
        xCuadrada = xCuadrada + i.var1**2
        xy = xy + i.var1 * i .var3
        x.append(i.var1)
        y.append(i.var3)
    xSum = sum(x)
    ySum = sum(y)
    constante = (xCuadrada*ySum - xy*xSum)/(datos.count()*xCuadrada-xSum**2)
    return constante
    