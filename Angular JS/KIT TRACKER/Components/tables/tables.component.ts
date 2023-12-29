import { Component} from '@angular/core';
import { Router } from '@angular/router';
import { QueryService } from '../../services/query.service';
import { JOB } from '../../models/job';

@Component({
  selector: 'app-tables',
  templateUrl: './tables.component.html',
  styleUrls: ['./tables.component.scss']
})
export class TablesComponent{

  /* INITIALIZER SECTION */
  /* Constructor used to be able to use Router module and correlates it to public variable _router */
  constructor(
    public _router:Router,
    public Query: QueryService
  ) {}

  /* Initializes Public Variable: Empty Array of Strings */
  public Kits: JOB[] = []

  /* Creates Function to Call Lambda Function to Query Athena for Current data */
  RefreshSubscribe(component: number){
    this.Query.getResults(component).subscribe((data: JOB[]) => {this.Kits = data})
  };

  ToBeDone(): void {
    this.RefreshSubscribe(0)
  }

  Create(): void {
    this.RefreshSubscribe(1)
  }

  Request(): void {
    this.RefreshSubscribe(2)
  }

  Historical(): void {
    this.RefreshSubscribe(9)
  }
}
