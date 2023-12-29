import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class WriteService {

  private url = '[INSERT LAMBDA URL HERE]'
  httpOptions = {headers: new HttpHeaders({
    'Content-Type':'application/JSON',
    'Cache-Control':'no-cache'
  })}

  constructor( private http: HttpClient) {}

  WriteNtree(Ntree: string[]){
    var NtreeString = ''
    var Y = 'init'
    
    Ntree.forEach(
      (value) => { NtreeString+=value.replaceAll(' ','%20')+'&'}
    )
    console.log(NtreeString)
    this.http.get(this.url+NtreeString,this.httpOptions).subscribe((data)=>{
      Y = Object(data)["message"];
      console.log(Y.toString())
      return Y
    })
  }
}
