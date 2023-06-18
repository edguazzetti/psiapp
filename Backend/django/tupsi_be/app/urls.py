from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('sign/paciente/', views.SignPacienteView.as_view(), name='sign_paciente'),
    path('sign/profesional/', views.SignProfesionalView.as_view(), name='sign_profesional'),
    path('terapias/', views.TerapiasView.as_view(), name='terapias'),
    path('admin/pacientes/', views.AdminPacientesView.as_view(), name='admin_pacientes'),
    path('admin/profesionales/', views.AdminProfesionalesView.as_view(), name='admin_profesionales'),
    path('admin/planes/', views.AdminPlanesView.as_view(), name='admin_planes'),
    path('admin/terapias/', views.AdminTerapiasView.as_view(), name='admin_terapias'),
    path('buscar/profesional/', views.BuscarProfesionalView.as_view(), name='buscar_profesional'),

]
