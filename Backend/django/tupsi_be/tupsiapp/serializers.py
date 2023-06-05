from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .models import Terapia, Paciente
  

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    username = serializers.CharField(
        required=True)
    password = serializers.CharField(
    min_length=8, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password')
    def validate_password(self, value):
        return make_password(value)
    

class TerapiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terapia
        fields = '__all__'
        #fields = ('nombre', 'descripcion')

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'
        #fields = ('codigodeBarras',"nombre" ,'descripcion','peso','precio','cantidad')