from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Textarea
from django.utils import timezone

from .models import MarcaVehiculos,TipoVehiculo,Vehiculos

class MarcaVehiculosForm(forms.ModelForm):
    class Meta:
        model = MarcaVehiculos
        fields =[
            'mveh_nombre',
            'mveh_descripcion',
        ]
        labels = {
            'mveh_nombre': 'Marca',
            'mveh_descripcion': 'Descripción',
        }
        help_texts = {
            'mveh_nombre': 'Ingrese el Modulo',
            'mveh_descripcion': 'Ingrese Descripción',
        }
        widgets = {
            'mveh_nombre': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Marca Vehiculo'}),
            'mveh_descripcion': forms.Textarea(attrs={'class': 'form-control','rows': 5,'cols': 20,'placeholder': 'Ingrese Descipción'}),
        }

class TipoVehiculoForm(forms.ModelForm):
    class Meta:
        model = TipoVehiculo
        fields =[
            'tveh_nombre',
            'tveh_descripcion',
        ]
        labels = {
            'tveh_nombre': 'Tipo',
            'tveh_descripcion': 'Descripción',
        }
        help_texts = {
            'tveh_nombre': 'Ingrese Tipo De Vehiculo',
            'tveh_descripcion': 'Ingrese Descripción',
        }
        widgets = {
            'tveh_nombre': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Tipo Vehiculo'}),
            'tveh_descripcion': forms.Textarea(attrs={'class': 'form-control','rows': 5,'cols': 20,'placeholder': 'Ingrese Descipción'}),
        }

class VehiculosForm(forms.ModelForm):
    class Meta:
        model = Vehiculos
        fields =[
            'vehi_placa',
            'mveh_id',
            'tveh_id',
            'vehi_combustible',
            'vehi_capacidadcombustible',
            'vehi_capacidadpasajeros',
            'vehi_capacidadaaforopasajeros',
        ]
        labels = {
            'vehi_placa': 'Placa',
            'mveh_id': 'Marca',
            'tveh_id': 'Tipo',
            'vehi_combustible': 'Combustible',
            'vehi_capacidadcombustible': 'Capacidad Combustible',
            'vehi_capacidadpasajeros': 'Capacidad Pasajeros',
            'vehi_capacidadaaforopasajeros': 'Capacidad Pasajeros Aforo',
        }
        help_texts = {
            'vehi_placa': 'Ingrese Placa',
            'mveh_id': 'seleccione Marca',
            'tveh_id': 'seleccione Tipo',
            'vehi_combustible': 'seleccione Combustible',
            'vehi_capacidadcombustible': 'Ingrese Capacidad Combustible',
            'vehi_capacidadpasajeros': 'Ingrese Capacidad Pasajeros',
            'vehi_capacidadaaforopasajeros': 'Ingrese Capacidad Pasajeros por Aforo',
        }
        widgets = {
            'vehi_placa': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Placa'}),
            'mveh_id': forms.Select(
                attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Marca Vehiculo'}),
            'tveh_id': forms.Select(
                attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Tipo Vehiculo'}),
            'vehi_combustible': forms.Select(
                attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Combustible'}),
            'vehi_capacidadcombustible': forms.TextInput(
                attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Capacidad Combustible'}),
            'vehi_capacidadpasajeros': forms.TextInput(
                attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Capacidad Pasajeros'}),
            'vehi_capacidadaaforopasajeros': forms.TextInput(
                attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Capacidad Pasajeros Aforo'}),

        }