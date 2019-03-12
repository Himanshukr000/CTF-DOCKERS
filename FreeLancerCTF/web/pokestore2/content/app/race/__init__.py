from flask import Blueprint

race = Blueprint('race',
    __name__,
    template_folder='templates',
    static_folder='static')

from . import init_products
race.record_once(init_products.do)

from . import views
