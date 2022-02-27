from django.db import models

# Create your models here.

class PeriodoUniversidad(models.Model):
    peun_id = models.BigAutoField(primary_key=True)
    peun_ano = models.IntegerField()
    peun_periodo = models.CharField(max_length=15)
    peun_fechainicio = models.DateField()
    peun_fechafin = models.DateField()

    class Meta:
        managed = False
        db_table = '"academico"."periodouniversidad"'

    def __str__(self):
        return self.peun_periodo

class Programa(models.Model):
    prog_id = models.BigAutoField(primary_key=True)
    prog_nombre = models.CharField(max_length=150)
    prog_codigoprograma = models.CharField(max_length=50,null=True,blank=True)
    prog_estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = '"academico"."programa"'

class Unidad(models.Model):
    unid_id = models.BigAutoField(primary_key=True)
    unid_nombre = models.CharField(max_length=100)
    unid_codigo = models.CharField(max_length=40,null=True,blank=True)

    class Meta:
        managed = False
        db_table = '"academico"."unidad"'

class UnidadPrograma(models.Model):
    unpr_id = models.BigAutoField(primary_key=True)
    prog_id = models.ForeignKey(Programa,on_delete=models.CASCADE)
    unid_id = models.ForeignKey(Unidad,on_delete=models.CASCADE)
    unpr_cupominimo = models.IntegerField(null=True,blank=True)
    unpr_cupomaximo = models.IntegerField(null=True,blank=True)

    class Meta:
        managed = False
        db_table = '"academico"."unidadprograma"'

class Materia(models.Model):
    mate_codigomateria = models.CharField(primary_key=True,unique=True,max_length=50)
    mate_nombre = models.CharField(max_length=100)
    mate_capacidad = models.IntegerField(null=True,blank=True)
    mate_horaspracticas = models.IntegerField(null=True,blank=True)
    mate_horasteoricas = models.IntegerField(null=True,blank=True)

    class Meta:
        managed = False
        db_table = '"academico"."materia"'


class PensumMateria(models.Model):
    pens_id =  models.BigAutoField(primary_key=True)
    prog_id = models.ForeignKey(Programa,on_delete=models.CASCADE)
    mate_codigomateria = models.ForeignKey(Materia,on_delete=models.CASCADE)
    pema_periodo = models.IntegerField()
    pema_estado  = models.IntegerField()

    class Meta:
        managed = False
        db_table = '"academico"."pensummateria"'


class Grupo(models.Model):
    grup_id = models.BigAutoField(primary_key=True)
    peun_id = models.ForeignKey(PeriodoUniversidad,on_delete=models.CASCADE,db_column='peun_id')
    mate_codigomateria = models.ForeignKey(Materia,on_delete=models.CASCADE,db_column='mate_codigomateria')
    grup_nombre = models.CharField(max_length=30,null=True,blank=True)

    class Meta:
        managed = False
        db_table = '"academico"."grupo"'


class EstudiantePensum(models.Model):
    estp_id = models.BigAutoField(primary_key=True)


class MatriculaAcademica(models.Model):
    maac_id = models.BigAutoField(primary_key=True)


class MatriculaGrupoPersona(models.Model):
    grup_id = models.BigAutoField(primary_key=True)
    pege_id = models.IntegerField()
    pers_id = models.IntegerField()
    estp_id = models.IntegerField()
    unid_nombre = models.CharField(max_length=100)
    prog_nombre = models.CharField(max_length=150)
    tdoc_abreviatura = models.CharField(max_length=5)
    pers_documentoidentidad = models.CharField(max_length=50)
    pers_primernombre = models.CharField(max_length=50)
    pers_segundonombre = models.CharField(max_length=50,null=True,blank=True)
    pers_primerapellido = models.CharField(max_length=50)
    pers_segundoapellido = models.CharField(max_length=50,null=True,blank=True)

    class Meta:
        managed = False
        db_table = '"academico"."matriculagrupopersona"'