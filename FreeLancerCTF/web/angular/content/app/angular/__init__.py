from flask import Blueprint

angular = Blueprint('angular',
    __name__,
    template_folder='templates',
    static_folder='static')

from . import init_angular
angular.record_once(init_angular.do)

from . import views
