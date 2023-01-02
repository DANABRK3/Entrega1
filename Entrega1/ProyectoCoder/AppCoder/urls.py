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
    path('leerVendedores/', views.leer_vendedores),
    path('crearVendedores/', views.crear_vendedores),
    path('editarVendedores/', views.editar_vendedores),
    path('eliminarVendedores/', views.eliminar_vendedores),
    path('vendedores/list/', views.vendedoresList.as_view(),name='List'),
    path('vendedores/create/', views.vendedoresCreate.as_view(),name='New'),
    path('vendedores/edit/<pk>', views.vendedoresEdit.as_view(),name='Edit'),
    path('vendedores/detail/<pk>', views.vendedoresDetail.as_view(),name='Detail'),
    path('vendedores/delete/<pk>', views.vendedoresDelete.as_view(),name='Delete'),
   
    ]
