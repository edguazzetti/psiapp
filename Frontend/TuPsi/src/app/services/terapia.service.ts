import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';
import { Terapia } from '../models/terapia.model';

@Injectable({
  providedIn: 'root'
})
export class TerapiaService {
  private terapiasSubject: BehaviorSubject<Terapia[]> = new BehaviorSubject<Terapia[]>([]); //almacenará y emitirá un arreglo de terapias.
  public terapias$: Observable<Terapia[]> = this.terapiasSubject.asObservable(); // suscribirse a los cambios en terapiasSubject
  private terapiasURL = 'http://127.0.0.1:8000/api/terapias/';

  constructor(private http: HttpClient) { }

  obtenerTerapias(): void {
    this.http.get<Terapia[]>(this.terapiasURL).subscribe(
      terapias => {
        console.log('JSON recibido:', terapias);
        this.terapiasSubject.next(terapias);
      },
      error => console.error('Error al obtener las terapias', error)
    );
  }
  getTerapias(): Observable<Terapia[]> {
    return this.terapias$;
  }
}
  
  
