from flask_wtf import Form
from wtforms import TextField, SubmitField

class messsage_form(Form):
    secret_key = TextField("secret_key")
    submit = SubmitField("Send")

