from django.contrib import admin
from django.urls import path
from familiares.views import Formulario_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrarFamiliar/', Formulario_view.index),
    path('guardarFamiliar/', Formulario_view.guardarFamiliar, name="guardarFamiliar"),
    path('listarFamiliares/', Formulario_view.listar_familiares, name="listarFamiliares"),
]
