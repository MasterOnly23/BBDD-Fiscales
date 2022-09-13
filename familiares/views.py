
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from familiares.models import Familiares
from familiares.forms import Formularios

# Create your views here.

class Formulario_view(HttpRequest):

    def home(request):
        return render(request, 'home.html')

    def index(request):
        familiar = Formularios()
        return render(request, 'index.html', {"form":familiar})


    def guardarFamiliar(request):

        familiar = Formularios(request.POST)

        if familiar.is_valid(): #validar que la informacion del request es true
            familiar.save() #guardar en la db
            familiar = Formularios() #instanciar de nuevo para limpiar lo campos

        return render(request, 'index.html', {"form":familiar, "msg":"OK"}) #volvemos a renderiazar la misma vista para que cuando se ingrese un formulario me vuelva a dejar en misma vista para seguir ingresando

    def listar_familiares(request):
        familiar = Familiares.objects.all()
        return render(request, 'listaFamiliares.html', {"familiares":familiar}) 


    def editar_familiar(request, id_familiar):

        familiar = Familiares.objects.filter(id=id_familiar).first() #filter para que me filtre por id y first para que me traiga el primer dato
        form = Formularios(instance=familiar)
        return render(request, 'editFamiliar.html', {"form":form, "familiar":familiar})

    def actualizar_familiar(request, id_familiar):

        familiar = Familiares.objects.get(pk=id_familiar) #get para seleccionar el objeto en la base de datos
        form = Formularios(request.POST, instance=familiar) #con request post le digo que obtenga los datos que se ingresaron en el formulario
        # y lo matchee con el objeto de la base de datos

        if form.is_valid(): #si el formulario es valido
            form.save()

        familiar = Familiares.objects.all() #acemos de nuevo una peticion a la base de datos para redireccionar al usuario a la lista de familiares despues de actualizar el objeto
        return render(request, 'listaFamiliares.html', {"familiares":familiar})

