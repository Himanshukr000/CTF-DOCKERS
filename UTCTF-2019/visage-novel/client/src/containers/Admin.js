/* eslint-disable react/destructuring-assignment */
/* eslint-disable camelcase */
/* eslint-disable no-console */
import React, { Component } from 'react';
import axios from 'axios';
import TextField from '@material-ui/core/TextField';

import {
  LinkButtons,
  loginButton,
  inputStyle,
  saveButton,
  SubmitButtons,
  HeaderBar,
} from '../components';

const loading = {
  margin: '1em',
  fontSize: '24px',
};

const title = {
  pageTitle: 'Admin panel',
};

class Admin extends Component {
  constructor() {
    super();

    this.state = {
      promoting_username: '',
      is_admin: false,
      isLoading: true,
      error: false,
    };
  }

  async componentDidMount() {
    const accessString = localStorage.getItem('JWT');
    const username = localStorage.getItem('logged_in_user');
    if (accessString == null) {
      this.setState({
      isLoading: false,
      error: true,
      });
    } else {
      await axios
      .get('http://visagenovel.ga:3003/findUser', {
        params: {
        username,
        },
        headers: { Authorization: `JWT ${accessString}` },
      })
      .then((response) => {
        this.setState({
        is_admin: response.data.is_admin,
        isLoading: false,
        error: false,
        });
      })
      .catch((error) => {
        console.error(error.response.data);
        this.setState({
        error: true,
        });
      });
    }
  }

  promoteUser = (e) => {
    e.preventDefault();
    const accessString = localStorage.getItem('JWT');
    axios.post('http://visagenovel.ga:3003/promote', {
      username: this.state.promoting_username,
      secret: 'supersecretkey42'
    }, {
      headers: { Authorization: `JWT ${accessString}` },
    }).then((response) => {
      if (response.data.message === 'user promoted') {
        this.setState({
          error: false,
          promoting_username: 'success!'
        });
      }
    }).catch((error) => {
      console.log(error.response.data);
      this.setState({
        error: true,
        isLoading: false,
      });
    });
  }

  handleChange = name => (event) => {
    this.setState({
      [name]: event.target.value,
    });
  };

  render() {
    const {
      is_admin,
      error,
      isLoading,
    } = this.state;

    if (error) {
      return (
        <div>
          <HeaderBar title={title} />
          <div style={loading}>
            An error has occurred. Please login again.
          </div>
          <LinkButtons
            buttonText="Login"
            buttonStyle={loginButton}
            link="/login"
          />
        </div>
      );
    }
    if (isLoading) {
      return (
        <div>
          <HeaderBar title={title} />
          <div style={loading}>Loading User Data...</div>
        </div>
      );
    }
    return (
      <div>
        <HeaderBar title={title} />
        <br />
        {is_admin 
        ? (
          <div>
            <form className="profile-form" onSubmit={this.promoteUser}>
              <TextField
                style={inputStyle}
                id="username"
                label="Username"
                value={this.state.promoting_username}
                onChange={this.handleChange('promoting_username')}
                placeholder="Username"
              />
              <br />
              <SubmitButtons
                buttonStyle={saveButton}
                buttonText="Save Changes"
              />
            </form>
          </div>
        )
        : <div>Error: You are not an admin</div>
        }
      </div>
    );
  }
}

export default Admin;
