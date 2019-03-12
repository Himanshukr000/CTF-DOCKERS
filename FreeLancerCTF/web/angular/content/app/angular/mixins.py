from functools import wraps
from flask import current_app
from flask.ext.login import current_user
from .helpers import jsonify


def _call_or_get(function_or_property):
    return function_or_property() if callable(function_or_property) else function_or_property


def login_required(func):
    """ This decorator ensures that the current user is logged in before calling the actual view.
        Calls the unauthorized_view_function() when the user is not logged in."""
    @wraps(func)
    def decorated_view(*args, **kwargs):
        # User must be authenticated
        if not _call_or_get(current_user.is_authenticated):
            # Redirect to unauthenticated page
            print("attempted illegal access")
            return jsonify({'message': 'You have to be logged in to access this'}, 401)

        # Call the actual view
        return func(*args, **kwargs)
    return decorated_view

def donny_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not (_call_or_get(current_user.is_authenticated) and current_user.username == 'donny'):
            return jsonify({'message': 'This is not in the scope of the CTF Challenge'}, 401)

        # Call the actual view
        return func(*args, **kwargs)
    return decorated_view

