from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Textarea
from django.utils import timezone
import datetime
from .models import GrupoIntegrante,TipoIntegrante,ConceptosPraticas,LugaresPraticas,SolictudPratica,VhiculosPracticas,\
    PersonaIntegrante,RutasPractica,MateriasPracticas,CostosPraticas
from academico.models import PeriodoUniversidad

CHOICES = [('1', 'SI'), ('0', 'NO')]
class GrupoIntegranteForm(forms.ModelForm):
    class Meta:
        model = GrupoIntegrante
        fields =[
            'grin_nombre',
            'grin_descripcion',
        ]
        labels = {
            'grin_nombre': 'Grupo Integrante',
            'grin_descripcion': 'Descripción',
        }
        help_texts = {
            'grin_nombre': 'Ingrese Grupo',
            'mveh_descripcion': 'Ingrese Descripción',
        }
        widgets = {
            'grin_nombre': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Grupo Integrante'}),
            'grin_descripcion': forms.Textarea(attrs={'class': 'form-control','rows': 5,'cols': 20,'placeholder': 'Ingrese Descipción'}),
        }

class TipoIntegranteForm(forms.ModelForm):
    class Meta:
        model = TipoIntegrante
        fields =[
            'grin_id',
            'tiin_nombre',
            'tiin_descripcion',
        ]
        labels = {
            'grin_id': 'Grupo Integrante',
            'tiin_nombre': 'Nombre',
            'tiin_descripcion': 'Descripción',
        }
        help_texts = {
            'grin_id': 'Ingrese Grupo',
            'tiin_nombre': 'Ingrese Nombre',
            'tiin_descripcion': 'Ingrese Descripción',
        }
        widgets = {
            'grin_id': forms.Select(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Grupo Tipo Integrante'}),
            'tiin_nombre': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Tipo Integrante'}),
            'tiin_descripcion': forms.Textarea(attrs={'class': 'form-control','rows': 5,'cols': 20,'placeholder': 'Ingrese Descipción'}),
        }

class LugaresPraticasForm(forms.ModelForm):
    class Meta:
        model = LugaresPraticas
        fields =[
            'lupr_codigo',
            'lupr_nombre',
            'lupr_estado',
        ]
        labels = {
            'lupr_codigo': 'Codigo',
            'lupr_nombre': 'Nombre',
            'lupr_estado': 'Estado',
        }
        help_texts = {
            'lupr_codigo': 'Ingrese Codigo',
            'lupr_nombre': 'Ingrese Lugar',
            'lupr_estado': 'Estado',
        }
        widgets = {
            'lupr_codigo': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Codigo Lugar'}),
            'lupr_nombre': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Ingrese Lugar'}),
            #'lupr_estado': forms.Textarea(attrs={'class': 'form-control','rows': 5,'cols': 20,'placeholder': 'Estado'}),
        }

class SolictudPraticaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SolictudPraticaForm, self).__init__(*args, **kwargs)
        date = datetime.date.today()
        print('fecha file form : ', date)
        year = date.strftime("%Y")
        #depar = DepartamentoGeneral.objects.values_list('dege_id', flat=True).filter(page_id='CO')
        self.fields['peun_id'].queryset = PeriodoUniversidad.objects.filter(peun_ano=year)
        self.fields['solp_anio'].initial=year


    class Meta:
        model = SolictudPratica
        fields =[
            'solp_nombre',
            'solp_anio',
            'peun_id',
            'solp_numerodias',
            'solp_fechainiciopractica',
            'solp_fechafinpractica',
            'solp_liqviaticos',
            'solp_idayregreso',
            'solp_ayudaeconomica',
        ]
        labels = {
            'solp_nombre': 'Nombre',
            'solp_anio': 'Año',
            'peun_id': 'Periodo',
            'solp_numerodias': 'Número de Días',
            'solp_fechainiciopractica': 'Fecha Salida',
            'solp_fechafinpractica': 'Fecha Llegada',
            'solp_liqviaticos': 'Liquidacion de Viaticos',
            'solp_idayregreso': 'Ida y Regreso',
            'solp_ayudaeconomica': 'Ayuda Económica',
        }
        help_texts = {
            'solp_nombre': 'Nombre',
            'solp_anio': 'Año',
            'peun_id': 'Periodo',
            'solp_numerodias': 'Numero de Días',
            'solp_fechainiciopractica': 'Fecha Salida',
            'solp_fechafinpractica': 'Fecha Llegada',
            'solp_liqviaticos': 'solp_liqviaticos',
            'solp_idayregreso': 'Ida y Regreso',
            'solp_ayudaeconomica': 'Ayuda Económica',
        }
        widgets = {
            'solp_nombre': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Nombre'}),
            'solp_anio': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Año','readonly':'readonly'}),
            'peun_id': forms.Select(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Periodo'}),
            'solp_numerodias': forms.TextInput(attrs={'class': 'form-control','rows': 5,'cols': 20,'placeholder': 'Numero Días'}),
            'solp_liqviaticos': forms.Select(attrs={'class': 'form-control', 'rows': 5, 'cols': 20, 'placeholder': 'Viaticos'}),
            'solp_idayregreso': forms.Select(attrs={'class': 'form-control', 'rows': 5, 'cols': 20, 'placeholder': 'ida'}),
            'solp_ayudaeconomica': forms.Select(attrs={'class': 'form-control', 'rows': 5, 'cols': 20, 'placeholder': 'Ayuda eco'}),
            'solp_fechainiciopractica': forms.TextInput(attrs={'class': 'form-control', 'rows': 5, 'cols': 20, 'placeholder': 'Fecha Salida'}),
            'solp_fechafinpractica': forms.TextInput(attrs={'class': 'form-control', 'rows': 5, 'cols': 20, 'placeholder': 'Fecha Llegada'}),
        }

class SolictudPraticaGesVehicleForm(forms.ModelForm):
    class Meta:
        model = SolictudPratica
        fields =[
            'solp_cvehiculopractica'
        ]
        labels = {
            'solp_cvehiculopractica': 'Ges Vehiculo'
        }
        help_texts = {
            'solp_cvehiculopractica': 'Ges Vehiculo'
        }
        widgets = {
            'solp_cvehiculopractica': forms.Select(attrs={'class': 'form-control', 'rows': 5, 'cols': 20, 'placeholder': 'Ges Vehiculo'})
        }

class VhiculosPracticasForm(forms.ModelForm):
    class Meta:
        model = VhiculosPracticas
        fields =[
            'vehi_id',
            'solp_id'
        ]
        labels = {
            'vehi_id': 'Vehiculo',
        }
        help_texts = {
            'vehi_id': 'Seleccionar Vehiculo',
        }
        widgets = {
            'vehi_id': forms.Select(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Vehiculo'}),
        }

class PersonaIntegranteDocenteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonaIntegranteDocenteForm, self).__init__(*args, **kwargs)
        #depar = DepartamentoGeneral.objects.values_list('dege_id', flat=True).filter(page_id='CO')
        grupopersona = GrupoIntegrante.objects.filter(grin_nombre='DOCENTES').first()
        self.fields['tiin_id'].queryset = TipoIntegrante.objects.filter(grin_id = grupopersona.grin_id)
    class Meta:
        model = PersonaIntegrante
        fields =[
            'solp_id',
            'tiin_id',
            'pers_id',
            'pege_id',
        ]
        labels = {
            'tiin_id': 'Tipo Integrante',
            #'grin_descripcion': 'Descripción',
        }
        help_texts = {
            'tiin_id': 'Seleccione Tipo Integrante',
            #'mveh_descripcion': 'Ingrese Descripción',
        }
        widgets = {
            'tiin_id': forms.Select(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Tipo Integrante'}),
            'pers_id': forms.TextInput(
                attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Tipo Integrante'}),
            #'grin_descripcion': forms.Textarea(attrs={'class': 'form-control','rows': 5,'cols': 20,'placeholder': 'Ingrese Descipción'}),
        }

class AuxiliarPracticaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AuxiliarPracticaForm, self).__init__(*args, **kwargs)
        #depar = DepartamentoGeneral.objects.values_list('dege_id', flat=True).filter(page_id='CO')
        grupopersona = GrupoIntegrante.objects.filter(grin_nombre='AUXILIARES LAB. PRACTICAS').first()
        self.fields['tiin_id'].queryset = TipoIntegrante.objects.filter(grin_id = grupopersona.grin_id)
    class Meta:
        model = PersonaIntegrante
        fields =[
            'solp_id',
            'tiin_id',
            'pers_id',
            'pege_id',
        ]
        labels = {
            'tiin_id': 'Tipo Integrante',
            #'grin_descripcion': 'Descripción',
        }
        help_texts = {
            'tiin_id': 'Seleccione Tipo Integrante',
            #'mveh_descripcion': 'Ingrese Descripción',
        }
        widgets = {
            'tiin_id': forms.Select(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Tipo Integrante'}),
            'pers_id': forms.TextInput(
                attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Tipo Integrante'}),
            #'grin_descripcion': forms.Textarea(attrs={'class': 'form-control','rows': 5,'cols': 20,'placeholder': 'Ingrese Descipción'}),
        }

class PersonaIntegranteConductorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonaIntegranteConductorForm, self).__init__(*args, **kwargs)
        #depar = DepartamentoGeneral.objects.values_list('dege_id', flat=True).filter(page_id='CO')
        grupopersona = GrupoIntegrante.objects.filter(grin_nombre='CONDUCTORES').first()
        self.fields['tiin_id'].queryset = TipoIntegrante.objects.filter(grin_id = grupopersona.grin_id)
    class Meta:
        model = PersonaIntegrante
        fields =[
            'solp_id',
            'tiin_id',
            'pers_id',
            'pege_id',
        ]
        labels = {
            'tiin_id': 'Tipo Integrante',
            #'grin_descripcion': 'Descripción',
        }
        help_texts = {
            'tiin_id': 'Seleccione Tipo Integrante',
            #'mveh_descripcion': 'Ingrese Descripción',
        }
        widgets = {
            'tiin_id': forms.Select(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Tipo Integrante'}),
            'pers_id': forms.TextInput(
                attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Tipo Integrante'}),
            #'grin_descripcion': forms.Textarea(attrs={'class': 'form-control','rows': 5,'cols': 20,'placeholder': 'Ingrese Descipción'}),
        }

class RutasPracticaForm(forms.ModelForm):
    class Meta:
        model = RutasPractica
        fields =[
            'solp_id',
            'lupr_id',
            'rupr_descripcion',
        ]
        labels = {
            'lupr_id': 'Ruta',
            'rupr_descripcion': 'Descripción',
        }
        help_texts = {
            'lupr_id': 'Seleccione Ruta',
            'rupr_descripcion': 'Ingrese Descripción',
        }
        widgets = {
            'lupr_id': forms.Select(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Ruta'}),
            'rupr_descripcion': forms.Textarea(attrs={'class': 'form-control','rows': 5,'cols': 20,'placeholder': 'Ingrese Descipción'}),
        }

class MateriasPracticasForm(forms.ModelForm):
    class Meta:
        model = MateriasPracticas
        fields =[
            'solp_id',
            'mate_codigomateria',
        ]
        """labels = {
            'lupr_id': 'Ruta',
            'rupr_descripcion': 'Descripción',
        }
        help_texts = {
            'lupr_id': 'Seleccione Ruta',
            'rupr_descripcion': 'Ingrese Descripción',
        }
        widgets = {
            'lupr_id': forms.Select(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Ruta'}),
            'rupr_descripcion': forms.Textarea(attrs={'class': 'form-control','rows': 5,'cols': 20,'placeholder': 'Ingrese Descipción'}),
        }"""

class CostosPraticasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CostosPraticasForm, self).__init__(*args, **kwargs)
        #depar = DepartamentoGeneral.objects.values_list('dege_id', flat=True).filter(page_id='CO')
        #grupopersona = GrupoIntegrante.objects.filter(grin_nombre='CONDUCTORES').first()
        self.fields['copr_id'].queryset = ConceptosPraticas.objects.filter(copr_requierebase = 0)
    class Meta:
        model = CostosPraticas
        fields =[
            'solp_id',
            'copr_id',
            'ctpr_cantidad',
            'ctpr_costounitario',
        ]
        labels = {
            'copr_id': 'Concepto',
            'ctpr_cantidad': 'Cantidad',
            'ctpr_costounitario': 'Valor Unitario',
        }
        help_texts = {
            'copr_id': 'Seleccione Concepto',
            'ctpr_cantidad': 'Ingrese Cantidad',
            'ctpr_costounitario': 'Ingrese Valor Unitario',
        }
        widgets = {
            'copr_id': forms.Select(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Selecciones Concepto'}),
            'ctpr_cantidad': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Ingrese Cantidad'}),
            'ctpr_costounitario': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus',  'placeholder': 'Ingrese Valor Unitario'}),
        }