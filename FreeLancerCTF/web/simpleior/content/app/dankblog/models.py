from ..app import db

class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.UnicodeText(500), index=True)
