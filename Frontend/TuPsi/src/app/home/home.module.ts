import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header/header.component';
import { Section1Component } from './section1/section1.component';
import { Section2Component } from './section2/section2.component';



@NgModule({
  declarations: [
    HeaderComponent,
    Section1Component,
    Section2Component
  ],
  imports: [
    CommonModule,

  ],
  exports: [
    HeaderComponent,
    Section1Component,
    Section2Component
  ]
})
export class HomeModule { }
