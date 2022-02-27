from django.urls import path

from .views import MarcaVehiculosListar,MarcaVehiculosCrear,MarcaVehiculosEditar,TipoVehiculosListar,TipoVehiculosCrear,\
    TipoVehiculosEditar,VehiculosListar,VehiculosCrear,VehiculosEditar

app_name = 'gestionflota'

urlpatterns = [
    path('marcavehiculo/', MarcaVehiculosListar.as_view(), name= 'marcavehiculo_listar'),
    path('marcavehiculonuevo', MarcaVehiculosCrear.as_view(), name = 'marcavehiculo_crear'),
    path('marcavehiculoeditar/<int:pk>', MarcaVehiculosEditar.as_view(), name = 'marcavehiculo_editar'),
    path('tipovehiculo/', TipoVehiculosListar.as_view(), name= 'tipovehiculo_listar'),
    path('tipovehiculonuevo', TipoVehiculosCrear.as_view(), name = 'tipovehiculo_crear'),
    path('tipovehiculoeditar/<int:pk>', TipoVehiculosEditar.as_view(), name = 'tipovehiculo_editar'),
    path('vehiculo/', VehiculosListar.as_view(), name= 'vehiculo_listar'),
    path('vehiculonuevo', VehiculosCrear.as_view(), name = 'vehiculo_crear'),
    path('vehiculoeditar/<int:pk>', VehiculosEditar.as_view(), name = 'vehiculo_editar'),
]