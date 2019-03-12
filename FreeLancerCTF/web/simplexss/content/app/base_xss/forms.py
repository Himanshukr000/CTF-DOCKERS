from flask_wtf import Form
from wtforms import TextField, SubmitField, TextAreaField

class base_xss_form(Form):
    title = TextField("title")
    content = TextAreaField("content")
    submit = SubmitField("Send")
