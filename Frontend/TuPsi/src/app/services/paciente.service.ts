import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Paciente } from '../models/paciente.model';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class PacienteService {
  private signUpUrl = 'http://127.0.0.1:8000/api/sign/paciente/';
 

  constructor(private http: HttpClient) {
    console.log('Servicio Paciente está iniciando');
  }

  createPaciente(paciente: Paciente): Observable<Paciente> {
    return this.http.post<Paciente>(this.signUpUrl, paciente);
  }

  getPaciente(id: number): Observable<Paciente> {
    const url = `http://127.0.0.1:8000/admin/pacientes/${id}/`;
    return this.http.get<Paciente>(url);
  }

  getAllPacientes(): Observable<Paciente[]> {
    const url = 'http://127.0.0.1:8000/api/pacientes/';
    return this.http.get<Paciente[]>(url);
  }

  updatePaciente(paciente: Paciente): Observable<Paciente> {
    const url = `http://127.0.0.1:8000/api/pacientes/${paciente.id}/`;
    return this.http.put<Paciente>(url, paciente);
  }

  deletePaciente(id: number): Observable<Paciente> {
    const url = `http://127.0.0.1:8000/api/pacientes/${id}/`;
    return this.http.delete<Paciente>(url);
  }


}