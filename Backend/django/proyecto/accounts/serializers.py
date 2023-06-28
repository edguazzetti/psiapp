from typing import Tuple
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework import serializers
from core.models  import Paciente, Profesional, Plan, Terapia, Provincias, Localidades
from django.contrib.auth.models import Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields =('email','username','password','name')
        extra_kwargs = {'password':{'write_only':True,'min_length':8}}

    def create(self,validated_data):
        return get_user_model().objects.create_user(**validated_data)

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type':'password'},
        trim_whitespace = False
    )
    def validate(self,attrs):
        email = attrs.get('email')
        password = attrs.get('password')

         # Imprimir los valores de email y password
        print(f"Email: {email}")
        print(f"Password: {password}")

        user = authenticate(
            request=self.context.get('request'),
            email=email,
            password=password
        )
        if not user:
            raise serializers.ValidationError("falla la validacion")
        attrs['user'] =user
        return attrs
    
class ProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesional
        fields = ('email', 'username', 'password', 'name', 'lastname', 'localidad', 'provincia', 'sexo', 'dni', 'terapiaprofesional', 'matricula')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        profesional = Profesional(**validated_data)
        profesional.set_password(password)
        profesional.save()
        return profesional

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('email', 'username', 'password', 'name', 'lastname', 'localidad', 'provincia', 'sexo', 'dni', 'terapiapaciente')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        paciente = Paciente(**validated_data)
        paciente.set_password(password)
        paciente.save()
        group = Group.objects.get(name='grupofull')  # Obtén el grupo de permisos de pacientes
        paciente.groups.add(group)  # Asigna el grupo al paciente
        return paciente

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
