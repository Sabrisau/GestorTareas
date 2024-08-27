# views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import Tarea

def ver_tareas_pendientes(request):
# Se interactúa con el modelo para obtener las tareas pendientes
    tareas_pendientes = Tarea.objects.filter(estado='pendiente')
# Se pasa la lista de tareas a la plantilla
    return render(request, 'pendientes.html', {'tareas': tareas_pendientes})
    #return HttpResponse("Hola")