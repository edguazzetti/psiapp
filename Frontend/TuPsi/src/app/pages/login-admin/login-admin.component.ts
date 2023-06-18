import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router'
import { AdminServiceService } from 'src/app/services/admin-service.service';

@Component({
  selector: 'app-login-admin',
  templateUrl: './login-admin.component.html',
  styleUrls: ['./login-admin.component.css'],

})
export class LoginAdminComponent implements OnInit {

  formAdmin!: FormGroup;

  admins: any[] = []


  constructor(
    private router: Router,
    private adminService: AdminServiceService

  ){}

  ngOnInit(): void {
    this.formAdmin = new FormGroup({
      email   : new FormControl('', Validators.required),
      password: new FormControl('', Validators.required),
    });

    this.adminService.getAdmin().subscribe({
      next: (adm) => this.admins = adm,
      error: (e) => console.error(e),
      complete: () => {}
    })

  }

  loginAdmin(){
    const formValue = this.formAdmin.value
    const { email, password } = formValue

    console.log(email, password);

    for (let i = 0; i < this.admins.length; i++) {
      const e = this.admins[i];
      if(email === e.email && password === e.contrasena) {
        this.router.navigateByUrl('/AdminProfesionales')
      }
      else {
        console.log('no existe el admin');

      }
    }



  }


}
