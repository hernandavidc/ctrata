from django.contrib import admin
from .models import Caso, Pregunta, PerfilPersona

class CasoAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

class PreguntaAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

class PerfilPersonaAdmin(admin.ModelAdmin):
    readonly_fields= ('edad','lugarOrigen','lugarDestino','motivoViaje','estratoSocioeconomico','created', 'updated')

admin.site.register(Caso, CasoAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(PerfilPersona, PerfilPersonaAdmin)
