from django.contrib import admin
from .models import Administrador
from .models import TiposDeTerapia
from .models import Ubicacion
from .models import UsuarioPaciente
from .models import Profesional
from .models import Planes
from .models import PagosSuscripciones

# lo mismo que el comentario de models.py REVISAR
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('dni_administrador', 'nombre_a', 'apellido_a', 'email_a')
    list_filter = ('nombre_a',)
    search_fields = ('nombre_a', 'apellido_a', 'email_a')
    ordering = ('nombre_a',)
    fields = ('dni_administrador', 'nombre_a', 'apellido_a', 'email_a')

admin.site.register(Administrador, AdministradorAdmin)

class TiposDeTerapiaAdmin(admin.ModelAdmin):
    list_display = ('id_t', 'nombre_rama')

admin.site.register(TiposDeTerapia, TiposDeTerapiaAdmin)


class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('id_u', 'provincia', 'localidad')

admin.site.register(Ubicacion, UbicacionAdmin)


class UsuarioPacienteAdmin(admin.ModelAdmin):
    list_display = ('dni_paciente', 'nombre_p', 'apellido_p', 'email_p')
    list_filter = ('nombre_p',)
    search_fields = ('nombre_p', 'apellido_p', 'email_p')
    ordering = ('nombre_p',)
    fields = ('dni_paciente', 'nombre_p', 'apellido_p', 'email_p', 'provincia_p')

admin.site.register(UsuarioPaciente, UsuarioPacienteAdmin)


class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ('matricula_pr', 'nombre_pr', 'apellido_pr', 'email_pr')
    list_filter = ('nombre_pr',)
    search_fields = ('nombre_pr', 'apellido_pr', 'email_pr')
    ordering = ('nombre_pr',)
    fields = ('matricula_pr', 'nombre_pr', 'apellido_pr', 'email_pr', 'provincia_pr', 'localidad_pr', 'tipos_de_terapia_pr')

admin.site.register(Profesional, ProfesionalAdmin)


class PlanesAdmin(admin.ModelAdmin):
    list_display = ('id_plan', 'precio_plan', 'dni_adm_p', 'nombre_plan')

admin.site.register(Planes, PlanesAdmin)


class PagosSuscripcionesAdmin(admin.ModelAdmin):
    list_display = ('id_pago', 'tipo_pago', 'id_plan_p', 'fecha_inicio', 'fecha_caducidad', 'dni_pac')

admin.site.register(PagosSuscripciones, PagosSuscripcionesAdmin)