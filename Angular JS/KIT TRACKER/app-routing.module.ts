import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { LandingComponent } from './Components/landing/landing.component';
import { ProccessRoutingComponent } from './Components/proccess-routing/proccess-routing.component';
import { KitCreateComponent } from './Components/kit-create/kit-create.component';
import { KitMoveComponent } from './Components/kit-move/kit-move.component';
import { KitAddMatComponent } from './Components/[OUTDATED] kit-add-mat/kit-add-mat.component';
import { TablesComponent } from './Components/tables/tables.component';



const routes: Routes = [
  {path: 'Landing', component: LandingComponent},
  {path: 'Routing', component: ProccessRoutingComponent},
  {path: 'KitCreation', component: KitCreateComponent},
  {path: 'KitMove', component: KitMoveComponent},
  {path: 'KitAddMat', component: KitAddMatComponent},
  {path: 'Tables', component: TablesComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
