# Generated by Django 4.2.2 on 2023-06-18 22:52

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Localidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localidad', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Localidad',
                'verbose_name_plural': 'Localidades',
                'db_table': 'localidad',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Planes',
                'db_table': 'plan',
            },
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provincia', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
                'db_table': 'provincias',
            },
        ),
        migrations.CreateModel(
            name='Terapia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Terapia',
                'verbose_name_plural': 'Terapias',
                'db_table': 'terapia',
            },
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dni', models.PositiveIntegerField(unique=True)),
                ('sexo', models.CharField(choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')], max_length=9)),
                ('telefono', models.BigIntegerField()),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('matricula', models.BigIntegerField(unique=True)),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.localidades')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.provincias')),
                ('terapiaprofesional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.terapia')),
            ],
            options={
                'verbose_name': 'Profesional',
                'verbose_name_plural': 'Profesionales',
                'db_table': 'profesional',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dni', models.PositiveIntegerField(unique=True)),
                ('sexo', models.CharField(choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')], max_length=9)),
                ('telefono', models.BigIntegerField()),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('suscripto', models.BooleanField(default=False)),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.localidades')),
                ('planactual', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.plan')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.provincias')),
                ('terapiapaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.terapia')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'db_table': 'paciente',
            },
        ),
        migrations.AddField(
            model_name='localidades',
            name='id_provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.provincias'),
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='administrador_set', related_query_name='administrador', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='administrador_set', related_query_name='administrador', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(default='', max_length=150, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='customuser_set', related_query_name='customuser', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='customuser_set', related_query_name='customuser', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Custom Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
