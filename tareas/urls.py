# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_tareas_pendientes, name='ver_tareas_pendientes'),
]