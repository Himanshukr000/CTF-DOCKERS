/* eslint-disable no-console */
import passport from 'passport';
import User from '../sequelize';

module.exports = (app) => {
    app.post('/promote', (req, res, next) => {
      if(req.body.secret !== 'supersecretkey42'){
        console.log("invalid secret key");
        res.status(301).send("invalid secret key");
        return;
      }

      passport.authenticate('jwt', { session: false }, (err, user, info) => {
        if (err) {
          console.log(err);
        }

        if (info !== undefined) {
          console.log(info.message);
          res.status(401).send(info.message);
        } else if (user.is_admin) {
            User.findOne({
              where: {
                username: req.body.username,
              },
            }).then((userInfo) => {
              if (userInfo != null) {
                console.log('user found in db');
                userInfo
                  .update({
                    is_admin: true
                  })
                  .then(() => {
                    console.log('user promoted');
                    res.status(200).send({ auth: true, message: 'user promoted' });
                  });
              } else {
                console.error('no user exists in db to promote');
                res.status(401).send('no user exists in db to promote');
              }
            });
        } else {
          console.error('Unauthorized action');
          res.status(403).send('you are not an admin');
        }
      })(req, res, next);
    });
  };
  