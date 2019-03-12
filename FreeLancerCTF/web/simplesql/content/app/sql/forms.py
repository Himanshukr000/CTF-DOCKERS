from flask_wtf import Form
from wtforms import TextField, SubmitField, TextAreaField

class login_form(Form):
    username = TextField("username")
    password = TextField("password")
    submit = SubmitField("Send")
