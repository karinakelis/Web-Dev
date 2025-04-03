import { Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { ProductListComponent } from './product-list/product-list.component';

export const routes: Routes = [
  { path: '', component: AppComponent },
  { path: 'category/:id', component: ProductListComponent }
];