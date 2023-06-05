from django.contrib import admin
<<<<<<< HEAD
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .models import Terapia
from .models import Paciente
=======
from .models import Administrador
from .models import TiposDeTerapia
from .models import Ubicacion
from .models import UsuarioPaciente
from .models import Profesional
from .models import Planes
from .models import PagosSuscripciones
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


#para usar el custom user model (p/tener acceso al modelo para editar, crear, borrar usuarios desde admin)
@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    pass
>>>>>>> 6221f347e554122fc1d9a1cce0c7fd1946792b00


class TerapiaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "dni", "id_terapia")

@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(Terapia,TerapiaAdmin)
admin.site.register(Paciente,PacienteAdmin)
