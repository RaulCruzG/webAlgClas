from django.shortcuts import render
from .models import Entero

# Create your views here.
def entero_list(request):
    ent = Entero.objects.all()
    return render(request, 'prueba2/entero_list.html', {'enteros': ent})