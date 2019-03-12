from .models import Product
from ..app import db
from ..app import app
from products import mokepon

def do(derp):
    with app.app_context():
        if (db.session.query(Product).count() != len(mokepon)):
            for poke in mokepon:
                ball = Product(price = poke[0], name = poke[1], img = poke[2], desc = poke[3], currency = 'poke')
                db.session.add(ball)
            db.session.commit()
