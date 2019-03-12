# -*- coding: utf-8 -*-
from ..app import db
from flask_user import UserManager, UserMixin, current_user
import json
from .products import mokepon

product_json = dict()
for prod in mokepon:
    print prod
    product_json.update({prod[1].replace("'", "`"): 0})

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)

    # User authentication information
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    pokedollars = db.Column(db.Integer(), server_default='9999')
    realdollars = db.Column(db.Integer(), server_default='0')
    pokeballs = db.Column(db.LargeBinary(1500), server_default=json.dumps(product_json).decode('utf-8'))
    flagstring = db.Column(db.String(128), server_default='')

    def get_id(self):
        return unicode(self.id)

    def is_active(self):
        return True

class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(1000))
    img = db.Column(db.String(100))
    price = db.Column(db.Integer())
    currency = db.Column(db.String(50))
