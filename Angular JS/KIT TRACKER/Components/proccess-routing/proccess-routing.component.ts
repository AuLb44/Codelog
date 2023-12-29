import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { LoginService } from '../../services/login.service';


@Component({
  selector: 'app-proccess-routing',
  templateUrl: './proccess-routing.component.html',
  styleUrls: ['./proccess-routing.component.scss']
})
export class ProccessRoutingComponent {

  /* Constructor used to be able to use Router module and correlates it to public variable _router */
  constructor(public _router:Router, public login:LoginService) {}

  /* Initializes Public Variables */
  public LoginUser = ''
  public LoginDept = ''
  public LoginRole = false

  /* Creates funciton for grabbing Login Details from Landing Component */
  RetreiveLoginDetails(){
    this.LoginUser = this.login.GetUserDetails()
    this.LoginDept = this.login.GetDeptDetails()
    this.LoginRole = this.login.GetRole()
  }

  /* Initializes component to trigger Refresh function */
  ngOnInit(): void {
    this.RetreiveLoginDetails()
  }


  /* Creates Routing Buttons to Creation, Move, and Addtional Material Request Components */
  KitCreate(): void{
    this._router.navigate(['KitCreation'])
  }
  KitMove(): void{
    this._router.navigate(['KitMove'])
  }
  KitTables(): void{
    this._router.navigate(['Tables'])
  }
}
