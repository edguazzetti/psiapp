from rest_framework import generics
from .serializers import UserSerializer,AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfesionalSerializer, PacienteSerializer, PlanSerializer, TerapiaSerializer, ProvinciasSerializer, LocalidadesSerializer
from core.models import Provincias, Profesional, Paciente, Plan, Terapia, Localidades
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class LoginView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'user_id': user.id,
            'email': user.email,
            'name': user.name
        })


class PacienteCreateView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfesionalCreateView(APIView):
    def post(self, request):
        serializer = ProfesionalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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


##############BUSCAR PROFESIONALES##############

class BuscarProfesionalView(APIView):
    def get(self, request):
        profesionales = Profesional.objects.all()
        serializer = ProfesionalSerializer(profesionales, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


##############VER PERFIL DE USUARIO LOGUEADO##############
class PacienteDetailView(generics.RetrieveAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ProfesionalDetailView(generics.RetrieveAPIView):
    queryset = Profesional.objects.all()
    serializer_class = ProfesionalSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


#############ENDPOINT PARA MOSTRAR TERAPIAS REGISTRADAS##############

class TerapiasView(APIView):
    queryset = Terapia.objects.all()
    serializer_class = TerapiaSerializer
    http_method_names = ['get']
    permission_classes = [AllowAny]

    def get(self, request):
        terapias = Terapia.objects.all()
        serializer = TerapiaSerializer(terapias, many=True)
        return Response(serializer.data)


#############ENDPOINT PARA MOSTRAR PROVINCIAS REGISTRADAS##############

class ProvinciasView(APIView):
    queryset = Provincias.objects.all()
    serializer_class = ProvinciasSerializer
    http_method_names = ['get']
    permission_classes = [AllowAny]

    def get(self, request):
        provincias = Provincias.objects.all()
        serializer = ProvinciasSerializer(provincias, many=True)
        return Response(serializer.data)


#############ENDPOINT PARA MOSTRAR LOCALIDADES REGISTRADAS##############
class LocalidadesView(APIView):
    queryset = Localidades.objects.all()
    serializer_class = LocalidadesSerializer
    http_method_names = ['get']
    permission_classes = [AllowAny]

    def get(self, request):
        localidades = Localidades.objects.all()
        serializer = LocalidadesSerializer(localidades, many=True)
        return Response(serializer.data)


#############ENDPOINT PARA MOSTRAR PLANES REGISTRADAS##############

class PlanListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        planes = Plan.objects.all()
        serializer = PlanSerializer(planes, many=True)
        return Response(serializer.data)
