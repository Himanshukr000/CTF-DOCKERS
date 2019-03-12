from .models import User
from ..app import db, app

def do(derp):
    with app.app_context():
        if (db.session.query(User).filter_by(username='gernot').first() == None):
            gernot = User(username='gernot', password='9cc9e32de1071f9c8c3b48ad0e9a532d', role="Conquerer of AOS and all concurrency models")
            db.session.add(gernot)
            db.session.commit()
