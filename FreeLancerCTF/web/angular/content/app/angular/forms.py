import FlaskForm
from wtforms import TextField, SubmitField
from wtforms import validators

class angular_form(Form):
    content = TextField("content")
    submit = SubmitField("Send")
