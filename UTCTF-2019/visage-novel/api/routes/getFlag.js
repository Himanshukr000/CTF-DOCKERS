/* eslint-disable no-console */
import passport from 'passport';

module.exports = (app) => {
    app.get('/getFlag', (req, res, next) => {

      passport.authenticate('jwt', { session: false }, (err, user, info) => {
        if (err) {
          console.log(err);
        }

        if (info !== undefined) {
          console.log(info.message);
          res.status(401).send(info.message);
        } else if (user.is_admin) {
            res.status(200).send({flag: 'utflag{2_be_fair_u_need_A_v_hi_iq_to_do_xss}'});
        } else {
          console.error('Unauthorized action');
          res.status(403).send('you are not an admin');
        }
      })(req, res, next);
    });
  };
  