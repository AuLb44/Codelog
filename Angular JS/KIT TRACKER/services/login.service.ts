import { Injectable } from '@angular/core';
import { Profile } from '../models/profile';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  private User = ''
  private Dept = ''
  private Role = false

  /* Get User's Log In Details for Permissions and Data Collection */
  setLoginDetails(UserInput:string, DeptInput:string){
    this.User=UserInput
    this.Dept=DeptInput
    var profile = this.MH.find(({email}) => email == this.User)
    this.Role = Object(profile)['permissions']
  }

  /* Returns User Email, Dept, and Permissions */
  GetUserDetails():string{
    return(this.User)
  }
  GetDeptDetails():string{
    return(this.Dept)
  }
  GetRole():boolean{
    return(this.Role)
  }
  
  MH: Profile[] = [
    {
      name: 'Andrew',
      email: 'andrew.albee@thermofisher.com',
      permissions: true
    },
    {
      name: 'Andy',
      email: 'albeeandrew@gmail.com',
      permissions: false
    }
  ]
}