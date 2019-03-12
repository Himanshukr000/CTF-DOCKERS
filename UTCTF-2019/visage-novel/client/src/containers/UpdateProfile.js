/* eslint-disable camelcase */
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
  pageTitle: 'Update User Profile Screen',
};

class UpdateProfile extends Component {
  constructor(props) {
    super(props);

    this.state = {
      first_name: '',
      last_name: '',
      email: '',
      username: '',
      status: '',
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
    }

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
          first_name: response.data.first_name ? response.data.first_name : '',
          last_name: response.data.last_name ? response.data.last_name : '',
          email: response.data.email,
          username: response.data.username,
          status: response.data.status,
          error: false,
        });
      })
      .catch((error) => {
        console.log(error.response.data);
      });
  }

  handleChange = name => (event) => {
    this.setState({
      [name]: event.target.value,
    });
  };

  updateUser = (e) => {
    const accessString = localStorage.getItem('JWT');
    if (accessString === null) {
      this.setState({
        loadingUser: false,
        error: true,
      });
    }

    e.preventDefault();

    axios
      .get(
        'http://visagenovel.ga:3003/sanitize',
        {
          params: { content: this.state.status },
        }
      ).then((res) => {
        const sanitized = res.data.content;
        const { checksum } = res.data;

        axios
          .put(
            'http://visagenovel.ga:3003/updateUser',
            {
              first_name: this.state.first_name,
              last_name: this.state.last_name,
              email: this.state.email,
              status: btoa(sanitized),
              checksum,
              username: this.state.username,
            },
            {
              headers: { Authorization: `JWT ${accessString}` },
            },
          )
          // eslint-disable-next-line no-unused-vars
          .then((response) => {
            // console.log(response.data);
            this.setState({
              updated: true,
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
      });
  };

  // eslint-disable-next-line consistent-return
  render() {
    const {
      first_name,
      last_name,
      email,
      username,
      updated,
      status,
      error,
      loadingUser,
    } = this.state;

    if (error) {
      return (
        <div>
          <HeaderBar title={title} />
          <p style={loading}>
            An error has occurred. Please go login again.
          </p>
          <LinkButtons
            buttonStyle={loginButton}
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
          <form className="profile-form" onSubmit={this.updateUser}>
            <TextField
              style={inputStyle}
              id="first_name"
              label="First name"
              value={first_name}
              onChange={this.handleChange('first_name')}
              placeholder="First Name"
            />
            <br />
            <TextField
              style={inputStyle}
              id="last_name"
              label="Last name"
              value={last_name}
              onChange={this.handleChange('last_name')}
              placeholder="Last Name"
            />
            <br />
            <TextField
              style={inputStyle}
              id="email"
              label="Email"
              value={email}
              onChange={this.handleChange('email')}
              placeholder="Email"
            />
            <br />
            <TextField
              style={inputStyle}
              id="status"
              label="Status"
              value={status || ''}
              onChange={this.handleChange('status')}
              placeholder="status"
            />
            <br />
            <SubmitButtons buttonStyle={saveButton} buttonText="Save Changes" />
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

UpdateProfile.propTypes = {
  // eslint-disable-next-line react/require-default-props
  match: PropTypes.shape({
    params: PropTypes.shape({
      username: PropTypes.string.isRequired,
    }),
  }),
};

export default UpdateProfile;
