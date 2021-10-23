import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

const baseUrl = 'http://localhost:8000/ticket'

@Injectable({
  providedIn: 'root'
})
export class TicketService {

  constructor(private httpClient: HttpClient) { }

  readAll(): Observable<any> {
    return this.httpClient.get(baseUrl);
  }

  read(id): Observable<any> {
    return this.httpClient.get(`${baseUrl}/${id}/`);
  }

  create(data): Observable<any> {
    return this.httpClient.post(baseUrl+'/', data);
  }

  update(id, data): Observable<any> {
    return this.httpClient.put(`${baseUrl}/${id}/`, data);
  }

  delete(id): Observable<any> {
    return this.httpClient.delete(`${baseUrl}/${id}/`);
  }

  deleteAll(): Observable<any> {
    return this.httpClient.delete(baseUrl)
  }
}
