from flask import Flask

class ConfigClass(object):
    # Flask settings
    SECRET_KEY                      = 'idgafabotusecuresecretshahahahah'
    USER_ENABLE_EMAIL               = False
    USER_ENABLE_CONFIRM_EMAIL       = False
    USER_ENABLE_FORGOT_PASSWORD     = False
    USER_ENABLE_LOGIN_WITHOUT_CONFIRM = True
    USER_AUTO_LOGIN                  = True
    USER_AUTO_LOGIN_AFTER_CONFIRM    = USER_AUTO_LOGIN
    USER_AUTO_LOGIN_AFTER_REGISTER   = USER_AUTO_LOGIN
    USER_AUTO_LOGIN_AFTER_RESET_PASSWORD = USER_AUTO_LOGIN
    USER_PASSWORD_HASH_MODE = 'plaintext'

app = Flask(__name__)
app.config.from_object(__name__+'.ConfigClass')

from pkls import pkls
app.register_blueprint(pkls)

