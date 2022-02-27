from django.db import models

# Create your models here.
TIPOCOMBUSTIBLE_CHOICES = (
    ('GASOLINA','GASOLINA'),
    ('ACPM','ACPM'),
)

class MarcaVehiculos(models.Model):
    mveh_id = models.BigAutoField(primary_key=True)
    mveh_nombre = models.CharField(max_length=100)
    mveh_descripcion = models.TextField(null=True,blank=True,db_column='MVEH_DESCRIPTION')
    mveh_registradopor = models.CharField(max_length=30,null=True,blank=True)
    mveh_fecharegistro = models.DateTimeField(auto_now_add=True)
    mveh_fechacambio = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = '"gpracticasut"."marcavehiculos"'

    def __str__(self):
        return self.mveh_nombre

class TipoVehiculo(models.Model):
    tveh_id = models.BigAutoField(primary_key=True)
    tveh_nombre = models.CharField(max_length=100)
    tveh_descripcion = models.TextField(null=True, blank=True)
    tveh_registradopor = models.CharField(max_length=30, null=True, blank=True)
    tveh_fecharegistro = models.DateTimeField(auto_now_add=True)
    tveh_fechacambio = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = '"gpracticasut"."tipovehiculo"'

    def __str__(self):
        return self.tveh_nombre


class Vehiculos(models.Model):
    vehi_id = models.BigAutoField(primary_key=True)
    vehi_placa = models.CharField(max_length=10)
    mveh_id = models.ForeignKey(MarcaVehiculos,on_delete=models.CASCADE,db_column='mveh_id')
    tveh_id = models.ForeignKey(TipoVehiculo,on_delete=models.CASCADE,db_column='tveh_id')
    vehi_transporte = models.CharField(max_length=50,null=True,blank=True)
    vehi_combustible = models.CharField(max_length=20, choices=TIPOCOMBUSTIBLE_CHOICES)
    vehi_capacidadcombustible = models.IntegerField(null=True,blank=True)
    vehi_capacidadpasajeros = models.IntegerField()
    vehi_capacidadaaforopasajeros = models.IntegerField(null=True,blank=True)
    vehi_registradopor = models.CharField(max_length=30, null=True, blank=True)
    vehi_fecharegistro = models.DateTimeField(auto_now_add=True)
    vehi_fechacambio = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = '"gpracticasut"."vehiculos"'

    def __str__(self):
        return self.vehi_placa

