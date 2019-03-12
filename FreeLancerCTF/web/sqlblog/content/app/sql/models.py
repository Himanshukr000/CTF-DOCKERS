from ..app import db

class Post(db.Model):
    id = db.Column(db.UnicodeText(1000))
    title = db.Column(db.UnicodeText(5000), index=True)
    content = db.Column(db.UnicodeText(5000), index=True)
    hash = db.Column(db.UnicodeText(1000))
    uid = db.Column(db.UnicodeText(10), primary_key=True)
    time = db.Column(db.Integer())
    hidden = db.Column(db.UnicodeText(5000))

class FLAG(db.Model):
    __tablename__ = 'wowsupersecrettablename'
    flag = db.Column(db.UnicodeText(100), primary_key=True)
