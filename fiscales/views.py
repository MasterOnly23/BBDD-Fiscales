
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from fiscales.models import Fiscales
from fiscales.forms import Formularios

# Create your views here.

class Formulario_view(HttpRequest):

    def home(request):
        return render(request, 'home.html')

    def registrar_fiscal(request):
        fiscal = Formularios()
        return render(request, 'registrarFiscal.html', {"form":fiscal})


    def guardarFiscal(request):
        #if request.method == 'POST'
        fiscal = Formularios(request.POST)

        if fiscal.is_valid(): #validar que la informacion del request es true
            fiscal.save() #guardar en la db
            fiscal = Formularios() #instanciar de nuevo para limpiar lo campos

        return render(request, 'registrarFiscal.html', {"form":fiscal, "msg":"OK"}) #volvemos a renderiazar la misma vista para que cuando se ingrese un formulario me vuelva a dejar en misma vista para seguir ingresando

    def listar_fiscales(request):
        fiscales = Fiscales.objects.all()
        queryset = request.GET.get("buscar")
        if queryset:

            sucursal = Fiscales.objects.filter(nombre_sucursal__icontains=queryset)
            return render(request, 'listaFiscales.html', {"sucursal":sucursal})
        return render(request, 'listaFiscales.html', {"fiscales":fiscales})


    def editar_fiscal(request, id_fiscal):

        fiscal = Fiscales.objects.filter(id=id_fiscal).first() #filter para que me filtre por id y first para que me traiga el primer dato
        form = Formularios(instance=fiscal)
        return render(request, 'editFiscal.html', {"form":form, "fiscal":fiscal})

    def actualizar_fiscal(request, id_fiscal):

        fiscal = Fiscales.objects.get(pk=id_fiscal) #(pk=primary key)  get para seleccionar el objeto en la base de datos
        form = Formularios(request.POST, instance=fiscal) #con request post le digo que obtenga los datos que se ingresaron en el formulario
        # y lo matchee con el objeto de la base de datos

        if form.is_valid(): #si el formulario es valido
            form.save()

        fiscales = Fiscales.objects.all() #hacemos de nuevo una peticion a la base de datos para redireccionar al usuario a la lista de familiares despues de actualizar el objeto
        return render(request, 'listaFiscales.html', {"fiscales":fiscales})

    def eliminar_fiscal(request, id_fiscal):

        fiscal = Fiscales.objects.get(pk=id_fiscal) #seleccionamos el objeto de la base de datos que queremos eliminar, buscamos el id
        fiscal.delete() #metodo delete 
        fiscales = Fiscales.objects.all()
        return render(request, 'listaFiscales.html', {"fiscales":fiscales, "msg":"OK"})#agregamos la variable msg para habilitar la alerta del mensaje cuando el alumno sea eliminado correctamente
        

    def buscar_fiscal(request, nombre_suc):
        queryset = request.GET.get("buscar")
        if queryset:

            sucursal = Fiscales.objects.filter(nombre_sucursal__icontains=queryset)
            return render(request, 'buscar.html', {"sucursal":sucursal})
        else:
            return render(request, 'buscar.html', {"busqueda":queryset, "msg":'No data'})