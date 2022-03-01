from django.urls import path

from .views import GrupoIntegranteListar, GrupoIntegranteCrear, GrupoIntegranteEditar, TipoIntegranteListar, \
    TipoIntegranteCrear, TipoIntegranteEditar, LugaresPraticasListar, LugaresPraticasCrear, LugaresPraticasEditar, \
    SolictudPracticasListar, SolictudPracticasCrear, PracticaDetalle, VehiculoPracticasListar, \
    VehiculoPracticaCrear, DocenteBuscar, DocenteBusarcarAdd, DocentePractica, ConductorBusarcarAdd, ConductorPractica, \
    RutasPraticasListar, RutasPraticasCrear, MateriaPraticasListar, MateriasBusarcarAdd, MateriasPracticaCrear, \
    GruposList, MatriculaGrupoPersonaListar, agregarEstudiante, DocentePracticasListar, ConductorPracticasListar, \
    AuxiliarPracticasListar, AuxiliarBusarcarAdd, AuxiliarPractica, CostosPraticasListar, CostosPraticasCrear, \
    VehicleManagmentView, SolictudPracticasUpdate

# SolictudPracticasEditar,
app_name = 'gestionpratica'

urlpatterns = [
    path('grupointegrante/', GrupoIntegranteListar.as_view(), name='grupointegrante_listar'),
    path('grupointegrantenuevo', GrupoIntegranteCrear.as_view(), name='grupointegrante_crear'),
    path('grupointegranteeditar/<int:pk>', GrupoIntegranteEditar.as_view(), name='grupointegrante_editar'),
    path('tipointegrante/', TipoIntegranteListar.as_view(), name='tipointegrante_listar'),
    path('tipointegrantenuevo', TipoIntegranteCrear.as_view(), name='tipointegrante_crear'),
    path('tipointegranteeditar/<int:pk>', TipoIntegranteEditar.as_view(), name='tipointegrante_editar'),
    path('lugarespracticas/', LugaresPraticasListar.as_view(), name='lugarespracticas_listar'),
    path('lugarespracticasnuevo', LugaresPraticasCrear.as_view(), name='lugarespracticas_crear'),
    path('lugarespracticaseditar/<int:pk>', LugaresPraticasEditar.as_view(), name='lugarespracticas_editar'),
    path('solicitudpracticas/', SolictudPracticasListar.as_view(), name='solicitudpracticas_listar'),
    path('solicitudpracticasnuevo/', SolictudPracticasCrear.as_view(), name='solicitudpracticas_crear'),
    path('solicitudpracticasupdate/<int:pk>', SolictudPracticasUpdate.as_view(), name='solicitudpracticas_update'),
    # path('solicitudpracticaseditar/<int:pk>', SolictudPracticasEditar.as_view(), name = 'solicitudpracticas_editar'),
    path('practicadetallado/<int:pk>', PracticaDetalle.as_view(), name='practicas_detalle'),
    path('vehiculopractica/<int:pk>', VehiculoPracticasListar.as_view(), name='vehiculopractica_list'),
    path('vehiculopracticaadd/<int:pk>', VehiculoPracticaCrear.as_view(), name='vehiculopractica_add'),
    # path('docentepersona/<int:pk>', DocenteBuscar.as_view(), name = 'docentepersona_add'),
    path('docentepractica/<int:pk>', DocentePracticasListar.as_view(), name='docentepractica_list'),
    path('docentepersona/<int:pk>', DocenteBusarcarAdd, name='docentepersona_add'),
    path('docentepracticanuevo/<int:pk>/<int:pers>/<int:pege>', DocentePractica.as_view(),
         name='docentepractica_crear'),
    path('auxliarpractica/<int:pk>', AuxiliarPracticasListar.as_view(), name='auxiliarpractica_list'),
    path('auxiliarpersona/<int:pk>', AuxiliarBusarcarAdd, name='auxiliarpersona_add'),
    path('auxiliarpracticanuevo/<int:pk>/<int:pers>/<int:pege>', AuxiliarPractica.as_view(),
         name='auxiliarpractica_crear'),
    path('conductorpractica/<int:pk>', ConductorPracticasListar.as_view(), name='conductorpractica_list'),
    path('conductorpersona/<int:pk>', ConductorBusarcarAdd, name='conductorpersona_add'),
    path('conductorpracticanuevo/<int:pk>/<int:pers>/<int:pege>', ConductorPractica.as_view(),
         name='conductorpractica_crear'),
    path('costospracticas/<int:pk>', CostosPraticasListar.as_view(), name='costospracticas_listar'),
    path('costospracticasnuevo/<int:pract>', CostosPraticasCrear.as_view(), name='costospracticas_crear'),
    path('rutaspracticas/<int:pk>', RutasPraticasListar.as_view(), name='rutaspracticas_listar'),
    path('rutaspracticasnuevo/<int:pract>', RutasPraticasCrear.as_view(), name='rutaspracticas_crear'),
    path('materiaspracticas/<int:pk>', MateriaPraticasListar.as_view(), name='materiaspracticas_listar'),
    path('materiaspracticasadd/<int:pk>', MateriasBusarcarAdd, name='materiaspracticas_add'),
    path('materiaspracticanuevo/<int:pk>/<codigomateria>', MateriasPracticaCrear.as_view(),
         name='materiaspractica_crear'),
    path('gruposmaterialistar/<int:pk>/<codigomateria>', GruposList.as_view(), name='gruposmateria_listar'),
    path('matriculagrupospersonalistar/<int:pk>/<codmate>/<int:grupoid>', MatriculaGrupoPersonaListar.as_view(),
         name='matriculagrupopersona_listar'),
    path('agregarestudiantes', agregarEstudiante, name='agregarestudiantes'),
    # Gestion de Vehiculo
    path('vehicle_managment/', VehicleManagmentView.as_view(), name='vehicle_managment'),

]
