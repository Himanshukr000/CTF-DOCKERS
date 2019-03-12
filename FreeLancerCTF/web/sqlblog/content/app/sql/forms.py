from flask_wtf import Form
from wtforms import TextField, SubmitField, TextAreaField

class post_form(Form):
    title = TextField("title")
    content = TextAreaField("content")
    hidden = TextField("hidden")
    submit = SubmitField("Send")
