from rest_framework import serializers
from .models import Administrador, Paciente, Profesional, Plan, Terapia, Provincias, Localidades
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    username = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8 , write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password')
    
    def validate_password(self, value):
        return make_password(value)
    
class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = '__all__'


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'


class ProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesional
        fields = '__all__'


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class TerapiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terapia
        fields = '__all__'


class ProvinciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincias
        fields = '__all__'


class LocalidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localidades
        fields = '__all__'


