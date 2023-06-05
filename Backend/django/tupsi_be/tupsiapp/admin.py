from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .models import Terapia
from .models import Paciente


class TerapiaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "dni", "id_terapia")

@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(Terapia,TerapiaAdmin)
admin.site.register(Paciente,PacienteAdmin)
