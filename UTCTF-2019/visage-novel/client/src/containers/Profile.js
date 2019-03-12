/* eslint-disable react/destructuring-assignment */
/* eslint-disable camelcase */
/* eslint-disable no-console */
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';
import Table from '@material-ui/core/Table';
import Button from '@material-ui/core/Button';
import { Link, Redirect } from 'react-router-dom';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableRow from '@material-ui/core/TableRow';

import {
  LinkButtons,
  updateButton,
  deleteButton,
  loginButton,
  logoutButton,
  HeaderBar,
  linkStyle,
  forgotButton,
} from '../components';

const loading = {
  margin: '1em',
  fontSize: '24px',
};

const title = {
  pageTitle: 'User Profile Screen',
};

class Profile extends Component {
  constructor() {
    super();

    this.state = {
      first_name: '',
      last_name: '',
      email: '',
      username: '',
      status: '',
      reported: false,
      isLoading: true,
      deleted: false,
      error: false,
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
            first_name: response.data.first_name,
            last_name: response.data.last_name,
            email: response.data.email,
            username: response.data.username,
            status: response.data.status,
            reported: response.data.reported,
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

  logout = (e) => {
    e.preventDefault();
    localStorage.removeItem('JWT');
    localStorage.removeItem('logged_in_user');
  };

  reportUser = (e) => {
    const accessString = localStorage.getItem('JWT');
    e.preventDefault();

    axios.get('http://visagenovel.ga:3003/report', {
      params: {
        username: this.props.match.params.username,
      },
      headers: { Authorization: `JWT ${accessString}` }
    }).then((response) => {
      alert(response.data.message);
      window.location.reload();
    }).catch((error) => {
      console.error(error.response.data);
      this.setState({
        error: true,
      });
    });
  }

  render() {
    const {
      first_name,
      last_name,
      email,
      username,
      error,
      reported,
      status,
      isLoading,
      deleted,
    } = this.state;
    const logged_in_user = localStorage.getItem('logged_in_user');

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
    if (deleted) {
      return <Redirect to="/" />;
    }
    return (
      <div>
        <HeaderBar title={title} />
        <Table>
          <TableBody>
            <TableRow>
              <TableCell>First Name</TableCell>
              <TableCell>{first_name}</TableCell>
            </TableRow>
            <TableRow>
              <TableCell>Last Name</TableCell>
              <TableCell>{last_name}</TableCell>
            </TableRow>
            <TableRow>
              <TableCell>Email</TableCell>
              <TableCell>{email}</TableCell>
            </TableRow>
            <TableRow>
              <TableCell>User Name</TableCell>
              <TableCell>{username}</TableCell>
            </TableRow>
            <TableRow>
              <TableCell>
                Status
              </TableCell>
              <TableCell dangerouslySetInnerHTML={{ __html: status }} />
            </TableRow>
            <TableRow>
              <TableCell>Share Link</TableCell>
              <TableCell>
                <Link
                  to={`/userProfile/${username}`}
                >
                  {`/userProfile/${username}`}
                </Link>
              </TableCell>
            </TableRow>
          </TableBody>
        </Table>
        {logged_in_user !== username ? (
          <div>
            <br />
            {!reported 
            ? (
              <Button onClick={this.reportUser} color="secondary">
              This is inappropriate
              </Button>
            ) 
            : (
              <div>
                Thank you for reporting! 
                An admin is looking into this and should make a decision within 10 minutes.
              </div>
            )}
          </div>
        ) : (
          <div>
            <LinkButtons
              buttonStyle={deleteButton}
              buttonText="Get Flag"
              link={`/showFlag/${username}`}
            />
            <LinkButtons
              buttonStyle={updateButton}
              buttonText="Update User"
              link={`/updateUser/${username}`}
            />
            <LinkButtons
              buttonStyle={forgotButton}
              buttonText="Update Password"
              link={`/updatePassword/${username}`}
            />
            <Button
              style={logoutButton}
              variant="contained"
              color="primary"
              onClick={this.logout}
            >
              <Link style={linkStyle} to="/">
                Logout
              </Link>
            </Button>
          </div>
          )
        }
      </div>
    );
  }
}

Profile.propTypes = {
  // eslint-disable-next-line react/require-default-props
  match: PropTypes.shape({
    params: PropTypes.shape({
      username: PropTypes.string.isRequired,
    }),
  }),
};

export default Profile;
