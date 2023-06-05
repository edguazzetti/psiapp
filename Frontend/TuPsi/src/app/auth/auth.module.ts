import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoginComponent } from './login/login.component';
import { SignProfesionalComponent } from './sign-profesional/sign-profesional.component';
import { SignPacienteComponent } from './sign-paciente/sign-paciente.component';
import { RouterModule } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';
import { ProfileComponent } from './profile/profile.component';
import { FormsModule } from '@angular/forms';


@NgModule({
  declarations: [
    LoginComponent,
    SignProfesionalComponent,
    SignPacienteComponent,
    ProfileComponent
  ],
  imports: [
    CommonModule,
    RouterModule,
    ReactiveFormsModule,
    FormsModule
  ],
  exports: [
    LoginComponent,
    SignProfesionalComponent,
    SignPacienteComponent
  ]
})
export class AuthModule { }
