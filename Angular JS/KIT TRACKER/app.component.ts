import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})

/* Export class includes implimentation of OnInit to be able to have Default Functionality */
export class AppComponent implements OnInit{ 

  /* Constructor used to be able to use Router module and correlates it to public variable _router */
  constructor(public _router:Router) {}

  ngOnInit(): void {
    this._router.navigate(['Landing'])
  } 
}
