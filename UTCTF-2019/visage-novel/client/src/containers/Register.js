/* eslint-disable no-console */
/* eslint-disable camelcase */
import React, { Component } from 'react';
import TextField from '@material-ui/core/TextField';
import axios from 'axios';

import {
  LinkButtons,
  SubmitButtons,
  registerButton,
  loginButton,
  inputStyle,
  HeaderBar,
} from '../components';

const title = {
  pageTitle: 'Register',
};

class Register extends Component {
  constructor(props) {
    super(props);

    this.state = {
      first_name: '',
      last_name: '',
      email: '',
      username: '',
      password: '',
      messageFromServer: '',
      showError: false,
      registerError: false,
      loginError: false,
    };
  }

  handleChange = name => (event) => {
    this.setState({
      [name]: event.target.value,
    });
  };

  registerUser = (e) => {
    e.preventDefault();
    const {
       first_name, last_name, username, password, email 
      } = this.state;
    if (username === '' || password === '' || email === '') {
      this.setState({
        showError: true,
        loginError: false,
        registerError: true,
      });
    } else {
      axios
        .post('http://visagenovel.ga:3003/registerUser', {
          first_name,
          last_name,
          email,
          username,
          password,
        })
        .then((response) => {
          // console.log(response.data.message);
          this.setState({
            messageFromServer: response.data.message,
            showError: false,
            loginError: false,
            registerError: false,
          });
        })
        .catch((error) => {
          console.error(error.response.data);
          if (error.response.data === 'username or email already taken') {
            this.setState({
              showError: true,
              loginError: true,
              registerError: false,
            });
          }
        });
    }
  };

  // eslint-disable-next-line consistent-return
  render() {
    const {
      first_name,
      last_name,
      email,
      username,
      password,
      messageFromServer,
      showError,
      loginError,
      registerError,
    } = this.state;

    if (messageFromServer === '') {
      return (
        <div>
          <HeaderBar title={title} />
          <form className="profile-form" onSubmit={this.registerUser}>
            <h1>Register</h1>
            <TextField
              style={inputStyle}
              id="first_name"
              label="first_name"
              value={first_name}
              onChange={this.handleChange('first_name')}
              placeholder="First Name"
            />
            <br />
            <TextField
              style={inputStyle}
              id="last_name"
              label="last_name"
              value={last_name}
              onChange={this.handleChange('last_name')}
              placeholder="Last Name"
            />
            <br />
            <TextField
              style={inputStyle}
              id="email"
              label="email"
              value={email}
              onChange={this.handleChange('email')}
              placeholder="Email"
            />
            <br />
            <TextField
              style={inputStyle}
              id="username"
              label="username"
              value={username}
              onChange={this.handleChange('username')}
              placeholder="Username"
            />
            <br />
            <TextField
              style={inputStyle}
              id="password"
              label="password"
              value={password}
              onChange={this.handleChange('password')}
              placeholder="Password"
              type="password"
            />
            <br />
            <SubmitButtons buttonStyle={registerButton} buttonText="Register" />
          </form>
          {showError === true && registerError === true && (
            <div>
              <p>Username, password and email are required fields.</p>
            </div>
          )}
          {showError === true && loginError === true && (
            <div>
              <p>
                That username or email is already taken. Please choose another
                or login.
              </p>
              <LinkButtons
                buttonText="Login"
                buttonStyle={loginButton}
                link="/login"
              />
            </div>
          )}
        </div>
      );
    }
    if (messageFromServer === 'user created') {
      return (
        <div>
          <HeaderBar title={title} />
          <h3>User successfully registered!</h3>
          <LinkButtons
            buttonText="Go Login"
            buttonStyle={loginButton}
            link="/login"
          />
        </div>
      );
    }
  }
}

export default Register;
