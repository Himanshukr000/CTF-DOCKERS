import Sequelize from 'sequelize';
import UserModel from './models/user';

const sequelize = new Sequelize('users', 'MYSQL_USER', 'MYSQL_PASS', {
  host: 'db',
  dialect: 'mysql',
  operatorsAliases: false
});

const User = UserModel(sequelize, Sequelize);

sequelize.sync().then(() => {
  // eslint-disable-next-line no-console
  console.log('Users db and user table have been created');
});

module.exports = User;
