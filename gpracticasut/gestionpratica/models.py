from django.db import models

# Create your models here.
from academicoglobal.models import Persona
from academico.models import Grupo,Programa,PeriodoUniversidad,Materia
from general.models import PersonaGeneral
from gestionflota.models import Vehiculos


VEHICULOPR_CHOICES = (
    ('PROPIO','PROPIO'),
    ('CONTRATADO','CONTRATADO'),
)

ACTIVO_CHOICES = (
    (1,'SÍ'),
    (0,'N0'),
)
class GrupoIntegrante(models.Model):
    grin_id = models.BigAutoField(primary_key=True)
    grin_nombre = models.CharField(max_length=300)
    grin_descripcion = models.TextField(null=True, blank=True)
    grin_registradopor = models.CharField(max_length=30, null=True, blank=True)
    grin_fecharegistro = models.DateTimeField(auto_now_add=True)
    grin_fechacambio = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = '"gpracticasut"."grupointegrante"'

    def __str__(self):
        return self.grin_nombre

class TipoIntegrante(models.Model):
    tiin_id = models.BigAutoField(primary_key=True)
    grin_id = models.ForeignKey(GrupoIntegrante,on_delete=models.CASCADE,db_column='grin_id')
    tiin_nombre = models.CharField(max_length=300)
    tiin_descripcion = models.TextField(null=True,blank=True)
    tiin_registradopor = models.CharField(max_length=30, null=True, blank=True)
    tiin_fecharegistro = models.DateTimeField(auto_now_add=True)
    tiin_fechacambio = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = '"gpracticasut"."tipointegrante"'

    def __str__(self):
        return self.tiin_nombre

class ConceptosPraticas(models.Model):
    copr_id = models.BigAutoField(primary_key=True)
    copr_nombre = models.CharField(max_length=300)
    copr_descripcion = models.TextField(null=True,blank=True)
    copr_requierebase = models.IntegerField(default=0)
    copr_valorbase = models.FloatField(null=True,blank=True)
    copr_estado = models.IntegerField(default=1,null=True,blank=True)
    copr_registradopor = models.CharField(max_length=30, null=True, blank=True)
    copr_fecharegistro = models.DateTimeField(auto_now_add=True)
    copr_fechacambio = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = '"gpracticasut"."conceptopracticas"'

    def __str__(self):
        return self.copr_nombre


class LugaresPraticas(models.Model):
    lupr_id = models.BigAutoField(primary_key=True)
    lupr_codigo = models.CharField(max_length=20,null=True,blank=True)
    lupr_nombre = models.CharField(max_length=300)
    lupr_description = models.TextField(null=True,blank=True)
    lupr_estado = models.BooleanField(default=True)
    lupr_registradopor = models.CharField(max_length=30, null=True, blank=True)
    lupr_fecharegistro = models.DateTimeField(auto_now_add=True)
    lupr_fechacambio = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = '"gpracticasut"."lugarespracticas"'

    def __str__(self):
        return self.lupr_nombre


class SolictudPratica(models.Model):
    solp_id = models.BigAutoField(primary_key=True)
    solp_nombre = models.CharField(max_length=300)
    solp_description = models.TextField(null=True, blank=True)
    solp_anio = models.CharField(max_length=4, null=True, blank=True)
    peun_id = models.ForeignKey(PeriodoUniversidad, on_delete=models.CASCADE,db_column='peun_id')
    solp_ayudaeconomica = models.IntegerField(null=True, blank=True, choices=ACTIVO_CHOICES)
    solp_idayregreso = models.IntegerField(null=True, blank=True, choices=ACTIVO_CHOICES)
    solp_liqviaticos = models.IntegerField(null=True, blank=True, choices=ACTIVO_CHOICES)
    solp_numerodias = models.PositiveIntegerField(null=True, blank=True)
    solp_numerodocentes = models.PositiveIntegerField(null=True, blank=True)
    solp_numeroestudiantes = models.PositiveIntegerField(null=True, blank=True)
    solp_numeroconductores = models.PositiveIntegerField(null=True, blank=True)
    solp_fechainiciopractica = models.DateTimeField(null=True, blank=True)
    solp_fechafinpractica = models.DateTimeField(null=True, blank=True)
    solp_duraciondoc = models.FloatField(null=True, blank=True)
    solp_cvehiculopractica = models.CharField(max_length=50, null=True, blank=True, choices=VEHICULOPR_CHOICES)
    solp_costototalpractica = models.FloatField(null=True, blank=True)
    solp_estado = models.IntegerField(default=1)
    solp_registradopor = models.CharField(max_length=30, null=True, blank=True)
    solp_fecharegistro = models.DateTimeField(auto_now_add=True)
    solp_fechacambio = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = '"gpracticasut"."solicitudpracticas"'

    def __str__(self):
        return self.solp_nombre

