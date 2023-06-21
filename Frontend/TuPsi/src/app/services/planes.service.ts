import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Plan } from '../models/planes.model';
import { tap } from 'rxjs/operators';
import { Subject } from 'rxjs';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PlanesService {
  apiURL: string = 'http://127.0.0.1:8000/api/accounts/planes/';
  private planCreadoSubject: Subject<Plan> = new Subject<Plan>();

  constructor(private http: HttpClient) {}

  getPlan(): Observable<Plan[]> {
    return this.http.get<Plan[]>(this.apiURL);
  }

  createPlan(plan: Plan): Observable<Plan>{
    return this.http.post<Plan>(this.apiURL, plan).pipe(
      tap((planCreado) => {
        this.planCreadoSubject.next(planCreado);
      })
    );
  }

  updatePlan(plan: Plan): Observable<Plan>{
    const url = `${this.apiURL}/${plan.id}`;
    return this.http.put<Plan>(url, plan);
  }

  deletePlan(id: number): Observable<any> {
    const url = `${this.apiURL}/${id}`;
    return this.http.delete(url);
  }

  getPlanCreadoObservable(): Observable<Plan>{
    return this.planCreadoSubject.asObservable();
  }
}
