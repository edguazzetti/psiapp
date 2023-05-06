import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {HeaderComponent } from '../app/home/header/header.component';
import {Section1Component} from '../app/home/section1/section1.component';
import {Section2Component} from '../app/home/section2/section2.component';

const routes: Routes = [
  {path:'Home', component:HeaderComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
