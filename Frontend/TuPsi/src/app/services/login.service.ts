import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  private apiURL: string = 'http://localhost:4200/login'; // ver en back

  constructor(private http: HttpClient) {}

  getUsers(): Observable<any> {
    return this.http.get<any>(`${this.apiURL}/users`);
  }

  validateLogin(username: string, password: string): Observable<any> {
    return this.http.post<any>(`${this.apiURL}/login`, { username, password });
  }
}


