import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { LoginService } from 'src/app/services/login.service';


@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent {
  constructor(
    private loginService: LoginService,
    private router: Router,
    ) {}

  get isAuthenticated(): boolean {
    let authStatus = false;
    this.loginService.estaAutenticado.subscribe(status => {
      authStatus = status;
    });
    return authStatus;
  }

  
  get username(): string {
    // Obtiene el nombre de usuario autenticado
    let userName = '';
    this.loginService.currentUser.subscribe((user: any) => {
      if (user) {
        userName = user.username; // Utiliza la propiedad 'username' del objeto de usuario
        console.log(userName);
      }
    });
    return userName;
  }
  
  logout() {
    // Llama al método logout del servicio de login para cerrar la sesión
    this.loginService.logout();
    this.router.navigate(['']);
  }
}
