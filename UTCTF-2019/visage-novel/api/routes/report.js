import passport from 'passport';
import User from '../sequelize';

module.exports = (app) => {
    app.get('/report', (req, res, next) => {
      passport.authenticate('jwt', { session: false }, (err, user, info) => {
        if (err) {
          console.log(err);
        }
        if (info !== undefined) {
          console.log(info.message);
          res.status(401).send(info.message);
        } else {
          User.findOne({
            where: {
              username: req.query.username,
            },
          }).then((userInfo) => {
          if (userInfo != null) {
            console.log('user found in db');
            userInfo
              .update({
                reported: true
              })
              .then(() => {
                console.log('user reported');
                res.status(200).send({ auth: true, message: 'User reported! An admin should take a look at this within 10 minutes.' });
              });
            } else {
              console.error('no user exists in db to report');
              res.status(401).send('no user exists in db to report');
            }
          });
        }
      })(req, res, next);
    });
  };