from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.utils import timezone
import datetime
from django.views.generic import View, ListView, CreateView, UpdateView, FormView, TemplateView, DeleteView, DetailView

from .models import GrupoIntegrante, TipoIntegrante, ConceptosPraticas, LugaresPraticas, SolictudPratica, \
    PersonaIntegrante, \
    VhiculosPracticas, CostosPraticas, CostoPracticaPersona, RutasPractica, MateriasPracticas

from academico.models import Grupo, Programa, Materia, PensumMateria, MatriculaGrupoPersona
from academicoglobal.models import Persona
from general.models import PersonaGeneral

from .forms import GrupoIntegranteForm, TipoIntegranteForm, LugaresPraticasForm, SolictudPraticaForm, \
    VhiculosPracticasForm, \
    PersonaIntegranteDocenteForm, PersonaIntegranteConductorForm, RutasPracticaForm, MateriasPracticasForm, \
    AuxiliarPracticaForm, \
    CostosPraticasForm, SolictudPraticaGesVehicleForm


# Create your views here.

# AGRUPACION DE TIPOS DE INTEGRANTES

class GrupoIntegranteListar(ListView):
    model = GrupoIntegrante
    template_name = 'gestionpratica/grupointegrante_list.html'


class GrupoIntegranteCrear(CreateView):
    model = GrupoIntegrante
    form_class = GrupoIntegranteForm
    page_title = 'Nuevo Marca'
    success_url = reverse_lazy('gestionpratica:grupointegrante_listar')
    context_object_name = 'obj'
    template_name = 'gestionpratica/grupointegrante_form.html'

    def get_context_data(self, **kwargs):
        context = super(GrupoIntegranteCrear, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context


class GrupoIntegranteEditar(UpdateView):
    model = GrupoIntegrante
    form_class = GrupoIntegranteForm
    page_title = 'Editar Marca'
    success_url = reverse_lazy('gestionpratica:grupointegrante_listar')
    context_object_name = 'obj'
    template_name = 'gestionpratica/grupointegrante_form.html'

    def get_context_data(self, **kwargs):
        context = super(GrupoIntegranteEditar, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context


# TIPO DE INTEGRANTES

class TipoIntegranteListar(ListView):
    model = TipoIntegrante
    template_name = 'gestionpratica/tipointegrante_list.html'


class TipoIntegranteCrear(CreateView):
    model = TipoIntegrante
    form_class = TipoIntegranteForm
    page_title = 'Tipo de Integrante'
    success_url = reverse_lazy('gestionpratica:tipointegrante_listar')
    context_object_name = 'obj'
    template_name = 'gestionpratica/tipointegrante_form.html'

    def get_context_data(self, **kwargs):
        context = super(TipoIntegranteCrear, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context


class TipoIntegranteEditar(UpdateView):
    model = TipoIntegrante
    form_class = TipoIntegranteForm
    page_title = 'Editar Tipo de Integrante'
    success_url = reverse_lazy('gestionpratica:tipointegrante_listar')
    context_object_name = 'obj'
    template_name = 'gestionpratica/tipointegrante_form.html'

    def get_context_data(self, **kwargs):
        context = super(TipoIntegranteEditar, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context


# LUGARES PRACTICAS

class LugaresPraticasListar(ListView):
    model = LugaresPraticas
    template_name = 'gestionpratica/lugarespracticas_list.html'


class LugaresPraticasCrear(CreateView):
    model = LugaresPraticas
    form_class = LugaresPraticasForm
    page_title = 'Tipo de Integrante'
    success_url = reverse_lazy('gestionpratica:lugarespracticas_listar')
    context_object_name = 'obj'
    template_name = 'gestionpratica/lugarespracticas_form.html'

    def get_context_data(self, **kwargs):
        context = super(LugaresPraticasCrear, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context


class LugaresPraticasEditar(UpdateView):
    model = LugaresPraticas
    form_class = LugaresPraticasForm
    page_title = 'Editar Tipo de Integrante'
    success_url = reverse_lazy('gestionpratica:lugarespracticas_listar')
    context_object_name = 'obj'
    template_name = 'gestionpratica/lugarespracticas_form.html'

    def get_context_data(self, **kwargs):
        context = super(LugaresPraticasEditar, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context


# CREAR PRACTICAS

class SolictudPracticasListar(ListView):
    model = SolictudPratica
    template_name = 'gestionpratica/solicitudpracticas_list.html'


"""class SolictudPracticasCrear(CreateView):
    model = SolictudPratica
    form_class = SolictudPraticaForm
    page_title = 'NUEVA PRATICAS'
    success_url = reverse_lazy('gestionpratica:solicitudpracticas_listar')
    context_object_name = 'obj'
    template_name = 'gestionpratica/solicitudpracticas_form.html'

    def get_context_data(self, **kwargs):
        context = super(SolictudPracticasCrear, self).get_context_data(**kwargs)
        date = datetime.date.today()
        print('fecha ', date)
        year = date.strftime("%Y")
        context['page_title'] = self.page_title
        context['year'] = year
        return context

    def post(self, request, *args, **kwargs):
        #self.object = self.get_context_object
        form = self.form_class(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            numdias = request.POST['solp_numerodias']
            duracion = (int(numdias) - 0.5)
            solicitud.solp_duraciondoc = duracion
            #viaticos = request.POST['solp_liqviaticos']
            #print('estos son los viaticos', viaticos)

            #print('Se registra la inscripción')
            solicitud.save()
            #mail = correo
            #send_mail(mail, nombre, snombre)
            return HttpResponseRedirect(reverse_lazy('gestionpratica:solicitudpracticas_listar'))"""

"""class SolictudPracticasCrear(CreateView):
    model = SolictudPratica
    form_class = SolictudPraticaForm
    page_title = 'NUEVA PRATICAS'
    success_url = reverse_lazy('gestionpratica:solicitudpracticas_listar')
    context_object_name = 'obj'
    template_name = 'gestionpratica/solicitudpracticas_form.html'

    def get_context_data(self, **kwargs):
        context = super(SolictudPracticasCrear, self).get_context_data(**kwargs)
        date = datetime.date.today()
        print('fecha ', date)
        year = date.strftime("%Y")
        context['page_title'] = self.page_title
        context['year'] = year
        return context

    def post(self, request, *args, **kwargs):
        # self.object = self.get_context_object
        form = self.form_class(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            numdias = request.POST['solp_numerodias']
            duracion = (int(numdias) - 0.5)
            solicitud.solp_duraciondoc = duracion

            print('Se registra la inscripción')
            solicitud.save()
            #mail = correo
            #send_mail(mail, nombre, snombre)
            #return HttpResponseRedirect(reverse_lazy('gestionpratica:solicitudpracticas_listar'))
            return redirect(self.success_url)"""


class SolictudPracticasCrear(CreateView):
    model = SolictudPratica
    form_class = SolictudPraticaForm
    template_name = 'gestionpratica/solicitudpracticas2_form.html'
    success_url = reverse_lazy('gestionpratica:solicitudpracticas_listar')
    page_title = 'NUEVA PRATICAS'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super(SolictudPracticasCrear, self).get_context_data(**kwargs)
        date = datetime.date.today()
        year = date.strftime("%Y")
        context['year'] = year
        context['page_title'] = self.page_title
        return context

    def post(self, request, *args, **kwargs):
        try:
            form = self.form_class(request.POST)
            if form.is_valid():
                solicitud = form.save(commit=False)
                numdias = request.POST['solp_numerodias']
                duracion = (int(numdias) - (0.5))
                solicitud.solp_duraciondoc = duracion
                solicitud.save()
                return redirect(reverse('gestionpratica:solicitudpracticas_listar'))
        except ValueError as e:
            print('Value error', str(e))


class SolictudPracticasUpdate(UpdateView):
    model = SolictudPratica
    form_class = SolictudPraticaForm
    template_name = 'gestionpratica/solicitudpracticasupdate_form.html'
    success_url = reverse_lazy('gestionpratica:solicitudpracticas_listar')
    page_title = 'ACTUALIZAR PRATICAS'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super(SolictudPracticasUpdate, self).get_context_data(**kwargs)
        date = datetime.date.today()
        year = date.strftime("%Y")
        context['year'] = year
        context['page_title'] = self.page_title
        return context

    def post(self, request, *args, **kwargs):
        try:
            form = self.form_class(request.POST)
            if form.is_valid():
                solicitud = form.save(commit=False)
                numdias = request.POST['solp_numerodias']
                duracion = (int(numdias) - (0.5))
                solicitud.solp_duraciondoc = duracion
                solicitud.save()
                return redirect(reverse('gestionpratica:solicitudpracticas_listar'))
        except ValueError as e:
            print('Value error', str(e))

"""class SolictudPracticasEditar(UpdateView):
    model = SolictudPratica
    form_class = SolictudPraticaForm
    page_title = 'MODIFICAR PRATICAS'
    success_url = reverse_lazy('gestionpratica:solicitudpracticas_listar')
    context_object_name = 'obj'
    template_name = 'gestionpratica/solicitudpracticas_form.html'

    def get_context_data(self, **kwargs):
        context = super(SolictudPracticasEditar, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context

    def post(self, request, *args, **kwargs):
        # self.object = self.get_context_object
        form = self.form_class(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            numdias = request.POST['solp_numerodias']
            duracion = (int(numdias) - 0.5)
            solicitud.solp_duraciondoc = duracion

            print('Se registra la inscripción')
            solicitud.save()
            #mail = correo
            #send_mail(mail, nombre, snombre)
            return HttpResponseRedirect(reverse_lazy('gestionpratica:solicitudpracticas_listar'))"""


class VehicleManagmentView(UpdateView):
    model = SolictudPratica
    form_class = SolictudPraticaGesVehicleForm


class PracticaDetalle(TemplateView):
    template_name = 'gestionpratica/practica_detallado.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PracticaDetalle, self).get_context_data(**kwargs)
        # print('foranea;', self.kwargs.get('pk'))
        solpractica = SolictudPratica.objects.filter(solp_id=self.kwargs.get('pk')).first()
        # docenpracticas = PersonaIntegrante.objects.filter(solp_id=self.kwargs.get('pk'),tiin_id = 1)
        # condupracticas = PersonaIntegrante.objects.filter(solp_id=self.kwargs.get('pk'), tiin_id=2)
        # estidiantepracticas = PersonaIntegrante.objects.filter(solp_id=self.kwargs.get('pk'), tiin_id=3)
        integrantepracticas = PersonaIntegrante.objects.filter(solp_id=self.kwargs.get('pk'))
        todointegrante = CostoPracticaPersona.objects.filter(solp_id=self.kwargs.get('pk')).order_by('pein_id')
        contartodos = CostoPracticaPersona.objects.filter(solp_id=self.kwargs.get('pk')).count()
        vehiculopracticas = VhiculosPracticas.objects.filter(solp_id=self.kwargs.get('pk'))
        rutaspracticas = RutasPractica.objects.filter(solp_id=self.kwargs.get('pk'))
        apolloestudiante = CostosPraticas.objects.filter(solp_id=self.kwargs.get('pk'), copr_id=3).first()
        costodocentes = CostosPraticas.objects.filter(solp_id=self.kwargs.get('pk'), copr_id=1).first()
        costoauxiliar = CostosPraticas.objects.filter(solp_id=self.kwargs.get('pk'), copr_id=22).first()
        costoconductores = CostosPraticas.objects.filter(solp_id=self.kwargs.get('pk'), copr_id=2).first()
        costocombustible = CostosPraticas.objects.filter(solp_id=self.kwargs.get('pk'), copr_id=4).first()
        costopeajes = CostosPraticas.objects.filter(solp_id=self.kwargs.get('pk'), copr_id=5).first()
        costoimprevistos = CostosPraticas.objects.filter(solp_id=self.kwargs.get('pk'), copr_id=6).first()
        costootros = CostosPraticas.objects.filter(solp_id=self.kwargs.get('pk'), copr_id=7).first()

        if costodocentes:
            vdocente = costodocentes.ctpr_costototalxconcepto
        else:
            vdocente = 0
        if costoauxiliar:
            vauxiliar = costoauxiliar.ctpr_costototalxconcepto
        else:
            vauxiliar = 0
        if costoconductores:
            vconductores = costoconductores.ctpr_costototalxconcepto
        else:
            vconductores = 0
        if apolloestudiante:
            vestudientes = apolloestudiante.ctpr_costototalxconcepto
        else:
            vestudientes = 0
        if costocombustible:
            vconbustible = costocombustible.ctpr_costototalxconcepto
        else:
            vconbustible = 0
        if costopeajes:
            vpeajes = costopeajes.ctpr_costototalxconcepto
        else:
            vpeajes = 0
        if costoimprevistos:
            vimprevistos = costoimprevistos.ctpr_costototalxconcepto
        else:
            vimprevistos = 0
        if costootros:
            votros = costootros.ctpr_costototalxconcepto
        else:
            votros = 0
        totaldocencia = (vdocente + vauxiliar)
        totaltransporte = (vconductores + vconbustible + vpeajes + vimprevistos)
        totalpratica = (
                    vdocente + vauxiliar + vconductores + vestudientes + vconbustible + vpeajes + vimprevistos + votros)

        # print('solictu practica: ',solpractica)
        context['pk'] = self.kwargs.get('pk')
        context['solpractica'] = solpractica
        # context['docenpracticas'] = docenpracticas
        # context['condupracticas'] = condupracticas
        # context['estidiantepracticas'] = estidiantepracticas
        context['integrantepracticas'] = integrantepracticas
        context['todointegrante'] = todointegrante
        context['contartodos'] = contartodos
        context['vehiculopracticas'] = vehiculopracticas
        context['rutaspracticas'] = rutaspracticas
        context['apolloestudiante'] = apolloestudiante
        # ****
        context['vdocente'] = vdocente
        context['vauxiliar'] = vauxiliar
        context['vconductores'] = vconductores
        context['vestudientes'] = vestudientes
        context['vconbustible'] = vconbustible
        context['vpeajes'] = vpeajes
        context['vimprevistos'] = vimprevistos
        context['votros'] = votros
        context['totaldocencia'] = totaldocencia
        context['totaltransporte'] = totaltransporte
        context['totalpratica'] = totalpratica

        return context


class VehiculoPracticasListar(ListView):
    model = SolictudPratica
    page_title = 'Vehiculo Asignados a la Práctica'
    template_name = 'gestionpratica/vehiculospracticas_list.html'

    def get_context_data(self, **kwargs):
        context = super(VehiculoPracticasListar, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        context['page_title'] = self.page_title
        context['vehiculos'] = VhiculosPracticas.objects.filter(solp_id=self.kwargs.get('pk'))
        return context


class VehiculoPracticaCrear(CreateView):
    model = VhiculosPracticas
    form_class = VhiculosPracticasForm
    template_name = 'gestionpratica/vehiculopractica_add2.html'
    # success_url = reverse_lazy('pbdeportivas:datosantrop')
    page_title = 'Adicionar Vehiculo'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super(VehiculoPracticaCrear, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        # pk = self.kwargs.get('pk')
        context['page_title'] = self.page_title
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            pk = self.kwargs.get('pk')
            # solicitud.id_solp_id = self.kwargs.get('pk')
            solicitud.save()
            return HttpResponseRedirect(reverse_lazy('gestionpratica:vehiculopractica_list', kwargs={'pk': pk}))


# DOCENTES PRACTICAS
class DocenteBuscar(TemplateView):
    template_name = 'gestionpratica/docente_persona.html'

    def post(self, request, *args, **kwargs):
        context = super(DocenteBuscar, self).get_context_data(**kwargs)
        page_title = 'Docente'

        if request.method == 'POST':
            print(request.POST)
            # if request.POST['documento']:
            cdocumento = request.POST['documento']
            persona = Persona.objects.filter(pers_documentoidentidad=cdocumento)

            def get_context_data(self, **kwargs):
                context = super(VehiculoPracticaCrear, self).get_context_data(**kwargs)
                context['pk'] = self.kwargs.get('pk')
                context['persona'] = persona
                return context
            # else:
            #    print('no hay datos')


class DocentePracticasListar(ListView):
    model = PersonaIntegrante
    page_title = 'Docentes Asignados a la Práctica'
    template_name = 'gestionpratica/docentespracticas_list.html'

    def get_context_data(self, **kwargs):
        context = super(DocentePracticasListar, self).get_context_data(**kwargs)
        # tiin_id.grin_id.grin_nombre
        context['pk'] = self.kwargs.get('pk')
        context['page_title'] = self.page_title
        context['docentes'] = PersonaIntegrante.objects.filter(solp_id=self.kwargs.get('pk'), tiin_id__in=(1, 2))
        return context


def DocenteBusarcarAdd(request, pk):
    dd = pk
    print('primaria ', dd)
    if request.method == 'POST':
        print(request.POST)
        # if request.POST['documento']:
        cdocumento = request.POST['documento']
        print('documento llegado: ', cdocumento)
    else:
        cdocumento = ''
    persona = Persona.objects.filter(pers_documentoidentidad=cdocumento)
    print('datos persona', persona)
    # print('datos persona', persona.pers_primernombre)

    page_title = 'Asignar Docente a la Practica'
    context = {
        'page_title': page_title,
        'persona': persona,
        'dd': dd

    }
    return render(request, 'gestionpratica/docente_persona.html', context)


class DocentePractica(CreateView):
    model = PersonaIntegrante
    form_class = PersonaIntegranteDocenteForm
    page_title = 'Agrear Docente practica'
    success_url = reverse_lazy('gestionpratica:grupointegrante_listar')
    context_object_name = 'obj'
    template_name = 'gestionpratica/docentepractica_form.html'

    def get_context_data(self, **kwargs):
        context = super(DocentePractica, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        context['pers'] = self.kwargs.get('pers')
        context['pege'] = self.kwargs.get('pege')
        context['page_title'] = self.page_title
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        pk = self.kwargs.get('pk')
        if form.is_valid():
            solicitud = form.save(commit=False)
            practica = request.POST['solp_id']
            pers = request.POST['pers_id']
            pege = request.POST['pege_id']
            tipopersona = request.POST['tiin_id']
            print('tipo presona: ', tipopersona)
            solicitud.save()
            personain = solicitud.pein_id
            personainte = PersonaIntegrante.objects.only('pein_id').get(pein_id=personain)
            print('persona gurdadad: ', personain)
            print('**************************entra a consultar tablas ********************')
            solpracticas = SolictudPratica.objects.filter(solp_id=practica).first()
            print('practica: ', solpracticas)
            print('practicaid: ', solpracticas.solp_id)
            practicaid = solpracticas.solp_id
            practicafac = solpracticas.solp_duraciondoc
            solpract = SolictudPratica.objects.only('solp_id').get(solp_id=practica)

            conceptopractica = ConceptosPraticas.objects.filter(copr_requierebase=1, copr_estado=1, copr_id=1).first()
            valorbasepract = conceptopractica.copr_valorbase
            conceptopracticaid = conceptopractica.copr_id
            print('valor base concepto: ', valorbasepract)
            conprac = ConceptosPraticas.objects.only('copr_id').get(copr_requierebase=1, copr_estado=1, copr_id=1)

            print('**************************entra registrar costos practicas ********************')
            costopractica = CostosPraticas.objects.filter(solp_id=practica, copr_id=1).first()
            if costopractica:
                cantidad = costopractica.ctpr_cantidad + 1
                valtotalpract = (cantidad * practicafac * valorbasepract)
                guardarcostopractica = CostosPraticas.objects.filter(solp_id=practica, copr_id=1).update(
                    ctpr_cantidad=cantidad,
                    ctpr_costototalxconcepto=valtotalpract)
                # idguardarcostopractica = guardarcostopractica.ctpr_id
            else:
                valtotalpract = (1 * practicafac * valorbasepract)
                guardarcostopractica = CostosPraticas.objects.create(solp_id=solpract, copr_id=conprac, ctpr_cantidad=1,
                                                                     ctpr_costounitario=valorbasepract,
                                                                     ctpr_costototalxconcepto=valtotalpract)
                idguardarcostopractica = guardarcostopractica.ctpr_id

            print('**************************entra registrar costos practicas por persona ********************')
            costopracticapersona = CostoPracticaPersona.objects.filter(solp_id=practica, pein_id=personain).first()
            if costopracticapersona:
                pass
            else:
                # valtotalpract = (1 * practicafac * valorbasepract)
                guardarcostopracticapersona = CostoPracticaPersona.objects.create(solp_id=solpract, pein_id=personainte,
                                                                                  copr_id=conprac,
                                                                                  cpxp_costounitario=valorbasepract,
                                                                                  cpxp_unidadfactor=practicafac,
                                                                                  cpxp_unidadmedida='facduracion',
                                                                                  cpxp_costototalconceptopersona=(
                                                                                          valorbasepract * practicafac))
                guardarcostopracticapersonaid = guardarcostopracticapersona.cpxp_id

            return HttpResponseRedirect(reverse_lazy('gestionpratica:docentepractica_list', kwargs={'pk': pk}))


# AUXLIAR PRACTICA

class AuxiliarPracticasListar(ListView):
    model = PersonaIntegrante
    page_title = 'Auxliar Asignados a la Práctica'
    template_name = 'gestionpratica/auxliarpracticas_list.html'

    def get_context_data(self, **kwargs):
        context = super(AuxiliarPracticasListar, self).get_context_data(**kwargs)
        # tiin_id.grin_id.grin_nombre
        context['pk'] = self.kwargs.get('pk')
        context['page_title'] = self.page_title
        context['auxiliar'] = PersonaIntegrante.objects.filter(solp_id=self.kwargs.get('pk'), tiin_id=3)
        return context


def AuxiliarBusarcarAdd(request, pk):
    dd = pk
    print('primaria ', dd)
    if request.method == 'POST':
        print(request.POST)
        # if request.POST['documento']:
        cdocumento = request.POST['documento']
        print('documento llegado: ', cdocumento)
    else:
        cdocumento = ''
    persona = Persona.objects.filter(pers_documentoidentidad=cdocumento)
    print('datos persona', persona)
    # print('datos persona', persona.pers_primernombre)

    page_title = 'Asignar Auxilar a la Practica'
    context = {
        'page_title': page_title,
        'persona': persona,
        'dd': dd

    }
    return render(request, 'gestionpratica/auxiliar_persona.html', context)


class AuxiliarPractica(CreateView):
    model = PersonaIntegrante
    form_class = AuxiliarPracticaForm
    page_title = 'Agrear Auxiliar practica'
    success_url = reverse_lazy('gestionpratica:grupointegrante_listar')
    context_object_name = 'obj'
    template_name = 'gestionpratica/auxiliarpractica_form.html'

    def get_context_data(self, **kwargs):
        context = super(AuxiliarPractica, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        context['pers'] = self.kwargs.get('pers')
        context['pege'] = self.kwargs.get('pege')
        context['page_title'] = self.page_title
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        pk = self.kwargs.get('pk')
        if form.is_valid():
            solicitud = form.save(commit=False)
            practica = request.POST['solp_id']
            pers = request.POST['pers_id']
            pege = request.POST['pege_id']
            tipopersona = request.POST['tiin_id']
            print('tipo presona: ', tipopersona)
            solicitud.save()
            personain = solicitud.pein_id
            personainte = PersonaIntegrante.objects.only('pein_id').get(pein_id=personain)
            print('persona gurdadad: ', personain)
            print('**************************entra a consultar tablas ********************')
            solpracticas = SolictudPratica.objects.filter(solp_id=practica).first()
            print('practica: ', solpracticas)
            print('practicaid: ', solpracticas.solp_id)
            practicaid = solpracticas.solp_id
            practicafac = solpracticas.solp_duraciondoc
            solpract = SolictudPratica.objects.only('solp_id').get(solp_id=practica)

            conceptopractica = ConceptosPraticas.objects.filter(copr_requierebase=1, copr_estado=1, copr_id=22).first()
            valorbasepract = conceptopractica.copr_valorbase
            conceptopracticaid = conceptopractica.copr_id
            print('valor base concepto: ', valorbasepract)
            conprac = ConceptosPraticas.objects.only('copr_id').get(copr_requierebase=1, copr_estado=1, copr_id=22)

            print('**************************entra registrar costos practicas ********************')
            costopractica = CostosPraticas.objects.filter(solp_id=practica, copr_id=22).first()
            if costopractica:
                cantidad = costopractica.ctpr_cantidad + 1
                valtotalpract = (cantidad * practicafac * valorbasepract)
                guardarcostopractica = CostosPraticas.objects.filter(solp_id=practica, copr_id=22).update(
                    ctpr_cantidad=cantidad,
                    ctpr_costototalxconcepto=valtotalpract)
                # idguardarcostopractica = guardarcostopractica.ctpr_id
            else:
                valtotalpract = (1 * practicafac * valorbasepract)
                guardarcostopractica = CostosPraticas.objects.create(solp_id=solpract, copr_id=conprac, ctpr_cantidad=1,
                                                                     ctpr_costounitario=valorbasepract,
                                                                     ctpr_costototalxconcepto=valtotalpract)
                idguardarcostopractica = guardarcostopractica.ctpr_id

            print('**************************entra registrar costos practicas por persona ********************')
            costopracticapersona = CostoPracticaPersona.objects.filter(solp_id=practica, pein_id=personain).first()
            if costopracticapersona:
                pass
            else:
                # valtotalpract = (1 * practicafac * valorbasepract)
                guardarcostopracticapersona = CostoPracticaPersona.objects.create(solp_id=solpract, pein_id=personainte,
                                                                                  copr_id=conprac,
                                                                                  cpxp_costounitario=valorbasepract,
                                                                                  cpxp_unidadfactor=practicafac,
                                                                                  cpxp_unidadmedida='facduracion',
                                                                                  cpxp_costototalconceptopersona=(
                                                                                          valorbasepract * practicafac))
                guardarcostopracticapersonaid = guardarcostopracticapersona.cpxp_id

            return HttpResponseRedirect(reverse_lazy('gestionpratica:auxiliarpractica_list', kwargs={'pk': pk}))


# CONDUCTOR PARCTICA
class ConductorPracticasListar(ListView):
    model = PersonaIntegrante
    page_title = 'Conductor Asignados a la Práctica'
    template_name = 'gestionpratica/conductorpracticas_list.html'

    def get_context_data(self, **kwargs):
        context = super(ConductorPracticasListar, self).get_context_data(**kwargs)
        # tiin_id.grin_id.grin_nombre
        context['pk'] = self.kwargs.get('pk')
        context['page_title'] = self.page_title
        context['conductor'] = PersonaIntegrante.objects.filter(solp_id=self.kwargs.get('pk'), tiin_id__in=(4, 21))
        return context


def ConductorBusarcarAdd(request, pk):
    dd = pk
    print('primaria ', dd)
    if request.method == 'POST':
        print(request.POST)
        # if request.POST['documento']:
        cdocumento = request.POST['documento']
        print('documento llegado: ', cdocumento)
    else:
        cdocumento = ''
    persona = Persona.objects.filter(pers_documentoidentidad=cdocumento)
    print('datos persona', persona)
    # print('datos persona', persona.pers_primernombre)

    page_title = 'Asignar Conductor a la Practica'
    context = {
        'page_title': page_title,
        'persona': persona,
        'dd': dd

    }
    return render(request, 'gestionpratica/conductor_persona.html', context)


class ConductorPractica(CreateView):
    model = PersonaIntegrante
    form_class = PersonaIntegranteConductorForm
    page_title = 'Agrear Conductor practica'
    success_url = reverse_lazy('gestionpratica:grupointegrante_listar')
    context_object_name = 'obj'
    template_name = 'gestionpratica/conductorpractica_form.html'

    def get_context_data(self, **kwargs):
        context = super(ConductorPractica, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        context['pers'] = self.kwargs.get('pers')
        context['pege'] = self.kwargs.get('pege')
        context['page_title'] = self.page_title
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        pk = self.kwargs.get('pk')
        if form.is_valid():
            solicitud = form.save(commit=False)
            practica = request.POST['solp_id']
            pers = request.POST['pers_id']
            pege = request.POST['pege_id']
            tipopersona = request.POST['tiin_id']
            print('tipo presona: ', tipopersona)
            solicitud.save()
            personain = solicitud.pein_id
            personainte = PersonaIntegrante.objects.only('pein_id').get(pein_id=personain)
            print('persona gurdadad: ', personain)
            print('**************************entra a consultar tablas ********************')
            solpracticas = SolictudPratica.objects.filter(solp_id=practica).first()
            print('practica: ', solpracticas)
            print('practicaid: ', solpracticas.solp_id)
            practicaid = solpracticas.solp_id
            practicafac = solpracticas.solp_duraciondoc
            solpract = SolictudPratica.objects.only('solp_id').get(solp_id=practica)

            conceptopractica = ConceptosPraticas.objects.filter(copr_requierebase=1, copr_estado=1, copr_id=2).first()
            valorbasepract = conceptopractica.copr_valorbase
            conceptopracticaid = conceptopractica.copr_id
            print('valor base concepto: ', valorbasepract)
            conprac = ConceptosPraticas.objects.only('copr_id').get(copr_requierebase=1, copr_estado=1, copr_id=2)

            print('**************************entra registrar costos practicas ********************')
            costopractica = CostosPraticas.objects.filter(solp_id=practica, copr_id=2).first()
            if costopractica:
                cantidad = costopractica.ctpr_cantidad + 1
                valtotalpract = (cantidad * practicafac * valorbasepract)
                guardarcostopractica = CostosPraticas.objects.filter(solp_id=practica, copr_id=2).update(
                    ctpr_cantidad=cantidad,
                    ctpr_costototalxconcepto=valtotalpract)
                # idguardarcostopractica = guardarcostopractica.ctpr_id
            else:
                valtotalpract = (1 * practicafac * valorbasepract)
                guardarcostopractica = CostosPraticas.objects.create(solp_id=solpract, copr_id=conprac, ctpr_cantidad=1,
                                                                     ctpr_costounitario=valorbasepract,
                                                                     ctpr_costototalxconcepto=valtotalpract)
                idguardarcostopractica = guardarcostopractica.ctpr_id

            print('**************************entra registrar costos practicas por persona ********************')
            costopracticapersona = CostoPracticaPersona.objects.filter(solp_id=practica, pein_id=personain).first()
            if costopracticapersona:
                pass
            else:
                # valtotalpract = (1 * practicafac * valorbasepract)
                guardarcostopracticapersona = CostoPracticaPersona.objects.create(solp_id=solpract, pein_id=personainte,
                                                                                  copr_id=conprac,
                                                                                  cpxp_costounitario=valorbasepract,
                                                                                  cpxp_unidadfactor=practicafac,
                                                                                  cpxp_unidadmedida='facduracion',
                                                                                  cpxp_costototalconceptopersona=(
                                                                                          valorbasepract * practicafac))
                guardarcostopracticapersonaid = guardarcostopracticapersona.cpxp_id

            return HttpResponseRedirect(reverse_lazy('gestionpratica:conductorpractica_list', kwargs={'pk': pk}))


# RUTAS PRACTICAS
class RutasPraticasListar(ListView):
    model = RutasPractica
    template_name = 'gestionpratica/rutaspracticas_list.html'
    page_title = 'Adicionar Ruta Practica'

    def get_context_data(self, **kwargs):
        context = super(RutasPraticasListar, self).get_context_data(**kwargs)
        practica = self.kwargs.get('pk')
        context['pract'] = self.kwargs.get('pk')
        context['rutas'] = RutasPractica.objects.filter(solp_id=practica)
        # pk = self.kwargs.get('pk')
        context['page_title'] = self.page_title
        return context


class RutasPraticasCrear(CreateView):
    model = RutasPractica
    form_class = RutasPracticaForm
    template_name = 'gestionpratica/rutaspracticas_form.html'
    success_url = reverse_lazy('gestionpratica:rutaspracticas_listar')
    page_title = 'Adicionar Ruta'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super(RutasPraticasCrear, self).get_context_data(**kwargs)
        context['pract'] = self.kwargs.get('pract')
        # pk = self.kwargs.get('pk')
        context['page_title'] = self.page_title
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            pract = self.kwargs.get('pract')
            # solicitud.id_solp_id = self.kwargs.get('pk')
            solicitud.save()
            return HttpResponseRedirect(reverse_lazy('gestionpratica:rutaspracticas_listar', kwargs={'pk': pract}))


# COSTOS PRACTICAS
class CostosPraticasListar(ListView):
    model = CostosPraticas
    template_name = 'gestionpratica/costospracticas_list.html'
    page_title = 'Adicionar Costos Practica'

    def get_context_data(self, **kwargs):
        context = super(CostosPraticasListar, self).get_context_data(**kwargs)
        practica = self.kwargs.get('pk')
        context['costos'] = CostosPraticas.objects.filter(solp_id=practica)
        context['pract'] = self.kwargs.get('pk')
        # pk = self.kwargs.get('pk')
        context['page_title'] = self.page_title
        return context


class CostosPraticasCrear(CreateView):
    model = CostosPraticas
    form_class = CostosPraticasForm
    template_name = 'gestionpratica/costospracticas_form.html'
    success_url = reverse_lazy('gestionpratica:costospracticas_listar')
    page_title = 'Adicionar Costo a Practica'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super(CostosPraticasCrear, self).get_context_data(**kwargs)
        context['pract'] = self.kwargs.get('pract')
        # pk = self.kwargs.get('pk')
        context['page_title'] = self.page_title
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            pract = self.kwargs.get('pract')
            cantidad = request.POST['ctpr_cantidad']
            vunitario = request.POST['ctpr_costounitario']
            solicitud.ctpr_costototalxconcepto = ((int(cantidad)) * (float(vunitario)))
            # solicitud.id_solp_id = self.kwargs.get('pk')
            solicitud.save()
            return HttpResponseRedirect(reverse_lazy('gestionpratica:costospracticas_listar', kwargs={'pk': pract}))


# Materia
class MateriaPraticasListar(ListView):
    model = MateriasPracticas
    template_name = 'gestionpratica/materiaspracticas_list.html'
    page_title = 'Adicionar Materias'

    def get_context_data(self, **kwargs):
        context = super(MateriaPraticasListar, self).get_context_data(**kwargs)
        pratrica = self.kwargs.get('pk')
        context['pk'] = self.kwargs.get('pk')
        context['materias'] = MateriasPracticas.objects.filter(solp_id=pratrica)
        # pk = self.kwargs.get('pk')
        context['page_title'] = self.page_title
        return context


def MateriasBusarcarAdd(request, pk):
    dd = pk
    print('primaria ', dd)
    if request.method == 'POST':
        print(request.POST)
        # if request.POST['documento']:
        cmateria = request.POST['materia']
        print('materia llegado: ', cmateria)
    else:
        cmateria = ''
    materia = Materia.objects.filter(mate_codigomateria=cmateria)
    print('datos persona', materia)
    # print('datos persona', persona.pers_primernombre)

    page_title = 'Asignar Materia a la Practica'
    context = {
        'page_title': page_title,
        'materia': materia,
        'dd': dd

    }
    return render(request, 'gestionpratica/materiaspracticas_buscar.html', context)


class MateriasPracticaCrear(CreateView):
    model = MateriasPracticas
    form_class = MateriasPracticasForm
    page_title = 'Agrear Materia a  practica'
    success_url = reverse_lazy('gestionpratica:materiaspracticas_listar')
    context_object_name = 'obj'
    template_name = 'gestionpratica/materiaspractica_form.html'

    def get_context_data(self, **kwargs):
        context = super(MateriasPracticaCrear, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        context['codigomateria'] = self.kwargs.get('codigomateria')
        # context['pege'] = self.kwargs.get('pege')
        context['page_title'] = self.page_title
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            pract = self.kwargs.get('pk')
            # solicitud.id_solp_id = self.kwargs.get('pk')
            solicitud.save()
            return HttpResponseRedirect(reverse_lazy('gestionpratica:materiaspracticas_listar', kwargs={'pk': pract}))


class GruposList(TemplateView):
    # model = NivelEducativo
    template_name = 'gestionpratica/grupospracticas_form.html'
    page_title = 'Seleccionar Grupo'

    # queryset = NivelEducativo.objects.filter(nied_estado = 1)

    def get_context_data(self, *args, **kwargs):
        context = super(GruposList, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        codigomateria = self.kwargs.get('codigomateria')
        periodou = SolictudPratica.objects.only('peun_id').get(solp_id=self.kwargs.get('pk'))
        periodou = periodou.peun_id.peun_id
        print('periodo universidad: ', periodou)
        context['grupos'] = Grupo.objects.filter(peun_id=periodou, mate_codigomateria=codigomateria)
        context['page_title'] = self.page_title
        context['codigomateria'] = codigomateria
        print(context['grupos'])
        return context

    def post(self, request, *args, **kwargs):
        context = super(GruposList, self).get_context_data(**kwargs)
        # context['pk'] = self.kwargs.get('pk')
        page_title = 'Crcunscripción'

        if request.method == 'POST':
            pract = self.kwargs.get('pk')
            codigomateria = self.kwargs.get('codigomateria')
            gruposid = request.POST['m_option_1']
            return HttpResponseRedirect(
                reverse_lazy('gestionpratica:matriculagrupopersona_listar',
                             kwargs={'pk': pract, 'codmate': codigomateria, 'grupoid': gruposid}))

    """def post(self, request, *args, **kwargs):
        #context = super(GruposList, self).get_context_data(**kwargs)
        # context['pk'] = self.kwargs.get('pk')
        page_title = 'Crcunscripción'
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            pract = self.kwargs.get('pk')
            gruposid = request.POST['m_option_1']
            return HttpResponseRedirect(reverse_lazy('gestionpratica:matriculagrupopersona_listar', kwargs={'pk': pract, 'grupoid': gruposid}))"""


class MatriculaGrupoPersonaListar(TemplateView):
    model = MatriculaGrupoPersona
    template_name = 'gestionpratica/matriculagrupopersona_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MatriculaGrupoPersonaListar, self).get_context_data(**kwargs)
        grupoid = self.kwargs.get('grupoid')
        codigomateria = self.kwargs.get('codmate')
        context['pk'] = self.kwargs.get('pk')
        context['grupoid'] = grupoid
        context['codigomateria'] = codigomateria
        context['estudiantesgpr'] = MatriculaGrupoPersona.objects.filter(grup_id=grupoid)
        return context

    """def post(self, request, *args, **kwargs):
        context = super(MatriculaGrupoPersonaListar, self).get_context_data(**kwargs)
        # context['pk'] = self.kwargs.get('pk')
        page_title = 'Crcunscripción'
        pract = self.kwargs.get('pk')
        gruposid = self.kwargs.get('grupoid')"""

    """if requests.method == 'GET':
        pass
        if request.method == 'POST':

            ids=request.POST.getlist("ids[]")
            cat_change = Persona.objects.filter(pers_documentoidentidad__in=ids)
            for item in cat_change:
                persid = item.pers_id
                pegeid = item.pege_id
                solpid = pract
                tiinid = item.tiin_id
                print('persona id: ',persid)
                print('persona pege: ', pegeid)
                print('solicitud id: ', solpid)
                print('persona tipo: ', tiinid)
            return HttpResponse("OK")"""


def agregarEstudiante(request):
    if request.method == 'POST' and request.is_ajax():
        print('este es el post: ', request.POST)
        ids = request.POST.getlist("ids[]")
        print('esto llega: ', ids)
        grupo = request.POST['grupid']
        print('este es el grupo: ', grupo)
        materia = request.POST['mateid']
        print('este es el grupo: ', materia)
        practica = request.POST['practid']
        print('este es el grupo: ', practica)
        cat_change = Persona.objects.filter(pers_documentoidentidad__in=ids)
        print('todos los ids: ', cat_change)
        tipopersona = TipoIntegrante.objects.only('tiin_id').get(tiin_nombre='ESTUDIANTE')
        solpract = SolictudPratica.objects.only('solp_id').get(solp_id=practica)
        numdias = solpract.solp_numerodias
        ayudaeconomica = solpract.solp_ayudaeconomica
        fullviaje = solpract.solp_idayregreso
        grupos = Grupo.objects.only('grup_id').get(grup_id=grupo)
        materias = MateriasPracticas.objects.only('mapr_id').get(mate_codigomateria=materia, solp_id=practica)
        conprac = ConceptosPraticas.objects.only('copr_id').get(copr_requierebase=1, copr_estado=1, copr_id=3)
        valorbasepract = conprac.copr_valorbase
        conceptopracticaid = conprac.copr_id
        for item in cat_change:
            persid = Persona.objects.only('pers_id').get(pers_id=item.pers_id)
            # persid = item.pers_id
            pege = item.pege_id.pege_id
            print('persona general: ', pege)
            pegeid = PersonaGeneral.objects.only('pege_id').get(pege_id=pege)
            # pegeid = item.pege_id.pege_id
            # solpid = pract
            # grupopersona = TipoIntegrante.objects.filter(tiin_nombre='ESTUDIANTE').first()
            # tiinid = grupopersona.tiin_id
            print('persona id: ', persid)
            print('persona pege: ', pegeid)
            print('pratica: ', solpract.solp_id)
            print('grupo: ', grupos)
            print('materia: ', materias)
            # print('solicitud id: ', solpid)
            # print('persona tipo: ', tiinid)
            persona = PersonaIntegrante.objects.filter(solp_id=solpract, pers_id=item.pers_id).first()
            if persona:
                print("la persona ya esta agragada a la practica")
            else:
                crearpersona = PersonaIntegrante.objects.create(solp_id=solpract, tiin_id=tipopersona,
                                                                pers_id=persid, pege_id=pegeid, grup_id=grupos,
                                                                mapr_id=materias)
                crearpersonaid = crearpersona
                if ayudaeconomica == 1:
                    if fullviaje == 1:
                        numedias = numdias
                    else:
                        numedias = 1
                    print('**************************entra registrar costos practicas ********************')
                    costopractica = CostosPraticas.objects.filter(solp_id=practica, copr_id=conprac).first()
                    if costopractica:
                        cantidad = costopractica.ctpr_cantidad + 1
                        valtotalpract = (cantidad * numedias * valorbasepract)
                        guardarcostopractica = CostosPraticas.objects.filter(solp_id=practica, copr_id=conprac).update(
                            ctpr_cantidad=cantidad,
                            ctpr_costototalxconcepto=valtotalpract)
                        # idguardarcostopractica = guardarcostopractica.ctpr_id
                    else:
                        valtotalpract = (1 * numedias * valorbasepract)
                        guardarcostopractica = CostosPraticas.objects.create(solp_id=solpract, copr_id=conprac,
                                                                             ctpr_cantidad=1,
                                                                             ctpr_costounitario=valorbasepract,
                                                                             ctpr_costototalxconcepto=valtotalpract)
                        idguardarcostopractica = guardarcostopractica.ctpr_id

                    print('**************************entra registrar costos practicas por persona********************')
                    valtotalpractpers = (1 * numedias * valorbasepract)
                    guardarcostopracticapersona = CostoPracticaPersona.objects.create(solp_id=solpract,
                                                                                      pein_id=crearpersonaid,
                                                                                      copr_id=conprac,
                                                                                      cpxp_costounitario=valorbasepract,
                                                                                      cpxp_unidadfactor=numedias,
                                                                                      cpxp_unidadmedida='días',
                                                                                      cpxp_costototalconceptopersona=valtotalpractpers)
                else:
                    print("no hay ayudas economicas, por lo cual no se hace nada")
        return HttpResponse("OK")
    pass


# SOLICITUD PRESUPUESTO PRACTICAS
class SolPresupuestoListar(ListView):
    model = RutasPractica
    template_name = 'gestionpratica/rutaspracticas_list.html'
    page_title = 'Adicionar Ruta Practica'

    def get_context_data(self, **kwargs):
        context = super(RutasPraticasListar, self).get_context_data(**kwargs)
        practica = self.kwargs.get('pk')
        context['pract'] = self.kwargs.get('pk')
        context['rutas'] = RutasPractica.objects.filter(solp_id=practica)
        # pk = self.kwargs.get('pk')
        context['page_title'] = self.page_title
        return context


class SolPresupuestoCrear(CreateView):
    model = RutasPractica
    form_class = RutasPracticaForm
    template_name = 'gestionpratica/rutaspracticas_form.html'
    success_url = reverse_lazy('gestionpratica:rutaspracticas_listar')
    page_title = 'Adicionar Ruta'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super(SolPresupuestoCrear, self).get_context_data(**kwargs)
        context['pract'] = self.kwargs.get('pract')
        # pk = self.kwargs.get('pk')
        context['page_title'] = self.page_title
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            pract = self.kwargs.get('pract')
            # solicitud.id_solp_id = self.kwargs.get('pk')
            solicitud.save()
            return HttpResponseRedirect(reverse_lazy('gestionpratica:rutaspracticas_listar', kwargs={'pk': pract}))
