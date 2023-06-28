from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)

class UserManager(BaseUserManager):

    def create_user(self,email,username=None,password=None,**extrafields):
        if not email:
            raise ValueError('Users must have an email')
        user = self.model(username=username,email=self.normalize_email(email), **extrafields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,password,username=None):
        user = self.create_user(email,username,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200,unique=True,null=True)
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Paciente(User):
    lastname = models.CharField(max_length=100)
    localidad = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    sexo = models.CharField(max_length=9)
    dni = models.PositiveIntegerField(unique=True)
    terapiapaciente = models.ForeignKey('Terapia', on_delete=models.SET_NULL, null=True)
    suscripto = models.BooleanField(default=False)
    planactual = models.ForeignKey('Plan', on_delete=models.SET_NULL, null=True)

    class Meta:
        
        db_table = 'paciente'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

class Profesional(User):
    lastname = models.CharField(max_length=100)
    localidad = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    sexo = models.CharField(max_length=9)
    dni = models.PositiveIntegerField(unique=True)
    terapiaprofesional = models.ForeignKey('Terapia', on_delete=models.SET_NULL, null=True)
    matricula = models.BigIntegerField(unique=True)
 

    class Meta:
        db_table = 'profesional'
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'

##############PLAN##############

class Plan(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    precio = models.IntegerField()

    class Meta:
        db_table = 'plan'
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'

    def __str__(self):
        return 'Plan: ' + self.nombre

##############TERAPIA##############

class Terapia(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'terapia'
        verbose_name = 'Terapia'
        verbose_name_plural = 'Terapias'

    def __str__(self):
        return 'Terapia: ' + self.nombre

##############PROVINCIAS##############

class Provincias(models.Model):
    provincia = models.CharField(max_length=255)

    class Meta:
        db_table = 'provincias'
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self):
        return 'Provincia: ' + self.provincia

##############LOCALIDADES##############

class Localidades(models.Model):
    id_provincia = models.ForeignKey(Provincias, on_delete=models.CASCADE)
    localidad = models.CharField(max_length=255)

    class Meta:
        db_table = 'localidad'
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'

    def __str__(self):
        return 'Localidad: ' + self.localidad

