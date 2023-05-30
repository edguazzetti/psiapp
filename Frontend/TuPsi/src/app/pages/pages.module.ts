import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home/home.component';
import { SearchComponent } from './search/search.component';
import { RouterModule } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { FooterComponent } from '../shared/footer/footer.component';
import { AddProfessionalComponent } from './dashboard/add-professional/add-professional.component';
import { SeeProfessionalComponent } from './dashboard/see-professional/see-professional.component';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations'
import { ToastrModule } from 'ngx-toastr';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AdminPacientesComponent } from './admin-pacientes/admin-pacientes.component';
import { AdminProfesionalesComponent } from './admin-profesionales/admin-profesionales.component';
import { AdminPlanesComponent } from './admin-planes/admin-planes.component';
import { PlanesComponent } from './planes/planes.component';

@NgModule({
  declarations: [
    HomeComponent,
    SearchComponent,
    DashboardComponent,
    AddProfessionalComponent,
    SeeProfessionalComponent,
    AdminPacientesComponent,
    AdminProfesionalesComponent,
    AdminPlanesComponent,
    PlanesComponent,
    
  ],
  imports: [
    CommonModule,
    RouterModule,
    FormsModule,
    ReactiveFormsModule,
    ToastrModule.forRoot(),
    BrowserAnimationsModule,
    
  ],
  exports: [
    HomeComponent,
    SearchComponent
  ]
})
export class PagesModule { }