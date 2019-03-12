from flask import current_app
from json import dumps

def jsonify(json_dict, status_code=200):
    response = current_app.make_response(dumps(json_dict))
    response.status_code = status_code
    response.content_type = 'application/json'
    return response

