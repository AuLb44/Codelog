import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { JOB } from '../models/job';

@Injectable({
  providedIn: 'root'
})
export class QueryService {

  private url = '[INSERT LAMBDA URL HERE]'
  httpOptions = {headers: new HttpHeaders({
    'Content-Type':'application/json',
    'Cache-Control':'no-cache'
  })}

  constructor( private http: HttpClient ) {} 

  getResults(component: number): Observable<JOB[]>{
    const Y = this.http.get<JOB[]>(this.url+component, this.httpOptions);
    return Y
  }
}
