import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { LandingComponent } from './Components/landing/landing.component';
import { KitCreateComponent } from './Components/kit-create/kit-create.component';
import { FormsModule } from '@angular/forms';
import { KitMoveComponent } from './Components/kit-move/kit-move.component';
import { KitAddMatComponent } from './Components/[OUTDATED] kit-add-mat/kit-add-mat.component';
import { HttpClientModule } from '@angular/common/http';
import { ProccessRoutingComponent } from './Components/proccess-routing/proccess-routing.component';
import { TablesComponent } from './Components/tables/tables.component';
import { KitStatusComponent } from './Components/kit-status/kit-status.component';


@NgModule({
  declarations: [
    AppComponent,
    LandingComponent,
    KitCreateComponent,
    KitMoveComponent,
    KitAddMatComponent,
    ProccessRoutingComponent,
    TablesComponent,
    KitStatusComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
