from django.shortcuts import render
from .models import Flotante

# Create your views here.
def flotante_list(request):
    flo = Flotante.objects.all()
    return render(request, 'prueba1/flotante_list.html', {'flotantes': flo})