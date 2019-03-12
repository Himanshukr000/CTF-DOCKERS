from flask import Blueprint

base_xss = Blueprint('base_xss',
    __name__,
    template_folder='templates',
    static_folder='static')

from . import views
