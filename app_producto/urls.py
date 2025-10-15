from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),  # Ruta principal muestra listado
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('producto/borrar/<int:id>/', views.borrar_producto, name='borrar_producto'),
]


