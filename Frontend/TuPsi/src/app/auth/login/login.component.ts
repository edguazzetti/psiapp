import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { LoginService } from '../../services/login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  formLogin!: FormGroup;
  errorMessage: string = '';

  constructor(private loginService: LoginService, private router: Router) {}

  ngOnInit(): void {
    this.formLogin = new FormGroup({
      email: new FormControl('', [Validators.required, Validators.email]),
      password: new FormControl('', [Validators.required, Validators.minLength(8)])
    });
  }

  createLogin() {
    if (this.formLogin.valid) {
      const formValue = this.formLogin.value;
      const { email, password } = formValue;

      this.loginService.getUsers().subscribe(
        (users) => {
          const foundUser = users.find((user: any) => user['email'] === email);

          if (foundUser) {
            if (foundUser['password'] === password) {
              console.log('Inicio de sesión exitoso:', foundUser);
              this.router.navigate(['/dashboard']);
            } else {
              console.error('Contraseña incorrecta.');
              this.errorMessage = 'Usuario y/o contraseña no válidos';
            }
          } else {
            console.error('Usuario no encontrado.');
            this.errorMessage = 'Usuario y/o contraseña no válidos';
          }
        },
        (error) => {
          console.error('Error al obtener los usuarios:', error);
          this.errorMessage = 'Error al iniciar sesión. Por favor, inténtelo nuevamente.';
        }
      );
    } else {
      this.errorMessage = 'Por favor, complete todos los campos obligatorios correctamente.';
    }
  }
}

