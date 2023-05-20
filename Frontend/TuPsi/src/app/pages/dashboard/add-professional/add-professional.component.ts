import { Component, OnInit } from '@angular/core';

//? importaciones necesarias
import { FormGroup, FormControl, Validators } from '@angular/forms' // buscar info sobre formularios reactivos
import { Professional } from '../models/professional.model'
import { ToastrService } from 'ngx-toastr';

//? importamos el servicio que creamos
import { ProfessionalService } from '../services/professional.service';

@Component({
  selector:     'app-add-professional',
  templateUrl:  './add-professional.component.html',
  styleUrls: [  './add-professional.component.css'  ]
})
export class AddProfessionalComponent implements OnInit {

  pFormGr!: FormGroup;


  constructor( private toast: ToastrService, private professionalService: ProfessionalService) {}

  ngOnInit() {
    this.pFormGr = new FormGroup({
      nombre:     new FormControl(''),
      telefono:   new FormControl(''),
      email:      new FormControl(''),
      matricula:  new FormControl(''),
    })
  }


  crearProfesional(){
    const id: number = this.generateID()
    const {nombre, telefono, email, matricula } = this.pFormGr.value

    // console.log(this.pFormGr.value);


    const profesional: Professional = {
      nombre: nombre.toString(),
      telefono: telefono.toString(),
      email: email.toString(),
      numero_matricula: matricula.toString(),
      status: true,
    }

    this.professionalService.createProfessional(profesional).subscribe(
      data => {
        this.toast.success('Profesional Creado', `Profesional creado bajo el nombre ${data.nombre}, id: ${data}`)
      },
      error => {
        console.log(error);

        this.toast.error('Hubo un error', error)
      }
    )

  }

  // Funcion para generar un id random de 3 digitos
  generateID(): number {
    return Math.floor(Math.random() * 900 ) + 100;
  }



}
