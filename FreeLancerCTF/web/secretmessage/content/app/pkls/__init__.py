from flask import Blueprint

pkls = Blueprint('pkls',
    __name__,
    template_folder='templates',
    static_folder='static')

from . import views
