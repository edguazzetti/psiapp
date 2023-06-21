import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { PacienteService } from 'src/app/services/paciente.service';
import { Paciente } from 'src/app/models/paciente.model';
import { Terapia } from 'src/app/models/terapia.model';
import { TerapiaService } from 'src/app/services/terapia.service';
import { Provincia } from 'src/app/models/provincia.model';
import { Localidad } from 'src/app/models/localidad.model';
import { UbicacionService } from 'src/app/services/ubicacion.service';

@Component({
  selector: 'app-sign-paciente',
  templateUrl: './sign-paciente.component.html',
  styleUrls: ['./sign-paciente.component.css'],
})

  export class SignPacienteComponent implements OnInit {
    convertirAEntero(valor: any): number {
      return parseInt(valor, 10);
    }
  form: FormGroup;
  terapias: Terapia[] = []; // Arreglo para almacenar las terapias
  provincias: Provincia[]= []; // arreglo para almacenar las provincias
  localidades: Localidad[]= []; //arreglo para almacenar las localidades
  
  constructor(
    private formBuilder: FormBuilder,
    public pacienteService: PacienteService,
    public ubicacionService: UbicacionService,
    public terapiaService: TerapiaService,
    private router: Router,
  ) {
    this.form = this.formBuilder.group({
      dni: ['', Validators.required],
      name: ['', Validators.required],
      apellido: ['', Validators.required],
      sexo: ['', Validators.required],
      telefono: ['', Validators.required],
      lastname: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
      provincia: ['', Validators.required],
      localidad: ['', Validators.required],
      terapiapaciente: ['', Validators.required],
    });
   
  }
 
  ngOnInit(): void {
    //TerapiaService
    this.terapiaService.obtenerTerapias(); // Llama a la función para obtener las terapias
    this.terapiaService.getTerapias().subscribe(terapias => {
    this.terapias = terapias;
    });
    // Actualiza el arreglo de terapias cuando cambie
    //UbicacionService
    this.ubicacionService.obtenerProvincias(); // Llama a la función para obtener las provincias
    this.ubicacionService.obtenerLocalidades(); // Llama a la función para obtener las localidades
    this.ubicacionService.getProvincias().subscribe(provincias => {
    this.provincias = provincias; // Actualiza el arreglo de provincias cuando cambie
    });
    this.ubicacionService.getLocalidades().subscribe(localidades => {
      this.localidades = localidades; // Actualiza el arreglo de localidades cuando cambie
    });
  }

  //Al enviar el formulario de registro del paciente
  
  onSubmit(): void {
    const user: Paciente = {
      username: this.form.value.name + this.form.value.lastname,
      email: this.form.value.email,
      password: this.form.value.password,
      dni: this.form.value.dni,
      name: this.form.value.name,
      lastname: this.form.value.lastname,
      sexo: this.form.value.sexo,
      telefono: this.form.value.telefono,
      terapiapaciente: this.form.value.terapiapaciente,
      provincia: this.form.value.provincia,
      localidad: this.form.value.localidad,
    };
    console.log('Formulario', this.form.value)
    this.pacienteService.createPaciente(user).subscribe(
      response => {
        console.log('Registro exitoso', response);
        alert('El registro ha sido creado satisfactoriamente. A continuación, por favor Inicie Sesión.');
        this.router.navigate(['/login']);
      },
      error => {
        console.error('Error durante el registro ', error);
        // alert('Ha ocurrido un error durante el registro. Por favor, intenta nuevamente.');
      }
    );
  }
  
  

  get dni() {
    return this.form.get('dni');
  }

  get name() {
    return this.form.get('name');
  }

  get lastname() {
    return this.form.get('lastname');
  }

  get sexo() {
    return this.form.get('sexo');
  }

  get telefono() {
    return this.form.get('telefono');
  }

  get terapiapaciente() {
    return this.form.get('terapiapaciente');
  }

  get email() {
    return this.form.get('email');
  }

  get password() {
    return this.form.get('password');
  }

  get provincia() {
    return this.form.get('provincia');
  }

  get localidad() {
    return this.form.get('localidad');
  }
}
