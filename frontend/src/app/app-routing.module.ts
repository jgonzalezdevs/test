import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { TicketListComponent } from './components/ticket-list/ticket-list.component';
import { TicketDetailsComponent } from './components/ticket-details/ticket-details.component';
import { TicketCreateComponent } from './components/ticket-create/ticket-create.component';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';

const routes: Routes = [
  { path: '', component: LoginComponent },
  { path: 'ticket', component: TicketListComponent },
  { path: 'ticket/:id', component: TicketDetailsComponent },
  { path: 'ticket/creation', component: TicketCreateComponent },
  { path: 'register', component: RegisterComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
