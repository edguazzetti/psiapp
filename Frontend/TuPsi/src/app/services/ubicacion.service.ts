import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';
import { Provincia} from '../models/provincia.model'
import { Localidad } from '../models/localidad.model';

@Injectable({
  providedIn: 'root'
})
export class UbicacionService {
  // Provincias
  private provinciasSubject: BehaviorSubject<Provincia[]> = new BehaviorSubject<Provincia[]>([]); //almacenará y emitirá un arreglo de provincias
  public provincias$: Observable<Provincia[]> = this.provinciasSubject.asObservable(); // suscribirse a los cambios 
  private provinciasURL = 'http://127.0.0.1:8000/api/accounts/provincias/';
  // Localidades
  private localidadesSubject: BehaviorSubject<Localidad[]> = new BehaviorSubject<Localidad[]>([]); //almacenará y emitirá un arreglo de localidades
  public localidades$: Observable<Localidad[]> = this.localidadesSubject.asObservable(); // suscribirse a los cambios 
  private localidadesURL = 'http://127.0.0.1:8000/api/accounts/localidades/';
  //
  constructor(private http: HttpClient) { }


//Provincias
  obtenerProvincias(): void {
    this.http.get<Provincia[]>(this.provinciasURL).subscribe(
      provincias => {
        console.log('JSON recibido:', provincias);
        this.provinciasSubject.next(provincias);
      },
      error => console.error('Error al obtener las provincias', error)
    );
  }
  getProvincias(): Observable<Provincia[]> {
    return this.provincias$;
  }


//Localidades

obtenerLocalidades(): void {
  this.http.get<Localidad[]>(this.localidadesURL).subscribe(
    localidades => {
      console.log('JSON recibido:', localidades);
      this.localidadesSubject.next(localidades);
    },
    error => console.error('Error al obtener las localidades', error)
  );
}
getLocalidades(): Observable<Localidad[]> {
  return this.localidades$;
}
}

  
  
