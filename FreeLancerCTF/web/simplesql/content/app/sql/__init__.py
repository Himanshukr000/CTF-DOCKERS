from flask import Blueprint

sql = Blueprint('sql',
    __name__,
    template_folder='templates',
    static_folder='static')

from . import views
