from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('productos/', views.productos, name='Productos'), 
    path('vendedores/', views.vendedores, name='Vendedores'),
    path('cursos/', views.cursos, name='Cursos'), 
    path('cursosApi/', views.cursosapi), 
    path('productosApi/', views.productosapi),
    path('vendedoresApi/', views.vendedoresapi),
    path('busquedaCategoria/', views.buscarcategoria),
    path('buscar/', views.buscar),
]
