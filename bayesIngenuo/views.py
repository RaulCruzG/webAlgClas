from django.http import HttpResponse
from django.shortcuts import render
from datosBase.models import Dato
import numpy as np

caracteres = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K',
              'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V',
              'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
evidencia = len(caracteres)
probabilidadCaso = 1/len(caracteres)

# Create your views here.
def clasificacion_Bayes(request):
    return render(request, 'bayesIngenuo/bayes.html')

def clasificar(request):
    if request.GET["x1"].isdigit() and request.GET["x2"].isdigit() and request.GET["x3"].isdigit():
        x1 = int(request.GET["x1"])
        x2 = int(request.GET["x2"])
        x3 = int(request.GET["x3"])
        datos = Dato.objects.all()
        mediaC1 = calcmediaC1(datos)
        varianzaC1 = calcvarianzaC1(datos)
        mediaC2 = calcmediaC2(datos)
        varianzaC2 = calcvarianzaC2(datos)
        mediaC3 = calcmediaC3(datos)
        varianzaC3 = calcvarianzaC3(datos)
        prod = posteriori(mediaC1, mediaC2, mediaC3, varianzaC1, varianzaC2, varianzaC3, x1, x2, x3)
        tabProd = zip(caracteres, mediaC1, mediaC2, mediaC3, varianzaC1, varianzaC2, varianzaC3, prod)
        prod = calcreferencia(mediaC1, mediaC2, mediaC3, varianzaC1, varianzaC2, varianzaC3, x1, x2, x3)
        return render(request, 'bayesIngenuo/respuesta.html', {'referencia': prod, 'resultado': tabProd})
    else:
        mensaje = "Te falto llenar o llenaste incorrectamente, recuerda que deben ser valores numericos"
    return HttpResponse(mensaje)

def calcmediaC1(datos):
    listaMedia = []
    for i in caracteres:
        lista = []
        for j in datos:
            if i == j.var2:
                lista.append(j.var1)
        if len(lista) == 0:
            listaMedia.append(0.0)
        else:
            lis = np.array(lista, int)
            listaMedia.append(round(lis.mean(), 3))
    return listaMedia

def calcvarianzaC1(datos):
    listaVarianza = []
    for i in caracteres:
        lista = []
        for j in datos:
            if i == j.var2:
                lista.append(j.var1)
        if len(lista) == 0:
            listaVarianza.append(0.0)
        else:
            lis = np.array(lista, int)
            listaVarianza.append(round(lis.var(), 3))
    return listaVarianza

def calcmediaC2(datos):
    listaMedia = []
    for i in caracteres:
        lista = []
        for j in datos:
            if i == j.var2:
                lista.append(j.var3)
        if len(lista) == 0:
            listaMedia.append(0.0)
        else:
            lis = np.array(lista, int)
            listaMedia.append(round(lis.mean(), 3))
    return listaMedia

def calcvarianzaC2(datos):
    listaVarianza = []
    for i in caracteres:
        lista = []
        for j in datos:
            if i == j.var2:
                lista.append(j.var3)
        if len(lista) == 0:
            listaVarianza.append(0.0)
        else:
            lis = np.array(lista, int)
            listaVarianza.append(round(lis.var(), 3))
    return listaVarianza

def calcmediaC3(datos):
    listaMedia = []
    for i in caracteres:
        lista = []
        for j in datos:
            if i == j.var2:
                lista.append(j.var4)
        if len(lista) == 0:
            listaMedia.append(0.0)
        else:
            lis = np.array(lista, int)
            listaMedia.append(round(lis.mean(), 3))
    return listaMedia

def calcvarianzaC3(datos):
    listaVarianza = []
    for i in caracteres:
        lista = []
        for j in datos:
            if i == j.var2:
                lista.append(j.var4)
        if len(lista) == 0:
            listaVarianza.append(0.0)
        else:
            lis = np.array(lista, int)
            listaVarianza.append(round(lis.var(), 3))
    return listaVarianza

def calcreferencia(mediaC1, mediaC2, mediaC3, varianzaC1, varianzaC2, varianzaC3, x1, x2, x3):
    referencia = ''
    mayor = 0
    x = 0
    for i in caracteres:
        if varianzaC1[x] == 0.0 or mediaC1[x] == 0.0 or varianzaC2[x] == 0.0 or mediaC2[x] == 0.0 or varianzaC3[x] == 0.0 or mediaC3[x] == 0.0:
            pass
        else:
            probC1Var = 1/(np.sqrt(2*np.pi*(varianzaC1[x]**2))) * np.exp((-(x1-mediaC1[x])**2)/(2*varianzaC1[x]**2))
            probC2Var = 1/(np.sqrt(2*np.pi*(varianzaC2[x]**2))) * np.exp((-(x2-mediaC2[x])**2)/(2*varianzaC2[x]**2))
            probC3Var = 1/(np.sqrt(2*np.pi*(varianzaC3[x]**2))) * np.exp((-(x3-mediaC3[x])**2)/(2*varianzaC3[x]**2))
            producto = (probabilidadCaso*probC1Var*probC2Var*probC3Var)/evidencia
            if producto >= mayor:
                mayor = producto
                referencia = i 
        x = x + 1  
    return referencia

def posteriori(mediaC1, mediaC2, mediaC3, varianzaC1, varianzaC2, varianzaC3, x1, x2, x3):
    productos = []
    mayor = 0
    x = 0
    for i in caracteres:
        if varianzaC1[x] == 0.0 or mediaC1[x] == 0.0 or varianzaC2[x] == 0.0 or mediaC2[x] == 0.0 or varianzaC3[x] == 0.0 or mediaC3[x] == 0.0:
            valorPrueba = 'Null'
        else:
            probC1Var = 1/(np.sqrt(2*np.pi*(varianzaC1[x]**2))) * np.exp((-(x1-mediaC1[x])**2)/(2*varianzaC1[x]**2))
            probC2Var = 1/(np.sqrt(2*np.pi*(varianzaC2[x]**2))) * np.exp((-(x2-mediaC2[x])**2)/(2*varianzaC2[x]**2))
            probC3Var = 1/(np.sqrt(2*np.pi*(varianzaC3[x]**2))) * np.exp((-(x3-mediaC3[x])**2)/(2*varianzaC3[x]**2))
            producto = (probabilidadCaso*probC1Var*probC2Var*probC3Var)/evidencia
            if producto >= mayor:
                mayor = producto
            valorPrueba = producto
        x = x + 1  
        productos.append(valorPrueba)
    return productos