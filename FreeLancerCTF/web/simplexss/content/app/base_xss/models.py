from ..app import db

class Xss(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.UnicodeText(500), index=True)
    content = db.Column(db.UnicodeText(500), index=True)
