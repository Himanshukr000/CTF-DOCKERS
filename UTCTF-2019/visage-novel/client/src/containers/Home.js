import React from 'react';
import {
  HeaderBar,
  LinkButtons,
  loginButton,
  registerButton,
} from '../components';

const title = {
  pageTitle: 'Home Screen',
};

const Home = () => (
  <div className="home-page">
    <HeaderBar title={title} />
    <h1>Welcome to VisageNovel, the next #1 social networking app.</h1>
    <h2>We demand to be taken seriously!</h2>
    <LinkButtons
      buttonText="Register"
      buttonStyle={registerButton}
      link="/register"
    />
    <LinkButtons buttonText="Login" buttonStyle={loginButton} link="/login" />
  </div>
);

export default Home;
