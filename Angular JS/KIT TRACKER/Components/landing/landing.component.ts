import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { LoginService } from '../../services/login.service';
import { QueryService } from 'src/app/services/query.service';
import { JOB } from 'src/app/models/job';


@Component({
  selector: 'app-landing',
  templateUrl: './landing.component.html',
  styleUrls: ['./landing.component.scss']
})

export class LandingComponent implements OnInit{

  /* Constructor used to be able to use Router module and correlates it to public variable _router */
  constructor(
    public _router:Router, 
    public login:LoginService, 
    public query:QueryService
  ) {}

  /* Initilize User and Department Variables */
  public User = ''
  public Dept = ''
  public QuerySwitch = 0
  public Kits: JOB[] = [];
  public DeptOption = [
    "",
    "AO",
    "AOF",
    "DPM",
    "LVL",
    "Labeling",
    "Liquid Finishing",
    "Component Prep",
    "Other"
  ]

  /* Set Variables User/Dept to input submissions */
  SetDept(Choice:string){
    this.Dept=Choice
  }
  StoreLoginDetails(){
    this.login.setLoginDetails(this.User, this.Dept )
  }

  /* Creates Routing Buttons to Creation, Move, and Addtional Material Request Components */
  LogIn(): void{
    this.StoreLoginDetails()
    this._router.navigate(['Routing'])
  }

  /* Creates Function to Call Lambda Function to Query Athena for Current data */
  RefreshSubscribe(component: number){
    this.query.getResults(component).subscribe((data: JOB[]) => {this.Kits = data})
  };

  ngOnInit(): void{
    this.RefreshSubscribe(this.QuerySwitch)
  }
}
