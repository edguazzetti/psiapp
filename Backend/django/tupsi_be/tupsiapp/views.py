from django.contrib.auth import authenticate, login, logout
from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from app.models import Terapia, Paciente, CustomUser
from .serializers import UserSerializer
from .serializers import PacienteSerializer
from .serializers import TerapiaSerializer
from .serializers import UserSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)

        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        
        # Si no es correcto devolvemos un error en la petición
        return Response(
            {"error": "Credenciales inválidas"},
            status=status.HTTP_400_BAD_REQUEST
        )

class LogoutView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        # Recuperamos al usuario autenticado antes de llamar a logout()
        user = request.user

        # Borramos de la request la información de sesión
        logout(request)

        # Devolvemos la respuesta al cliente con los datos del usuario
        return Response(
            UserSerializer(user).data,
            status=status.HTTP_200_OK)

    
class SignUpPacienteView(generics.CreateAPIView):
    serializer_class = UserSerializer

class verPacientes(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny] 
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class agregarPaciente(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, format=None):
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class verTerapias(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Terapia.objects.all()
    serializer_class = TerapiaSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated] #permiso para usuarios logueados
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch']
    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user
        
class ListarUsuarios(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']
    permission_classes = [IsAdminUser]
    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        if self.request.user.is_authenticated:
            return Response(serializer.data)