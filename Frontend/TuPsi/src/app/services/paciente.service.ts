import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Paciente } from '../models/paciente.model';
import { tap } from 'rxjs/operators';
import { Subject } from 'rxjs';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PacienteService {
  apiURL: string = 'http://127.0.0.1:8000/api/auth/singup/';
  private pacienteCreadoSubject: Subject<Paciente> = new Subject<Paciente>();

  constructor(private http: HttpClient) {}

  getPaciente(): Observable<Paciente[]> {
    return this.http.get<Paciente[]> (this.apiURL);
  }

  createPaciente(paciente: Paciente): Observable<Paciente> {
    return this.http.post<Paciente>(this.apiURL, paciente).pipe(
      tap((pacienteCreado) => {
        this.pacienteCreadoSubject.next(pacienteCreado);
      })
    );
  }

  updatePaciente(paciente: Paciente): Observable<Paciente> {
    const url = `${this.apiURL}/${paciente.id}`;
    return this.http.put<Paciente>(url, paciente);
  }

  deletePaciente(id: number): Observable<any> {
    const url = `${this.apiURL}/${id}`;
    return this.http.delete(url);
  }
  getPacienteCreadoObservable(): Observable<Paciente>{
    return this.pacienteCreadoSubject.asObservable();
  }
}