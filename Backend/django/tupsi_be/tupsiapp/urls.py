from django.urls import path, include
from .views import LoginView, LogoutView, SignUpPacienteView, ProfileView, ListarUsuarios, agregarPaciente

urlpatterns = [
    # Auth views
    path('api/auth/login/', LoginView.as_view(), name='auth_login'),
    path('api/auth/reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/auth/logout/', LogoutView.as_view(), name='auth_logout'),
    path('api/auth/signup/', SignUpPacienteView.as_view(), name='auth_signup'),

    path('api/user/profile/', ProfileView.as_view(), name='user_profile'),
    path('api/usuarios/', ListarUsuarios.as_view(), name='listar_usuarios'),
    path('api/agregarproducto/', agregarPaciente.as_view(), name='agregar_producto'),
]