class VhiculosPracticas(models.Model):
    vepr_id = models.BigAutoField(primary_key=True)
    vehi_id = models.ForeignKey(Vehiculos,on_delete=models.CASCADE,db_column='vehi_id')
    solp_id = models.ForeignKey(SolictudPratica,on_delete=models.CASCADE,db_column='solp_id')
    vepr_registradopor = models.CharField(max_length=30, null=True, blank=True)
    vepr_fecharegistro = models.DateTimeField(auto_now_add=True)
    vepr_fechacambio = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = '"gpracticasut"."vehiculopracticas"'

    """def __str__(self):
        return self.solp_nombre"""

class MateriasPracticas(models.Model):
    mapr_id = models.BigAutoField(primary_key=True)
    solp_id = models.ForeignKey(SolictudPratica, on_delete=models.CASCADE, db_column='solp_id')
    mate_codigomateria = models.ForeignKey(Materia,on_delete=models.CASCADE,db_column='mate_codigomateria')
    #grup_id = models.ForeignKey(Grupo,on_delete=models.CASCADE)
    mapr_registradopor = models.CharField(max_length=30, null=True, blank=True)
    mapr_fecharegistro = models.DateTimeField(auto_now_add=True)
    mapr_fechacambio = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = '"gpracticasut"."materiaspracticas"'


class PersonaIntegrante(models.Model):
    pein_id = models.BigAutoField(primary_key=True)
    solp_id = models.ForeignKey(SolictudPratica,on_delete=models.CASCADE,db_column='solp_id')
    tiin_id = models.ForeignKey(TipoIntegrante,on_delete=models.CASCADE,db_column='tiin_id')
    pers_id = models.ForeignKey(Persona,on_delete=models.CASCADE,db_column='pers_id')
    pege_id = models.ForeignKey(PersonaGeneral, on_delete=models.CASCADE,db_column='pege_id')
    grup_id = models.ForeignKey(Grupo,on_delete=models.CASCADE,null=True,blank=True, db_column='grup_id')
    mapr_id = models.ForeignKey(MateriasPracticas,on_delete=models.CASCADE,null=True,blank=True,db_column='mapr_id')
    pein_registradopor = models.CharField(max_length=30, null=True, blank=True)
    pein_fecharegistro = models.DateTimeField(auto_now_add=True)
    pein_fechacambio = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('pege_id', 'solp_id')
        db_table = '"gpracticasut"."personaintegrante"'


class CostosPraticas(models.Model):
    ctpr_id = models.BigAutoField(primary_key=True)
    solp_id = models.ForeignKey(SolictudPratica,on_delete=models.CASCADE,db_column='solp_id')
    copr_id = models.ForeignKey(ConceptosPraticas,on_delete=models.CASCADE,db_column='copr_id')
    ctpr_cantidad = models.IntegerField()
    ctpr_costounitario = models.FloatField()
    ctpr_costototalxconcepto = models.FloatField(null=True,blank=True) #CTPR_COSTOTOTALXCONCEPTO
    ctpr_registradopor = models.CharField(max_length=30, null=True, blank=True)
    ctpr_fecharegistro = models.DateTimeField(auto_now_add=True)
    ctpr_fechacambio = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        #unique_together = ('pege_id', 'solp_id')
        db_table = '"gpracticasut"."costopracticas"'


class CostoPracticaPersona(models.Model):
    cpxp_id = models.BigAutoField(primary_key=True)
    solp_id = models.ForeignKey(SolictudPratica, on_delete=models.CASCADE,db_column='solp_id')
    pein_id = models.ForeignKey(PersonaIntegrante,on_delete=models.CASCADE,db_column='pein_id')
    copr_id = models.ForeignKey(ConceptosPraticas, on_delete=models.CASCADE,db_column='copr_id')
    cpxp_costounitario = models.FloatField()
    cpxp_unidadfactor = models.FloatField(null=True,blank=True)
    cpxp_unidadmedida = models.CharField(max_length=50,null=True,blank=True)
    cpxp_costototalconceptopersona = models.FloatField(null=True, blank=True)
    cpxp_registradopor = models.CharField(max_length=30, null=True, blank=True)
    cpxp_fecharegistro = models.DateTimeField(auto_now_add=True)
    cpxp_fechacambio = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = '"gpracticasut"."costopracticapersona"'

    """def __str__(self):
        return self.solp_nombre"""


class RutasPractica(models.Model):
    rupr_id = models.BigAutoField(primary_key=True)
    solp_id = models.ForeignKey(SolictudPratica, on_delete=models.CASCADE, db_column='solp_id')
    lupr_id = models.ForeignKey(LugaresPraticas,on_delete=models.CASCADE,db_column='lupr_id')
    rupr_descripcion = models.TextField(null=True, blank=True)
    rupr_registradopor = models.CharField(max_length=30, null=True, blank=True)
    rupr_fecharegistro = models.DateTimeField(auto_now_add=True)
    rupr_fechacambio = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = '"gpracticasut"."rutaspracticas"'


