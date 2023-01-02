from django.shortcuts import render
from django.http import HttpResponse

from AppCoder.models import Curso
from AppCoder.models import Productos
from AppCoder.models import Vendedores
from django.core import serializers
from AppCoder.forms import CursoFormulario
from AppCoder.forms import ProductosFormulario
from AppCoder.forms import VendedoresFormulario

# Create your views here.
def buscar(request):
    categoria_views=request.GET['categoria']
    productos_todos = Productos.objects.filter(categoria=categoria_views)
    return render(request, 'AppCoder/resultadoCategoria.html', {'categoria':categoria_views, 'productos':productos_todos})

def buscarcategoria(request):
    return render(request, 'AppCoder/busquedaCategoria.html')

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def vendedores(request):
    if request.method == "POST":
            miFormulario = VendedoresFormulario(request.POST) 
            print(miFormulario)
        
            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                vendedores = Vendedores(localidad=informacion["localidad"], 
                tiempo_de_entrega=informacion["tiempo_de_entrega"], calificacion=informacion["calificacion"])
                vendedores.save()
                return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = VendedoresFormulario()

    return render(request, "AppCoder/vendedores.html", {"miFormulario": miFormulario})
    

def productos(request):
    if request.method == "POST":
            miFormulario = ProductosFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
        
            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                productos = Productos(categoria=informacion["categoria"], 
                rango_precio=informacion["rango_precio"])
                productos.save()
                return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = ProductosFormulario()

    return render(request, "AppCoder/productos.html", {"miFormulario": miFormulario})

def cursos(request):
    if request.method == "POST":
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
        
            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                curso = Curso(nombre=informacion["nombre"], 
                comision=informacion["comision"], fecha_creacion=informacion["fecha_creacion"], dia_semana=informacion["dia_semana"])
                curso.save()
                return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario()

    return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})

def cursosapi(request):
    cursos_todos = Curso.objects.all()
    return HttpResponse(serializers.serialize('json',cursos_todos))

def productosapi(request):
    productos_todos = Productos.objects.all()
    return HttpResponse(serializers.serialize('json',productos_todos))

def vendedoresapi(request):
    vendedores_todos = Vendedores.objects.all()
    return HttpResponse(serializers.serialize('json',vendedores_todos))

def leer_vendedores(request):
    vendedores_todos = Vendedores.objects.all()
    return HttpResponse(serializers.serialize('json',vendedores_todos))

def crear_vendedores(request):
    vendedores = Vendedores(localidad='LocalidadTest',calificacion='10',tiempo_de_entrega='5')
    vendedores.save()
    return HttpResponse(f'Vendedores de la localidad de {vendedores.localidad} ha sido creado')


def editar_vendedores(request):
    localidad_consulta = 'LocalidadTest1'
    Vendedores.objects.filter(localidad=localidad_consulta).update(localidad='LocalidadTest1')
    return HttpResponse(f'La localidad {localidad_consulta} ha sido actualizado')


def eliminar_vendedores(request):
    localidad_nuevo='LocalidadNuevoVendedorTest'
    vendedores = Vendedores.objects.get(localidad=localidad_nuevo)
    vendedores.delete()
    return HttpResponse(f'Vendedor de la localidad {localidad_nuevo} ha sido eliminado')

# CRUD: CREATE,READ,UPDATE,DELETE   

from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

class vendedoresList (ListView):
    model = Vendedores
    template = 'AppCoder/vendedores_list.html'

class vendedoresCreate (CreateView):
    model = Vendedores
    fields = '__all__'
    success_url = '/AppCoder/vendedores/list/'

class vendedoresEdit(UpdateView):
    model = Vendedores
    fields = '__all__'
    success_url = '/AppCoder/vendedores/list/'

from django.views.generic.detail import DetailView

class vendedoresDetail (DetailView):
    model = Vendedores
    template = 'AppCoder/vendedores_detail.html'

class vendedoresDelete (DeleteView):
    model = Vendedores
    success_url = '/AppCoder/vendedores/list/'