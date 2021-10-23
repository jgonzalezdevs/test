import { Component, OnInit } from '@angular/core';
import { TicketService } from 'src/app/services/ticket.service';

@Component({
  selector: 'app-ticket-list',
  templateUrl: './ticket-list.component.html',
  styleUrls: ['./ticket-list.component.css']
})
export class TicketListComponent implements OnInit {

  tickets: any;
  currentTicket = null;
  currentIndex = -1;

  constructor(private ticketService: TicketService) { }

  ngOnInit(): void {
    this.readTickets();
  }

  readTickets(): void {
    this.ticketService.readAll()
      .subscribe(
        tickets => {
          this.tickets = tickets;
          console.log(tickets);
        },
        error => {
          console.log(error);
        }
      );
  }

  refresh(): void {
    this.readTickets();
    this.currentTicket = null;
    this.currentIndex = -1;
  }

  setCurrentTicket(ticket, index): void {
    this.currentTicket = ticket;
    this.currentIndex = index;
  }

  deleteAllTickets(): void {
    this.ticketService.deleteAll()
      .subscribe(
        response => {
          console.log(response);
          this.readTickets();
        },
        error => {
          console.log(error);
        }
      );
  }

}
