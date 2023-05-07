import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { SearchComponent } from './pages/search/search.component';
import { LoginComponent } from './auth/login/login.component';
import { SignProfesionalComponent } from './auth/sign-profesional/sign-profesional.component';

const routes: Routes = [
  {path:'', component:HomeComponent},
  { path: 'search', component: SearchComponent },
  { path: 'login', component: LoginComponent },
  { path: 'professional-register', component: SignProfesionalComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
