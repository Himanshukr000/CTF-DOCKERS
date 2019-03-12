from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager, SQLAlchemyAdapter
from flask_bcrypt import Bcrypt
from flask_cors import CORS, cross_origin

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
    USER_PASSWORD_HASH              = 'bcrypt'
    USER_PASSWORD_HASH_MODE = 'sha256'
    SESSION_COOKIE_HTTPONLY     = False

db = SQLAlchemy()

app = Flask(__name__, static_folder=None)
CORS(app, supports_credentials=True, allow_headers=['set-cookie'])
app.config.from_object(__name__+'.ConfigClass')

db.init_app(app)
bcrypt = Bcrypt(app)

from . import models
with app.app_context():
    db.create_all()

from .angular import angular
app.register_blueprint(angular)

