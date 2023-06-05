import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
;

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  private apiURL: string = 'http://127.0.0.1:8000/api/auth/login/'; // ver en back
  private httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
  })
};

  constructor(private http: HttpClient) { }
  login(email: string, clave: string): Observable<any> {
    const body = {
      email,
      clave
    };
    return this.http.post<any>(`${this.apiURL}/login/`, body, this.httpOptions);
  }

}
