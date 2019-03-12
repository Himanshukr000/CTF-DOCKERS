/* eslint-disable no-console */
/* eslint-disable react/destructuring-assignment */

import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Redirect } from 'react-router-dom';
import TextField from '@material-ui/core/TextField';
import axios from 'axios';

import {
  LinkButtons,
  SubmitButtons,
  HeaderBar,
  cancelButton,
  saveButton,
  loginButton,
  inputStyle,
} from '../components';

const loading = {
  margin: '1em',
  fontSize: '24px',
};

const title = {
  pageTitle: 'Update Password Screen',
};

class UpdatePassword extends Component {
  constructor(props) {
    super(props);

    this.state = {
      username: '',
      password: '',
      loadingUser: false,
      updated: false,
      error: false,
    };
  }

  componentDidMount() {
    this.setState({ loadingUser: true });

    const accessString = localStorage.getItem('JWT');
    if (accessString === null) {
      this.setState({
        loadingUser: false,
        error: true,
      });
    } else {
      axios
        .get('http://visagenovel.ga:3003/findUser', {
          params: {
            username: this.props.match.params.username,
          },
          headers: { Authorization: `JWT ${accessString}` },
        })
        .then((response) => {
          // console.log(response.data);
          this.setState({
            loadingUser: false,
            username: response.data.username,
            password: response.data.password,
            error: false,
          });
        })
        .catch((error) => {
          console.log(error.response.data);
          this.setState({
            loadingUser: false,
            error: true,
          });
        });
    }
  }

  handleChange = name => (event) => {
    this.setState({
      [name]: event.target.value,
    });
  };

  updatePassword = (e) => {
    const accessString = localStorage.getItem('JWT');
    if (accessString === null) {
      this.setState({
        loadingUser: false,
        error: true,
      });
    } else {
      e.preventDefault();
      axios
        .put(
          'http://visagenovel.ga:3003/updatePassword',
          {
            username: this.state.username,
            password: this.state.password,
          },
          {
            headers: { Authorization: `JWT ${accessString}` },
          },
        )
        .then((response) => {
          if (response.data.message === 'password updated') {
            this.setState({
              updated: true,
              error: false,
              loadingUser: false,
            });
          }
        })
        .catch((error) => {
          console.log(error.response.data);
          this.setState({
            updated: false,
            error: true,
            loadingUser: false,
          });
        });
    }
  };

  // eslint-disable-next-line consistent-return
  render() {
    const {
      username, password, updated, error, loadingUser 
    } = this.state;

    if (error) {
      return (
        <div>
          <HeaderBar title={title} />
          <p style={loading}>
            An error has occurred. Please go login again.
          </p>
          <LinkButtons
            style={loginButton}
            buttonText="Go Login"
            link="/login"
          />
        </div>
      );
    }
    if (loadingUser !== false) {
      return (
        <div>
          <HeaderBar title={title} />
          <p style={loading}>Loading user data...</p>
        </div>
      );
    }
    if (loadingUser === false && updated === true) {
      return <Redirect to={`/userProfile/${username}`} />;
    }
    if (loadingUser === false) {
      return (
        <div>
          <HeaderBar title={title} />
          <form className="profile-form" onSubmit={this.updatePassword}>
            <TextField
              style={inputStyle}
              id="password"
              label="password"
              value={password}
              onChange={this.handleChange('password')}
              type="password"
            />
            <br />
            <SubmitButtons
              buttonStyle={saveButton}
              buttonText="Save Changes"
            />
          </form>
          <LinkButtons
            buttonStyle={cancelButton}
            buttonText="Return"
            link={`/userProfile/${username}`}
          />
        </div>
      );
    }
  }
}

UpdatePassword.propTypes = {
  // eslint-disable-next-line react/require-default-props
  match: PropTypes.shape({
    params: PropTypes.shape({
      username: PropTypes.string.isRequired,
    }),
  }),
};

export default UpdatePassword;
