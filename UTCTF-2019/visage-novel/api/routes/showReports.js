/* eslint-disable no-console */
import User from '../sequelize';

module.exports = (app) => {
  app.post('/showReports', (req, res, next) => {
    console.log(req);
    if(req.body.secret !== 'bekM29zxfm'){
      res.status(404).send('This is outside of the problem and probably won\'t help you solve it either');
      return;
    }

    User.findAll({
      where: {
        reported: true
      }
    }).then((users) => {
      res.status(200).send(users.map((user) => user.username));
      users.forEach((user) => {
        user.update({reported: false});
      });
    });
  });
};
