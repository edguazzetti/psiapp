import { NgModule } from '@angular/core';
import { AdminPacientesComponent } from './admin-pacientes/admin-pacientes.component';
import { AdminProfesionalesComponent } from './admin-profesionales/admin-profesionales.component';
import { AdminPlanesComponent } from './admin-planes/admin-planes.component';
import { HomeComponent } from './home/home.component';
import { PlanesComponent } from './planes/planes.component';
import { SearchComponent } from './search/search.component';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';
import { FormsModule } from '@angular/forms';

import { LoginAdminComponent } from './login-admin/login-admin.component';



@NgModule({
  declarations: [
    AdminPacientesComponent,
    AdminPlanesComponent,
    AdminProfesionalesComponent,
    HomeComponent,
    PlanesComponent,
    SearchComponent,


  ],

  imports: [
    CommonModule,
    RouterModule,
    FormsModule,
    ReactiveFormsModule

  ],
  exports: [],
})
export class PagesModule {}
