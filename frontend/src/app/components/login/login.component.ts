import { Component } from "@angular/core";
import { UsersService } from "src/app/services/user.service";
import { Router } from '@angular/router';

@Component({
  selector: "app-login",
  templateUrl: "./login.component.html",
  styleUrls: ["./login.component.css"]
})
export class LoginComponent {
  username: string;
  password: string;

  constructor(public userService: UsersService, private router: Router) {}

  login() {
    const user = {username: this.username, password: this.password};
    this.userService.login(user).subscribe( data => {
      console.log(data);
      this.redirect()
    });
  }
  redirect() {
    this.router.navigate(['ticket']);
}
}