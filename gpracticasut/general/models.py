from django.db import models

# Create your models here.

class PersonaGeneral(models.Model):
    pege_id = models.BigAutoField(primary_key=True)
    pege_tipopersona = models.IntegerField(null=True,blank=True)
    pege_direccion = models.CharField(max_length=100,null=True,blank=True)
    pege_mail = models.CharField(max_length=50,null=True,blank=True)

    class Meta:
        managed = False
        db_table = '"general"."personageneral"'

    """def __str__(self):
        return self.pege_mail"""