import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Paciente } from '../models/paciente.model';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root',
})
export class PacienteService {
  private signUpUrl = 'http://127.0.0.1:8000/api/accounts/paciente/create/';
 

  constructor(private http: HttpClient) {
    console.log('Servicio Paciente está iniciando');
  }

  createPaciente(paciente: Paciente): Observable<Paciente> {
    console.log('paciente',paciente)
    return this.http.post<Paciente>(this.signUpUrl, paciente);
  }

  getPaciente(id: number): Observable<Paciente> {
    const url = `http://127.0.0.1:8000/api/accounts/paciente/${id}/`;
    return this.http.get<Paciente>(url);
  }

  getAllPacientes(): Observable<Paciente[]> {
    const url = 'http://127.0.0.1:8000/api/accounts/paciente/';
    return this.http.get<Paciente[]>(url);
  }

  updatePaciente(paciente: Paciente): Observable<Paciente> {
    const url = ``;
    return this.http.put<Paciente>(url, paciente);
  }

  deletePaciente(id: number): Observable<Paciente> {
    const url = `/${id}/`;
    return this.http.delete<Paciente>(url);
  }


}