from turtle import home
from django.contrib import admin
from django.urls import path
from fiscales.views import Formulario_view

urlpatterns = [
    path('', Formulario_view.home, name='home'),
    path('registrarFiscal/', Formulario_view.registrar_fiscal, name="registrarFiscal"),
    path('guardarFiscal/', Formulario_view.guardarFiscal, name="guardarFiscal"),
    path('listarFiscales/', Formulario_view.listar_fiscales, name="listaFiscales"),
    path('editFiscal/<int:id_fiscal>', Formulario_view.editar_fiscal, name="editFiscal"),
    path('actualizarFiscal/<int:id_fiscal>', Formulario_view.actualizar_fiscal, name="actualizarFiscal"),
    path('eliminarFiscal/<int:id_fiscal>', Formulario_view.eliminar_fiscal, name="eliminarFiscal"),
    path('buscar/<str:nombre_sucursal>', Formulario_view.buscar_fiscal, name='buscar'),
]
