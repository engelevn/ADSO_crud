from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.lista_productos, name='lista'),
    path('nuevo/', views.crear_producto, name='nuevo'),
    path('editar/<int:id>/', views.editar_producto, name='editar'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar'),
]
