from django.contrib import admin
from django.urls import path,include
from .views import index,quienessomos,contacto,registro1,nuevopro,listar_flores,modificar_flor,galeria,eliminar_flor,registro_usuario,carro_compras,carro_compras_mas,carro_compras_menos,carros,grabar_carro
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', index,name='INDEX'),
    path('galeria/', galeria,name='GALERIA'),
    path('contacto/', contacto,name='CONTACTO'),
    path('registro1/', registro1,name='REGISTRO'),
    path('registro/nuevopro/', nuevopro,name='NUEVOPRO'),
    path('quienes-somos/', quienessomos,name='QUIENES'),
    path('listar_flores/', listar_flores,name='LISTAR'),
    path('modificar_flor/<nombre>/', modificar_flor,name='MODIFICARFLOR'),
    path('eliminar_flor/<nombre>/', eliminar_flor, name='ELIMINAR'),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('carro/',carros,name='CARRITO'),
    path('carro_mas/<nombre>/',carro_compras_mas,name='CARRO_MAS'),
    path('carro_menos/<nombre>/',carro_compras_menos,name='CARRO_MENOS'),
    path('grabar_carro/',grabar_carro,name='GRABAR_CARRO'),
]
