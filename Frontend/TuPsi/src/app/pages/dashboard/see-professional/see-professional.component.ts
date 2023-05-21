import { Component, OnInit, OnDestroy } from '@angular/core';

import { Professional } from '../models/professional.model';
import { ProfessionalService } from '../services/professional.service';
import { Subscription } from 'rxjs';


@Component({
  selector: 'app-see-professional',
  templateUrl: './see-professional.component.html',
  styleUrls: ['./see-professional.component.css']
})
export class SeeProfessionalComponent implements OnInit, OnDestroy {

  //lista de profesionales (que en este caso tiene un solo profesional)
 /* profesionales: Professional[] = [
    {

        nombre: "Julia",
        apellido: "Gómez",
        tipo-de-terapia: "Pareja",
        correo-electronico: "jgomez@gmail.com",
        provincia: "Buenos Aires",
        Localidad: "Lanus",
        matricula: "155442"

    }
  ]*/
electronico: any;
terapia: any;
de: any;
  profesionales: any;



  //? en el constructor inyectamos el servicio que creamos (profesional service)
  constructor(private professionalService: ProfessionalService){}


  ngOnInit() {
    this.seeProfessionals()
  }

  ngOnDestroy() {

  }

  //?  creamos el metodo para ver los profesionales
  seeProfessionals() {
    this.professionalService.getAllprofessionals().subscribe(
      (data) => {
        console.info(data);

        for (let i = 0; i < data.length; i++) {
          const e = data[i];
          this.profesionales.push(e)
        }
      },
      (error) => {
        console.log(error);

      }
    )
  }

}
