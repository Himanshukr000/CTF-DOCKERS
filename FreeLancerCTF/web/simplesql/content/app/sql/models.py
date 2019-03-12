from ..app import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.UnicodeText(5000))
    password = db.Column(db.UnicodeText(5000))
