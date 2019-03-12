/* eslint-disable no-console */
import passport from 'passport';
import User from '../sequelize';
import sha1 from 'node-sha1';
import atob from 'atob';

/**
 * @swagger
 * /updateUser:
 *   put:
 *     tags:
 *       - Users
 *     name: Update User
 *     summary: Update user info
 *     security:
 *       - bearerAuth: []
 *     consumes:
 *       - application/json
 *     produces:
 *       - application/json
 *     parameters:
 *       - name: body
 *         in: body
 *         schema:
 *           $ref: '#/definitions/User'
 *           type: object
 *           properties:
 *             first_name:
 *               type: string
 *             last_name:
 *               type: string
 *             email:
 *               type: string
 *             username:
 *               type: string
 *         required:
 *           - username
 *     responses:
 *       '200':
 *         description: User info updated
 *       '403':
 *         description: No authorization / user not found
 */

function checkHash(content, checksum) {
  try{
    return checksum === sha1(Buffer.concat([new Buffer('zZSfx7rlDZxdUvANh12MzYAaiT9XHkiV'), new Buffer(content, 'base64')]));
  }catch(e){
    return false;
  }
}

module.exports = (app) => {
  app.put('/updateUser', (req, res, next) => {
    passport.authenticate('jwt', { session: false }, (err, user, info) => {
      if (err) {
        console.error(err);
      }
      if (info !== undefined) {
        console.error(info.message);
        res.status(403).send(info.message);
      } else {
        if (!checkHash(req.body.status, req.body.checksum)){
          console.error('invalid request');
          res.status(401).json('your checksum is invalid');
        } else if (user.username !== req.body.username) {
          console.error('unauthorized update');
          res.status(401).json('you are unauthorized to perform this change');
        }else{
          req.body.status = atob(req.body.status);
          User.findOne({
            where: {
              username: req.body.username,
            },
          }).then((userInfo) => {
            if (userInfo != null) {
              console.log('user found in db');
              userInfo
                .update({
                  first_name: req.body.first_name,
                  last_name: req.body.last_name,
                  email: req.body.email,
                  status: req.body.status
                })
                .then(() => {
                  console.log('user updated');
                  res.status(200).send({ auth: true, message: 'user updated' });
                });
            } else {
              console.error('no user exists in db to update');
              res.status(401).send('no user exists in db to update');
            }
          });
        }
      }
    })(req, res, next);
  });
};
