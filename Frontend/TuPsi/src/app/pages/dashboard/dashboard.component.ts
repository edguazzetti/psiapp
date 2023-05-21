import { Component, OnInit } from '@angular/core';


import { Router } from '@angular/router'; 






interface MenuItems {
  title: string, 
  iconUrl: string, 
  route: string 
}


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})


export class DashboardComponent implements OnInit {

  
  menuItems: MenuItems[] = [
    {
      title: 'Agregar Profesional',
      iconUrl: '../../../assets/img/person-add.svg',
      route: 'dashboard/add-professional'
    },
    {
      title: 'Ver Profesionales',
      iconUrl: '../../../assets/img/people.svg',
      route: 'dashboard/see-professional'
    }
  ]

 
  constructor(private router: Router) {}

  ngOnInit() {
      this.navigateTo('dashboard/add-professional')
  }

  
  navigateTo(route: string){ 
    this.router.navigateByUrl(route)
  }

}