import React from 'react';
import { Switch, Route } from 'react-router-dom';
import Home from './containers/Home';
import Register from './containers/Register';
import Login from './containers/Login';
import Profile from './containers/Profile';
import UpdateProfile from './containers/UpdateProfile';
import UpdatePassword from './containers/UpdatePassword';
import Flag from './containers/Flag';
import Admin from './containers/Admin';

const Routes = () => (
  <div>
    <Switch>
      <Route exact path="/" component={Home} />
      <Route exact path="/login" component={Login} />
      <Route exact path="/register" component={Register} />
      <Route exact path="/userProfile/:username" component={Profile} />
      <Route exact path="/updateUser/:username" component={UpdateProfile} />
      <Route exact path="/showFlag/:username" component={Flag} />
      <Route exact path="/admin" component={Admin} />
      <Route
        exact
        path="/updatePassword/:username"
        component={UpdatePassword}
      />
    </Switch>
  </div>
);

export default Routes;
