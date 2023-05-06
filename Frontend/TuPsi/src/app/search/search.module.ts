import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FilterComponent } from './filter/filter.component';
import { CardComponent } from './card/card.component';

@NgModule({
  declarations: [FilterComponent, CardComponent],
  imports: [CommonModule],
  exports: [FilterComponent, CardComponent],
})
export class SearchModule {}
