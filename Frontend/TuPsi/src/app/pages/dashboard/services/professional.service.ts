import { Injectable } from '@angular/core';

//? importaciones necesarias
import { HttpClient } from '@angular/common/http';
import { Professional } from '../models/professional.model';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ProfessionalService {

  //? creamos una variable que usaremos para indicar la ruta a nuestro backend
  apiURL: string = 'http://localhost:3000/professional'

  //? inyectamos HttpClient en el constructor
  constructor(private http: HttpClient) { }

  //? creamos un metodo GET para obtener todos los profesionales
  getAllprofessionals(): Observable<Professional[]>{
    return this.http.get<Professional[]>(this.apiURL)
  }

  //? creamos un metodo POST para crear un nuevo profesional
  createProfessional(professional: Professional): Observable<Professional> {
    return this.http.post<Professional>(this.apiURL, professional)
  }




}