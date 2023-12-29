import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { LoginService } from '../../services/login.service';
import { JOB } from '../../models/job';

@Component({
  selector: 'app-kit-add-mat',
  templateUrl: './kit-add-mat.component.html',
  styleUrls: ['./kit-add-mat.component.scss']
})
export class KitAddMatComponent {

  constructor(public _router:Router, public login:LoginService) {}

  /* Initializes Public Variable: Empty Array of Strings */
  public jobsList: JOB[] = [];

  /* Definining login variables, defining function to call service, setting variables with service collected values */
  LoginUser = ''
  LoginDept = ''
  tempval: JOB = {
    KitNum: '',
    LotNum: '',
    WONum: '',
    ProcessStep: '',
    QTY: '',
    USER: '',
    DEPT: '',
    InputDate: '',
    PSDate: '',
    Comments: '',
    TimeNeeded: '',
    QuantityNeeded: ''
  }

  /* Creates Back Button Fucntion. Defines it to change component to 'Landing' page by calling _router Function */
  BackButton() {
    this._router.navigate(['Routing'])
  }

  RetreiveLoginDetails(){
    this.LoginUser = this.login.GetUserDetails()
    this.LoginDept = this.login.GetDeptDetails()
  }

}
