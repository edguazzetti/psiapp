import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { SearchComponent } from './pages/search/search.component';
import { LoginComponent } from './auth/login/login.component';
import { SignProfesionalComponent } from './auth/sign-profesional/sign-profesional.component';

import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { AddProfessionalComponent } from './pages/dashboard/add-professional/add-professional.component';
import { SeeProfessionalComponent } from './pages/dashboard/see-professional/see-professional.component';


const routes: Routes = [
  {path:'', component:HomeComponent},
  { path: 'search', component: SearchComponent },
  { path: 'login', component: LoginComponent },
  { path: 'professional-register', component: SignProfesionalComponent },

{
  path: 'dashboard',
  component: DashboardComponent,
  children: [
    {path: 'add-professional', component: AddProfessionalComponent},
    {path: 'see-professional', component: SeeProfessionalComponent}
  ]
}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
