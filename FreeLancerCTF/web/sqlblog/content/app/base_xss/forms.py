from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms import validators

class base_xss_form(Form):
    content = TextField("content")
    submit = SubmitField("Send")
