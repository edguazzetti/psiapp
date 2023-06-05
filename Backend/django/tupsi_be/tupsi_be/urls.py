from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.views import LoginView, LogoutView, SignUpPacienteView, ProfileView, ListarUsuarios, agregarPaciente, verPacientes, verTerapias

router = routers.DefaultRouter()
router.register('pacientes', verPacientes, basename='Paciente')
router.register('terapias', verTerapias, basename='Terapia')

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='auth_login'),
    path('auth/logout/', LogoutView.as_view(), name='auth_logout'),
    path('auth/signup/', SignUpPacienteView.as_view(), name='auth_signup'),
    path('user/profile/', ProfileView.as_view(), name='user_profile'),
    path('usuarios/', ListarUsuarios.as_view(), name='listar_usuarios'),
    path('agregarproducto/', agregarPaciente.as_view(), name='agregar_producto'),

    # Agregar las rutas generadas por el router
    path('api/', include(router.urls)),
]

