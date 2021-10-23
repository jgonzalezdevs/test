import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { TicketService } from 'src/app/services/ticket.service';

@Component({
  selector: 'app-ticket-details',
  templateUrl: './ticket-details.component.html',
  styleUrls: ['./ticket-details.component.css']
})
export class TicketDetailsComponent implements OnInit {

  currentTicket = null;
  message = '';

  constructor(
    private ticketService: TicketService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.message = '';
    this.getTicket(this.route.snapshot.paramMap.get('id'));
  }

  getTicket(id): void {
    this.ticketService.read(id)
      .subscribe(
        ticket => {
          this.currentTicket = ticket;
          console.log(ticket);
        },
        error => {
          console.log(error);
        }
      );
  }

  setAvailableStatus(status): void {
    const data = {
      name: this.currentTicket.name,
      last_name: this.currentTicket.last_name,
      paternal_last_name: this.currentTicket.paternal_last_name,
      maternal_last_name: this.currentTicket.maternal_last_name,
      age: this.currentTicket.age,
      rfc: this.currentTicket.rfc,
      date_of_birth: this.currentTicket.date_of_birth
    };

    this.ticketService.update(this.currentTicket.id, data)
      .subscribe(
        response => {
          this.currentTicket.available = status;
          console.log(response);
        },
        error => {
          console.log(error);
        }
      );
  }

  updateTicket(): void {
    this.ticketService.update(this.currentTicket.id, this.currentTicket)
      .subscribe(
        response => {
          console.log(response);
          this.message = 'El Ticket fue actualizado.';
        },
        error => {
          console.log(error);
        });
  }

  deleteTicket(): void {
    this.ticketService.delete(this.currentTicket.id)
      .subscribe(
        response => {
          console.log(response);
          this.router.navigate(['/tickets']);
        },
        error => {
          console.log(error);
        });
  }

}
