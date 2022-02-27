from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import View, ListView, CreateView,UpdateView,FormView,TemplateView,DeleteView,DetailView

from .models import MarcaVehiculos,TipoVehiculo,Vehiculos

from .forms import MarcaVehiculosForm,TipoVehiculoForm,VehiculosForm


# Create your views here.

#MARCA VEHICULOS
class MarcaVehiculosListar(ListView):
    model = MarcaVehiculos
    template_name = 'gestionflota/marcavehiculos_list.html'

class MarcaVehiculosCrear(CreateView):
    model = MarcaVehiculos
    form_class = MarcaVehiculosForm
    page_title = 'Nuevo Marca'
    success_url = reverse_lazy('gestionflota:marcavehiculo_listar')
    context_object_name = 'obj'
    template_name = 'gestionflota/marcavehiculos_form.html'

    def get_context_data(self, **kwargs):
        context = super(MarcaVehiculosCrear, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context

class MarcaVehiculosEditar(UpdateView):
    model = MarcaVehiculos
    form_class = MarcaVehiculosForm
    page_title = 'Editar Marca'
    success_url = reverse_lazy('gestionflota:marcavehiculo_listar')
    context_object_name = 'obj'
    template_name = 'gestionflota/marcavehiculos_form.html'

    def get_context_data(self, **kwargs):
        context = super(MarcaVehiculosEditar, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context

#TIPO DE VHICULOS

class TipoVehiculosListar(ListView):
    model = TipoVehiculo
    template_name = 'gestionflota/tipovehiculos_list.html'

class TipoVehiculosCrear(CreateView):
    model = TipoVehiculo
    form_class = TipoVehiculoForm
    page_title = 'Nuevo Tipo'
    success_url = reverse_lazy('gestionflota:tipovehiculo_listar')
    context_object_name = 'obj'
    template_name = 'gestionflota/tipovehiculos_form.html'

    def get_context_data(self, **kwargs):
        context = super(TipoVehiculosCrear, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context

class TipoVehiculosEditar(UpdateView):
    model = TipoVehiculo
    form_class = TipoVehiculoForm
    page_title = 'Editar Tipo'
    success_url = reverse_lazy('gestionflota:tipovehiculo_listar')
    context_object_name = 'obj'
    template_name = 'gestionflota/tipovehiculos_form.html'

    def get_context_data(self, **kwargs):
        context = super(TipoVehiculosEditar, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context


#VEHICULOS

class VehiculosListar(ListView):
    model = Vehiculos
    template_name = 'gestionflota/vehiculos_list.html'

class VehiculosCrear(CreateView):
    model = Vehiculos
    form_class = VehiculosForm
    page_title = 'Nuevo Tipo'
    success_url = reverse_lazy('gestionflota:vehiculo_listar')
    context_object_name = 'obj'
    template_name = 'gestionflota/vehiculos_form.html'

    def get_context_data(self, **kwargs):
        context = super(VehiculosCrear, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context

class VehiculosEditar(UpdateView):
    model = Vehiculos
    form_class = VehiculosForm
    page_title = 'Editar Tipo'
    success_url = reverse_lazy('gestionflota:vehiculo_listar')
    context_object_name = 'obj'
    template_name = 'gestionflota/vehiculos_form.html'

    def get_context_data(self, **kwargs):
        context = super(VehiculosEditar, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context