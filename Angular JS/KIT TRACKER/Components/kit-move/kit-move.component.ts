import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { LoginService } from '../../services/login.service';
import { QueryService } from '../../services/query.service';
import { WriteService } from '../../services/write.service';
import { JOB } from '../../models/job';


@Component({
  selector: 'app-kit-move',
  templateUrl: './kit-move.component.html',
  styleUrls: ['./kit-move.component.scss']
})
export class KitMoveComponent implements OnInit {

  /* INITIALIZER SECTION */
  /* Constructor used to be able to use Router module and correlates it to public variable _router */
  constructor(
    public _router:Router,
    public login:LoginService,
    public Query: QueryService,
    public Write: WriteService
  ) {}

  /* Initializes Public Variable: Empty Array of Strings */
  public LoginUser = ''
  public LoginDept = ''
  public RefreshTrigger = ''
  public QuerySwitch = 2
  public Kits: JOB[] = []
  public tempval: JOB = {
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
  public BlankVal = {
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
  public MoveOptions = [
    "",
    "Move In",
    "Move Out",
    "Additional Materials Needed"
  ]


  /* Creates Function to Call Lambda Function to Query Athena for Current data */
  RefreshSubscribe(component: number){
    this.Query.getResults(component).subscribe((data: JOB[]) => {this.Kits = data})
  };
  
  /* Creates funciton for grabbing Login Details from Landing Component */
  RetreiveLoginDetails(){
    this.LoginUser = this.login.GetUserDetails()
    this.LoginDept = this.login.GetDeptDetails()
  }

  /* Initializes component to trigger Refresh function */
  ngOnInit(): void {
    this.RefreshSubscribe(this.QuerySwitch)
    this.RetreiveLoginDetails()
  }


  /* MAIN FUNCTIONS SECTION */
  /* Creates Back Button Fucntion. Defines it to change component to 'Landing' page by calling _router Function */
  BackButton() {this._router.navigate(['Routing'])}

  /* Creates function to take user input and pass of to Lambda function for write */
  WriteData(data: string[]){
    this.Write.WriteNtree(data)
  }

  /* Creates Add Item Function. Defines functino to grab the current data and adds it to the array Items */
  MoveJob(data: JOB){

    /* Get Submission Detials, back end details to Job List */
    this.tempval.USER = this.LoginUser
    this.tempval.DEPT = this.LoginDept
    this.tempval.InputDate = Date()
    
    /* Sends data to write service to pass of to lambda function to write to DB */
    var Ntree = []
    Ntree.push(
      "KitNum="+data.KitNum,
      "LotNum="+data.LotNum,
      "WONum="+data.WONum,
      "ProcessStep="+data.ProcessStep,
      "QTY="+data.QTY,
      "USER="+data.USER,
      "DEPT="+data.DEPT,
      "InputDate="+data.InputDate,
      "PSDate="+data.PSDate,
      "Comments="+data.Comments
    )
    
    /* push data to service to write value to S3 and pushes local copy for display */
    this.WriteData(Ntree)
    this.Kits.push(this.tempval)
    this.Kits.sort((a,b) => (Number(a.InputDate) > Number(b.InputDate) ? -1 : 1))  

    /* clears tempval for next entry */
    this.tempval = this.BlankVal
  }

}