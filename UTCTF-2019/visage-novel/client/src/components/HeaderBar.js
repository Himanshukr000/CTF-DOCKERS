import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import { Link } from 'react-router-dom';

const headerStyle = {
  background:
    '#3C5A99',
  color: 'white',
};

const HeaderBar = () => (
  <div className="header">
    <AppBar position="static" color="default" style={headerStyle}>
      <Toolbar>
        <Link to="/" style={{ textDecoration: 'none', color: 'white' }}>
          <Typography variant="title" color="inherit">
            <b>VisageNovel</b>
          </Typography>
        </Link>
      </Toolbar>
    </AppBar>
  </div>
);

export default HeaderBar;
