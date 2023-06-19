import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class AdminServiceService {


  apiURL: string =  'http://localhost:3080/administrador'


  constructor(
    private http: HttpClient
  ) { }


  getAdmin(): Observable<any> {
    return this.http.get(this.apiURL)
  }




}