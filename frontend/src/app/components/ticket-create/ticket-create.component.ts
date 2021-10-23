import { Component, OnInit } from '@angular/core';
import { TicketService } from 'src/app/services/ticket.service';

@Component({
  selector: 'app-ticket-create',
  templateUrl: './ticket-create.component.html',
  styleUrls: ['./ticket-create.component.css']
})
export class TicketCreateComponent implements OnInit {

  ticket = {
    title: '',
    description: '',
  }

  submitted = false;

  constructor(private ticketService: TicketService) { }

  ngOnInit(): void {
  }

  createTicket(): void {
    const data = {
      title: this.ticket.title,
      description: this.ticket.description,
    };

    this.ticketService.create(data)
      .subscribe(
        response => {
          console.log(response);
          this.submitted = true;
        },
        error => {
          console.log(error);
        }
      );
  }
  
  newTicket(): void {
    this.submitted = false;
    this.ticket = {
      title: '',
      description: ''
    }
  }

}
