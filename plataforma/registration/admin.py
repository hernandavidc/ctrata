from django.contrib import admin
from .models import Pais, Ciudad, Profile

class ProfileAdmin(admin.ModelAdmin):
    readonly_fields= ('user',)

class PaisAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

class CiudadAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

admin.site.register(Pais, PaisAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Profile, ProfileAdmin)