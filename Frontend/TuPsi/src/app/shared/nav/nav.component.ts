import { Component } from '@angular/core';
import { LoginService } from 'src/app/services/login.service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent {
  constructor(private loginService: LoginService) {}

  get isAuthenticated(): boolean {
    let authStatus = false;
    this.loginService.estaAutenticado.subscribe(status => {
      authStatus = status;
    });
    return authStatus;
  }
  // get isAuthenticated(): boolean {
  //   return this.loginService.estaAutenticado.getValue();
  // }
  
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
  
  
  

  // get username(): string {
  //   // Obtiene el nombre de usuario autenticado
  //   console.log(this.username)
  //   return this.loginService.usuarioAutenticado.nombre;
   
  // }

  logout() {
    // Llama al método logout del servicio de login para cerrar la sesión
    this.loginService.logout();
  }
}
