from turtle import home
from django.contrib import admin
from django.urls import path
from familiares.views import Formulario_view

urlpatterns = [
    path('', Formulario_view.home),
    path('registrarFamiliar/', Formulario_view.index, name="registrarFamiliar"),
    path('guardarFamiliar/', Formulario_view.guardarFamiliar, name="guardarFamiliar"),
    path('listarFamiliares/', Formulario_view.listar_familiares, name="listarFamiliares"),
    path('editFamiliar/<int:id_familiar>', Formulario_view.editar_familiar, name="editFamiliar"),
    path('actualizarFamiliar/<int:id_familiar>', Formulario_view.actualizar_familiar, name="actualizarFamiliar"),
    path('eliminarFamiliar/<int:id_familiar>', Formulario_view.eliminar_familiar, name="eliminarFamiliar"),
]
