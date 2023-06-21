import { NgModule } from '@angular/core';
import { AdminPacientesComponent } from './admin-pacientes/admin-pacientes.component';
import { AdminProfesionalesComponent } from './admin-profesionales/admin-profesionales.component';
import { AdminPlanesComponent } from './admin-planes/admin-planes.component';
import { HomeComponent } from './home/home.component';
import { PlanesComponent } from './planes/planes.component';
import { SearchComponent } from './search/search.component';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { ProfileComponent } from './profile/profile.component';


@NgModule({
  declarations: [
    AdminPacientesComponent,
    AdminPlanesComponent,
    AdminProfesionalesComponent,
    HomeComponent,
    PlanesComponent,
    SearchComponent,
    ProfileComponent,   
     
  ],

  imports: [
    CommonModule,
    RouterModule,
    FormsModule,

   
  ],
  exports: [],
})
export class PagesModule {}
