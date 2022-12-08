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