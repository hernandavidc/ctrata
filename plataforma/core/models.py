from django.db import models
from ckeditor.fields import RichTextField
from registration.models import Ciudad

MOTIVO_CHOICES = (
    ('l','Oferta laboral'),
    ('t','Turismo'),
    ('a','Oferta academica'),
    ('s','Relación sentimental'),
)

class Pregunta(models.Model):
    cont = models.TextField(verbose_name="Descripción de la forma de captación", null=None, blank=None)
    motivo = models.CharField(choices=MOTIVO_CHOICES, max_length=1)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    def __str__(self):
        return str(self.id)+ " " + self.cont + " " + self.motivo

class PerfilPersona(models.Model):
    nombreCompleto = models.CharField(verbose_name="Nombre completo", max_length=200)
    dni = models.PositiveIntegerField()
    edad = models.SmallIntegerField(verbose_name='Edad')
    lugarOrigen =  models.TextField(verbose_name='Lugar de origen')
    estratoSocioeconomico = models.SmallIntegerField(verbose_name="Estrato socioeconómico", default=0)
    lugarDestino =  models.TextField(verbose_name='Lugar de destino')
    motivoViaje = models.CharField(verbose_name="Motivo del viaje",choices=MOTIVO_CHOICES, max_length=1)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

GENERO_CHOICES = (
		('m', 'Masculino'), 
		('f', 'Femenino'), 
	)

TIPOTRATA_CHOICES = (
		('i', 'Interna'), 
		('e', 'Externa'), 
	)

FINALIDAD_CHOICES = (
    ('ex', 'Explotación de la prostitución ajena u otras formas de Explotación sexual'),
    ('tr','Trabajos o servicios forzosos'),
    ('me','Mendicidad ajena'),
    ('ma','Matrimonio servil'),
    ('or','Extracción de órganos'),
    ('es','Practicas análogas a la esclavitud'),
    ('se','Servidumbre'),
    ('no','No se concretó'),
    ('ot','Otro'),
)

MEDIOCONTACTO_CHOICES = (
    ('re','Redes sociales'),
    ('cl','Clasificados'),
    ('ra','Radio'),
    ('am','Amigo(a)'),
    ('pr','Pareja'),
    ('ot','Otro'),
)

FORMA_CHOICES = (
    ('ol','Oferta laboral'),
    ('re','Relación sentimental'),
    ('oa','Oferta académica'),
    ('tu','Turismo'),
    ('ot','Otro'),
)

MEDIOTRANS_CHOICES = (
    ('a','Avión'),
    ('b','Bus'),
    ('m','Maritimo'),
    ('o','Otro'),
)

class Caso(models.Model):
    fecha = models.DateField(verbose_name="Fecha Reporte de caso")
    genero = models.CharField(choices=GENERO_CHOICES, max_length=1)
    edad = models.SmallIntegerField(verbose_name="Edad")
    finalidadExplotación = 	models.CharField(choices=FINALIDAD_CHOICES,max_length=2 ,verbose_name='Finalidad de explotación')
    estratoSocioeconomico = models.SmallIntegerField(verbose_name="Estrato socioeconómico", default=0)
    medioContacto = models.CharField(choices=MEDIOCONTACTO_CHOICES,max_length=2 ,verbose_name='Medio de contacto')
    formaCaptación = models.CharField(choices=FORMA_CHOICES,max_length=2 ,verbose_name='Forma de captación')
    tipoTrata = models.CharField(verbose_name="Tipo de trata",choices=TIPOTRATA_CHOICES, max_length=1)
    descriptFormaCap = RichTextField(verbose_name="Descripción de la forma de captación", null=True, blank=True)
    lugarExplotación = models.ManyToManyField(Ciudad, related_name="get_ciudades")
    medioTransporte = models.CharField(verbose_name="Medio de transporte utilizado", choices=MEDIOTRANS_CHOICES, max_length=1)
    rutaTraslado = models.CharField(verbose_name="Ruta de traslado de la presunta víctima", max_length=200)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
