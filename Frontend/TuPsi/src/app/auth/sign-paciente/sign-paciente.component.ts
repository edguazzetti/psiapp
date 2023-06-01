import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { PacienteService } from 'src/app/services/paciente.service';
import { Paciente } from 'src/app/models/paciente.model';

@Component({
  selector: 'app-sign-paciente',
  templateUrl: './sign-paciente.component.html',
  styleUrls: ['./sign-paciente.component.css']
})
export class SignPacienteComponent implements OnInit {

  formPaciente!: FormGroup;
  successMessage: string = '';
  errorMessage: string = '';

  constructor(private pacienteService: PacienteService) {}

  ngOnInit(): void {
    this.formPaciente = new FormGroup({
      nombre: new FormControl('', Validators.required),
      apellido: new FormControl('', Validators.required),
      sexo: new FormControl('', Validators.required),
      telefono: new FormControl('', Validators.required),
      terapia: new FormControl('', Validators.required),
      email: new FormControl('', Validators.required),
      clave: new FormControl('', Validators.required),
      provincia: new FormControl('', Validators.required),
      localidad: new FormControl('', Validators.required),

    });
  }

  createPaciente() {
    if (this.formPaciente.valid) {
      const formValue = this.formPaciente.value;
      const { nombre, apellido, sexo, telefono, terapia, email, clave, provincia, localidad} = formValue;

      const paciente: Paciente = {
        nombre: nombre.toString(),
        apellido: apellido.toString(),
        sexo: sexo.toString(),
        telefono: telefono.toString(),
        terapia: terapia.toString(),
        email: email.toString(),
        clave: clave.toString(),
        provincia: provincia.toString(),
        localidad: localidad.toString(),

      };

      this.pacienteService.createPaciente(paciente).subscribe(
        (response) => {
          console.log('Paciente registrado con éxito:', response);
          this.formPaciente.reset();
          this.successMessage = 'Bienvenido';
          this.errorMessage = '';
        },
        (error) => {
          console.error('Error al intentar registrar el Paciente:', error);
          this.successMessage = '';
          this.errorMessage = 'Error al crear el Paciente. Por favor, inténtelo nuevamente.';
        }
      );
    } else {
      this.successMessage = '';
      this.errorMessage = 'Por favor, complete todos los campos obligatorios.';
    }
  }

  updatePaciente() {
    // Implementa la lógica para actualizar un paciente
  }

  deletePaciente() {
    // Implementa la lógica para eliminar un paciente
  }

  generateID(): number {
    return Math.floor(Math.random() * 900) + 100;
  }
}
