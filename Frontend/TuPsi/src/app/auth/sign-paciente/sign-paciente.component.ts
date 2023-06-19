import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { PacienteService } from 'src/app/services/paciente.service';
import { Paciente } from 'src/app/models/paciente.model';
import { Terapia } from 'src/app/models/terapia.model';
import { TerapiaService } from 'src/app/services/terapia.service';

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

  constructor(
    private formBuilder: FormBuilder,
    private pacienteService: PacienteService,
    private router: Router,
    public terapiaService: TerapiaService,
  ) {
    this.form = this.formBuilder.group({
      dni: ['', Validators.required],
      nombre: ['', Validators.required],
      apellido: ['', Validators.required],
      sexo: ['', Validators.required],
      telefono: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
      provincia: ['', Validators.required],
      localidad: ['', Validators.required],
      terapiapaciente: ['', Validators.required],
    });
   
  }
 
  ngOnInit(): void {
    this.terapiaService.obtenerTerapias(); // Llama a la función para obtener las terapias

    this.terapiaService.getTerapias().subscribe(terapias => {
      this.terapias = terapias; // Actualiza el arreglo de terapias cuando cambie
    });
  }

  
  onSubmit(): void {
    const user: Paciente = {
      username: this.form.value.nombre + this.form.value.apellido,
      email: this.form.value.email,
      password: this.form.value.password,
      dni: this.form.value.dni,
      nombre: this.form.value.nombre,
      apellido: this.form.value.apellido,
      sexo: this.form.value.sexo === 'Femenino' ? 'F' : (this.form.value.sexo === 'Masculino' ? 'M' : ''),
      telefono: this.form.value.telefono,
      terapiapaciente: this.form.value.terapiapaciente,
      provincia: this.form.value.provincia,
      localidad: this.form.value.localidad,
    };
console.log('subit', user)
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

  get nombre() {
    return this.form.get('nombre');
  }

  get apellido() {
    return this.form.get('apellido');
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
