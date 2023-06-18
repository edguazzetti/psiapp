from django.contrib import admin
from .models import Administrador, CustomUser, Paciente, Profesional, Plan, Terapia, Provincias, Localidades

admin.site.register(Administrador)
admin.site.register(CustomUser)
admin.site.register(Paciente)
admin.site.register(Profesional)
admin.site.register(Plan)
admin.site.register(Terapia)
admin.site.register(Provincias)
admin.site.register(Localidades)
