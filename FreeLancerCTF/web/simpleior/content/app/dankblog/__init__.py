from flask import Blueprint

dankblog = Blueprint('dankblog',
    __name__,
    template_folder='templates',
    static_folder='static')

from . import views
