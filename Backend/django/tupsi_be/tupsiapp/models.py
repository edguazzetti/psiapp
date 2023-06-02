from django.db import models
from django.contrib.auth.models import AbstractUser


#Abstract user 
class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=120, unique=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']


# Chequear si estan bien las clases y si concuerdan con el archivo sql del sprint anterior

class Administrador(models.Model):
    dni_administrador = models.IntegerField(unique=True)
    nombre_a = models.CharField(max_length=100)
    apellido_a = models.CharField(max_length=100, null=True)
    email_a = models.CharField(max_length=45, unique=True)
    contrasena_a = models.CharField(max_length=45)
    
    def __str__(self):
        return self.nombre_a


class TiposDeTerapia(models.Model):
    id_t = models.AutoField(primary_key=True)
    nombre_rama = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre_rama


class Ubicacion(models.Model):
    id_u = models.AutoField(primary_key=True)
    provincia = models.CharField(max_length=45)
    localidad = models.CharField(max_length=45)

    def __str__(self):
        return self.provincia


class UsuarioPaciente(models.Model):
    dni_paciente = models.IntegerField(unique=True)
    nombre_p = models.CharField(max_length=100)
    apellido_p = models.CharField(max_length=100, null=True)
    email_p = models.CharField(max_length=45, unique=True)
    contrasena_p = models.CharField(max_length=45)
    provincia_p = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_p


class Profesional(models.Model):
    matricula_pr = models.IntegerField(unique=True)
    nombre_pr = models.CharField(max_length=100)
    apellido_pr = models.CharField(max_length=100)
    email_pr = models.CharField(max_length=45, null=True)
    contrasena_pr = models.CharField(max_length=8)
    provincia_pr = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    localidad_pr = models.CharField(max_length=45)
    tipos_de_terapia_pr = models.ForeignKey(TiposDeTerapia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_pr


class Planes(models.Model):
    id_plan = models.AutoField(primary_key=True)
    precio_plan = models.IntegerField()
    dni_adm_p = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    nombre_plan = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_plan


class PagosSuscripciones(models.Model):
    id_pago = models.AutoField(primary_key=True)
    tipo_pago = models.CharField(max_length=20)
    id_plan_p = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_caducidad = models.DateField()
    dni_pac = models.ForeignKey(UsuarioPaciente, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_pago)
