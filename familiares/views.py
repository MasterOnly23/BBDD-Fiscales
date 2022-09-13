
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from familiares.models import Familiares
from familiares.forms import Formularios

# Create your views here.

class Formulario_view(HttpRequest):

    def index(request):
        familiar = Formularios()
        return render(request, 'index.html', {"form":familiar})


    def guardarFamiliar(request):

        familiar = Formularios(request.POST)

        if familiar.is_valid(): #validar que la informacion del request es true
            familiar.save() #guardar en la db
            familiar = Formularios() #instanciar de nuevo para limpiar lo campos

        return render(request, 'index.html', {"form":familiar, "msg":"OK"}) #volvemos a renderiazar la misma vista para que cuando se ingrese un formulario me vuelva a dejar en misma vista para seguir ingresando


