import { Component } from "@angular/core";
import { LoginService } from "src/app/services/login.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  email: string = '';
  clave: string = '';
  error: string = '';

  constructor(private loginService: LoginService) { }

  login() {
    this.loginService.login(this.email, this.clave)
      .subscribe(
        response => {
          // Manejar la respuesta exitosa del backend
          console.log(response);
        },
        error => {
          // Manejar el error del backend
          this.error = error.error.detail;
        }
      );
  }


 }

 