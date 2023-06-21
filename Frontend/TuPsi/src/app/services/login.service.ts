import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { BehaviorSubject, Observable, throwError } from 'rxjs';
import { map, tap, catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  url = "http://127.0.0.1:8000/api/accounts/login/";
  currentUserSubject: BehaviorSubject<any>;
  currentUser: Observable<any>;
  private _estaAutenticado = new BehaviorSubject<boolean>(false);

  constructor(private http: HttpClient) {
    
    this.currentUserSubject = new BehaviorSubject<any>(JSON.parse(localStorage.getItem('currentUser') || '{}'));
    this.currentUser = this.currentUserSubject.asObservable();
  }
  
  login(email: string, password: string): Observable<any> {
    return this.http.post<any>(this.url, { email, password }, { observe: 'response' })
      .pipe(
        
        map(response => {
          const headers = response.headers; // Get the response headers
          const data = response.body; // Get the response body data
          if (data && data.username) {
           
            localStorage.setItem('currentUser', JSON.stringify(data));
            localStorage.setItem('token', this.getCookieValue(headers, 'csrftoken') || '');
            localStorage.setItem('username', data.username);
            
            this.currentUserSubject.next(data);
            this._estaAutenticado.next(true);
          }
    
          return data;
        }),
        catchError(error => {
          console.error('Error storing data in localStorage:', error);
          return throwError(error);
        })
      );
  }

  private getCookieValue(headers: HttpHeaders, cookieName: string): string | null {
    const cookies: string | null = headers.get('Set-Cookie');
    const cookieString: string | undefined = cookies?.split(';')
      .find((cookie: string) => cookie.trim().startsWith(`${cookieName}=`));
  
    if (cookieString) {
      return cookieString.split('=')[1].trim();
    }
  
    return null;
  }

  
  logout(): void {
    localStorage.removeItem('currentUser');
    localStorage.removeItem('token');
    localStorage.removeItem('username');
    this.currentUserSubject.next({});
    this._estaAutenticado.next(false); // Actualiza el valor de _estaAutenticado
    
  }

  get usuarioAutenticado(): any {
    return this.currentUserSubject.value;
  }

  get estaAutenticado(): BehaviorSubject<boolean> {
    return this._estaAutenticado;
  }
}
