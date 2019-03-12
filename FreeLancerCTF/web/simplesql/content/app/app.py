from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager, SQLAlchemyAdapter

class ConfigClass(object):
    # Flask settings
    SECRET_KEY                      = 'idgafabotusecuresecretshahahahah'
    SQLALCHEMY_DATABASE_URI         = 'sqlite:///basic_app.sqlite'
    SQLALCHEMY_ECHO                 = True
    USER_ENABLE_EMAIL               = False
    USER_ENABLE_CONFIRM_EMAIL       = False
    USER_ENABLE_FORGOT_PASSWORD     = False
    USER_ENABLE_LOGIN_WITHOUT_CONFIRM = True
    USER_AUTO_LOGIN                  = True
    USER_AUTO_LOGIN_AFTER_CONFIRM    = USER_AUTO_LOGIN
    USER_AUTO_LOGIN_AFTER_REGISTER   = USER_AUTO_LOGIN
    USER_AUTO_LOGIN_AFTER_RESET_PASSWORD = USER_AUTO_LOGIN
    USER_PASSWORD_HASH_MODE = 'plaintext'

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(__name__+'.ConfigClass')

db.init_app(app)

import models
with app.app_context():
    db.create_all()

from sql import sql
app.register_blueprint(sql)

