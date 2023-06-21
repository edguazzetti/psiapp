from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUser
from django.utils.translation import gettext as _
from .models import (
    User,
    Paciente,
    Profesional,
    Plan,
    Terapia,
    Provincias,
    Localidades,
)
from core import models

class UserAdmin(BaseUser):
    ordering = ['id']
    list_display = ['id','email','username','name']
    list_display_links = ['id','email']
    fieldsets = (
        (None,{'fields':('username','email','password')}),
        (_('Personal Info'),{'fields': ('name',)}),
        (_('Permissions'),{'fields':('is_active','is_staff','is_superuser')}),
        (_('Imp dates'),{'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('username','email','password1','password2')
        }),
    )

admin.site.register(models.User,UserAdmin)
admin.site.register(Paciente)
admin.site.register(Profesional)
admin.site.register(Plan)
admin.site.register(Terapia)
admin.site.register(Provincias)
admin.site.register(Localidades)