import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Profesional } from '../models/profesional.model';
import { tap } from 'rxjs/operators';
import { Subject } from 'rxjs';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProfesionalService {
  apiURL: string = 'http://localhost:3000/psicologos';
  private profesionalCreadoSubject: Subject<Profesional> = new Subject<Profesional>();

  constructor(private http: HttpClient) {}

  getProfesional(): Observable<Profesional[]> {
    return this.http.get<Profesional[]>(this.apiURL);
  }

  createProfesional(psicologo: Profesional): Observable<Profesional> {
    return this.http.post<Profesional>(this.apiURL, psicologo).pipe(
      tap((psicologoCreado) => {
        this.profesionalCreadoSubject.next(psicologoCreado);
      })
    );
  }

  updateProfesional(psicologo: Profesional): Observable<Profesional> {
    const url = `${this.apiURL}/${psicologo.id}`;
    return this.http.put<Profesional>(url, psicologo);
  }

  deleteProfesional(id: number): Observable<any> {
    const url = `${this.apiURL}/${id}`;
    return this.http.delete(url);
  }

  getProfesionalCreadoObservable(): Observable<Profesional>{
    return this.profesionalCreadoSubject.asObservable();
  }
}
