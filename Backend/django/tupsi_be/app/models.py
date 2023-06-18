from django.db import models
from django.contrib.auth.models import AbstractUser

class Administrador(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='administrador_set',
        related_query_name='administrador',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='administrador_set',
        related_query_name='administrador',
    )

    # Heredar del modelo AbstractUser para aprovechar su funcionalidad
    pass

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=150, default="", unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_set',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',
        related_query_name='customuser',
    )

    class Meta:
        verbose_name_plural = 'Custom Users'

class Paciente(models.Model):
    username = models.CharField(max_length=150, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.PositiveIntegerField(unique=True)
    sexo = models.CharField(max_length=9, choices=(('masculino', 'Masculino'), ('femenino', 'Femenino')))
    telefono = models.BigIntegerField()
    terapiapaciente = models.ForeignKey('Terapia', on_delete=models.CASCADE)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    provincia = models.ForeignKey('Provincias', on_delete=models.CASCADE)
    localidad = models.ForeignKey('Localidades', on_delete=models.CASCADE)
    suscripto = models.BooleanField(default=False)
    planactual = models.ForeignKey('Plan', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'paciente'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return 'Paciente ' + self.nombre + " " + self.apellido

class Profesional(models.Model):
    username = models.CharField(max_length=150, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.PositiveIntegerField(unique=True)
    sexo = models.CharField(max_length=9, choices=(('masculino', 'Masculino'), ('femenino', 'Femenino')))
    telefono = models.BigIntegerField()
    terapiaprofesional = models.ForeignKey('Terapia', on_delete=models.CASCADE)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    provincia = models.ForeignKey('Provincias', on_delete=models.CASCADE)
    localidad = models.ForeignKey('Localidades', on_delete=models.CASCADE)
    matricula = models.BigIntegerField(unique=True)

    class Meta:
        db_table = 'profesional'
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'

    def __str__(self):
        return 'Profesional ' + self.nombre + " " + self.apellido

class Plan(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()

    class Meta:
        db_table = 'plan'
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'

    def __str__(self):
        return 'Plan: ' + self.nombre

class Terapia(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'terapia'
        verbose_name = 'Terapia'
        verbose_name_plural = 'Terapias'

    def __str__(self):
        return 'Terapia: ' + self.nombre

class Provincias(models.Model):
    provincia = models.CharField(max_length=255)

    class Meta:
        db_table = 'provincias'
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self):
        return 'Provincia: ' + self.provincia

class Localidades(models.Model):
    id_provincia = models.ForeignKey(Provincias, on_delete=models.CASCADE)
    localidad = models.CharField(max_length=255)

    class Meta:
        db_table = 'localidad'
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'

    def __str__(self):
        return 'Localidad: ' + self.localidad
