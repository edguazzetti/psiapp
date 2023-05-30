import { Component, OnInit } from '@angular/core';

//? importaciones necesarias
import { FormGroup, FormControl, Validators } from '@angular/forms'; // buscar info sobre formularios reactivos
import { Professional } from '../models/professional.model';
// import { ToastrService } from 'ngx-toastr'; // tiene error y nose porqué

//? importamos el servicio que creamos
import { ProfessionalService } from '../services/professional.service';

@Component({
  selector:     'app-add-professional',
  templateUrl:  './add-professional.component.html',
  styleUrls: [  './add-professional.component.css'  ]
})
export class AddProfessionalComponent implements OnInit {

  pFormGr!: FormGroup;


  // constructor( private Toastr: ToastrService, private professionalService: ProfessionalService) {}
  constructor( private professionalService: ProfessionalService) {}

  ngOnInit() {
    this.pFormGr = new FormGroup({
      nombre:     new FormControl(''),
      apellido:     new FormControl(''),
      tipodeterapia:     new FormControl(''),
      email:   new FormControl(''),
      pronvicia:      new FormControl(''),
      localidad:     new FormControl(''),
      matricula:  new FormControl(''),
      telefono: new FormControl(''),
    })
  }


  crearProfesional(){
    const id: number = this.generateID()
    const {nombre, apellido, tipo_de_terapia, email, localidad, provincia, matricula, telefono } = this.pFormGr.value

    // console.log(this.pFormGr.value);


    const profesional: Professional = {
      nombre: nombre.toString(),
      apellido: apellido.toString(),
      tipo_de_terapia: tipo_de_terapia.toString(),
      email: email.toString(),
      localidad: localidad.toString(),
      provincia: provincia.toString(),
      numero_matricula: matricula.toString(),
      telefono: telefono.toString()
      
    }

    // this.professionalService.createProfessional(profesional).subscribe(
    //   data => {
    //     this.Toastr.success('Profesional Creado', `Profesional creado bajo el nombre ${data.nombre}, id: ${data}`)
    //   },
    //   error => {
    //     console.log(error);

    //     this.Toastr.error('Hubo un error', error)
    //   }
    // )

  }

  // Funcion para generar un id random de 3 digitos
  generateID(): number {
    return Math.floor(Math.random() * 900 ) + 100;
  }



}
