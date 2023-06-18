from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import status
from rest_framework import permissions
from .models import Paciente, Profesional, Plan, Terapia
from .serializers import (
    PacienteSerializer,
    ProfesionalSerializer,
    PlanSerializer,
    TerapiaSerializer,
    UserSerializer
)

from rest_framework import generics
import logging

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate (email = email , password = password)        
        if user:
            login(request, user)
            return Response(
                UserSerializer(user).data,
                status=status.HTTP_200_OK)
        return Response (status=status.HTTP_404_NOT_FOUND)



logging.basicConfig(level=logging.DEBUG)

# Crear un objeto logger
logger = logging.getLogger(__name__)

class SignPacienteView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        logger.debug('Este es un mensaje de depuración')
        logger.info('Esta es una información útil')
        logger.error('Se produjo un error')
        
        return super().create(request, *args, **kwargs)

class SignProfesionalView(APIView):
    def post(self, request):
        serializer = ProfesionalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registro exitoso"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminPacientesView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        pacientes = Paciente.objects.all()
        serializer = PacienteSerializer(pacientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        paciente = Paciente.objects.get(pk=pk)
        serializer = PacienteSerializer(paciente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        paciente = Paciente.objects.get(pk=pk)
        paciente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdminProfesionalesView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        profesionales = Profesional.objects.all()
        serializer = ProfesionalSerializer(profesionales, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfesionalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        profesional = Profesional.objects.get(pk=pk)
        serializer = ProfesionalSerializer(profesional, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        profesional = Profesional.objects.get(pk=pk)
        profesional.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdminPlanesView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        planes = Plan.objects.all()
        serializer = PlanSerializer(planes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        plan = Plan.objects.get(pk=pk)
        serializer = PlanSerializer(plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        plan = Plan.objects.get(pk=pk)
        plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdminTerapiasView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        terapias = Terapia.objects.all()
        serializer = TerapiaSerializer(terapias, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TerapiaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        terapia = Terapia.objects.get(pk=pk)
        serializer = TerapiaSerializer(terapia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        terapia = Terapia.objects.get(pk=pk)
        terapia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BuscarProfesionalView(APIView):
    def get(self, request):
        # Lógica para buscar profesionales
        # Implementa tu lógica personalizada aquí
        return Response(status=status.HTTP_200_OK)

class VerPerfil(APIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        queryset = Paciente.objects.filter(id=self.request.user.id)
        serializer = PacienteSerializer(queryset, many=True)
        if self.request.user.is_authenticated:
            return Response(serializer.data)


class TerapiasView(APIView):
    queryset = Terapia.objects.all()
    serializer_class = TerapiaSerializer
    http_method_names = ['get']
    permission_classes = [AllowAny]

    def get(self, request):
        terapias = Terapia.objects.all()
        serializer = TerapiaSerializer(terapias, many=True)
        return Response(serializer.data)