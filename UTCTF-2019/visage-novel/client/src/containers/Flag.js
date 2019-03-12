/* eslint-disable react/destructuring-assignment */
/* eslint-disable camelcase */
/* eslint-disable no-console */
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

import {
  LinkButtons,
  loginButton,
  HeaderBar,
} from '../components';

const loading = {
  margin: '1em',
  fontSize: '24px',
};

const title = {
  pageTitle: 'User Profile Screen',
};

class Flag extends Component {
  constructor() {
    super();

    this.state = {
      is_admin: false,
      isLoading: true,
      error: false,
      flag: ''
    };
  }

  async componentDidMount() {
    const accessString = localStorage.getItem('JWT');
    if (accessString == null) {
      this.setState({
        isLoading: false,
        error: true,
      });
    } else {
      await axios
        .get('http://visagenovel.ga:3003/findUser', {
          params: {
            username: this.props.match.params.username,
          },
          headers: { Authorization: `JWT ${accessString}` },
        })
        .then((response) => {
          this.setState({
            is_admin: response.data.is_admin,
            isLoading: false,
            error: false,
          });

          if (response.data.is_admin) {
            axios.get('http://visagenovel.ga:3003/getFlag', {
              headers: { Authorization: `JWT ${accessString}` }
            }).then((res) => {
              this.setState({
                flag: res.data.flag
              });
            }).catch((error) => {
              console.error(error.response.data);
              this.setState({
                error: true,
              });
            });
          }
        })
        .catch((error) => {
          console.error(error.response.data);
          this.setState({
            error: true,
          });
        });
    }
  }

  logout = (e) => {
    e.preventDefault();
    localStorage.removeItem('JWT');
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
          ? `You are an admin! Here's the flag: ${this.state.flag || 'did you really think it would be that easy'}`
          : 'You are not an admin'}
      </div>
    );
  }
}

Flag.propTypes = {
  // eslint-disable-next-line react/require-default-props
  match: PropTypes.shape({
    params: PropTypes.shape({
      username: PropTypes.string.isRequired,
    }),
  }),
};

export default Flag;
