from flask import request, session, redirect, render_template, make_response
from flask_sqlalchemy import sqlalchemy
from flask_user import SQLAlchemyAdapter, UserManager, current_user
from flask_login import LoginManager, login_user, logout_user, AnonymousUserMixin
from . import angular
from .models import User
from .helpers import jsonify
from .mixins import *
from ..app import db, app

db_adapter = SQLAlchemyAdapter(db, User)        # Register the User model
user_manager = UserManager(db_adapter, app,
                           password_validator=lambda x, y: None)
login_manager = LoginManager()
login_manager.init_app(app)

flag1 = 'FCTF{768a6a9ca8dffbcc1251b127ddd5202b}'
flag2 = 'FCTF{dbb1791dee3ef08367de135f0f3b7161}'

secret_role = "Conquerer of AOS and all concurrency models"

@angular.route('/', methods=['GET'])
def angular_home():
    return render_template('index.html')

@login_manager.user_loader
def get_user(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve
    """
    return User.query.filter(User.username == user_id).first()

@angular.route('/flag', methods=['GET'])
def angular_get_flag():
    if (current_user.role == "Conquerer of AOS and all concurrency models"):
        return jsonify({"message": "Congratulations: {}".format(flag1)})
    else:
        return jsonify({"message": "Your permissions are insufficient. Come back when you are almighty"},401)

@angular.route('/whoami', methods=['GET'])
def angular_whoami():
    username = 'anon'
    role = 'nobody'
    if (current_user.is_authenticated):
        username = current_user.username
        role = current_user.role
    return jsonify({'message': 'you are {}, who is {}'.format(username, role)})

@angular.route('/user/all', methods=['GET', 'POST'])
@login_required
def angular_user_all():
    users = User.query.filter(User.role != secret_role).all()
    return jsonify([user.json() for user in users])

def dict_to_user(data):
    #data:dict -> User
    new_user = User(username=data['username'], password=data['password'])
    data.pop('username')
    data.pop('password')
    for k, v in data.items():
        try:
            getattr(User, k)
        except:
            pass
        else:
            setattr(new_user, k, v)
    return new_user

@angular.route('/user/create', methods=['POST'])
def angular_user_create():
    post_data = request.get_json()
    if (('username' not in post_data or 'password' not in post_data) or
       (post_data['username'] == '' or post_data['password'] == '')):
        return jsonify({'message': 'You did not provide a username and or password'}, 400)

    new_user = dict_to_user(post_data)
    db.session.add(new_user)
    try:
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        return jsonify({'message': 'A user already exists with that username or id'}, 400)
    except:
        raise
    else:
        return jsonify({'message': 'User {} created'.format(new_user.username)}, 200)

@angular.route('/user/edit', methods=['POST'])
@login_required
def angular_user_edit():
    post_data = request.get_json()
    if ('username' not in post_data or post_data['username'] == ''):
        return jsonify({'message': 'You did not provide a username'}, 400)

    if ('role' in post_data):
        return jsonify({'message': 'You cannot modify your role in this grand plan.'}, 400)

    if ('id' in post_data):
        return jsonify({'message': 'Your ID is fixed. Stop trying to change it.'}, 400)

    if (current_user.username != post_data['username']):
        return jsonify({'message': 'You cannot modify this record.'}, 401)

    if ('password' in post_data):
        current_user._set_password(post_data['password'])
        post_data.pop('password')

    for k,v in post_data.items():
        try:
            getattr(User, k)
        except:
            pass
        else:
            setattr(current_user, k, v)

    db.session.add(current_user)
    try:
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        return jsonify({'message': 'Failed to update your request'}, 400)
    except:
        raise
    else:
        return jsonify({'message': 'User details updated', 'user': current_user.json()}, 200)

@angular.route('/user/login', methods=['POST'])
def angular_user_login():
    post_data = request.get_json()
    if (('username' not in post_data or 'password' not in post_data) or
       (post_data['username'] == '' or post_data['password'] == '')):
        return jsonify({'message': 'You did not provide a username and or password'}, 400)

    user = User.query.filter_by(username=post_data['username']).first()
    if (user and user.check_password(post_data['password'])):
        user.authenticated = True
        db.session.add(user)
        db.session.commit()
        login_user(user)
    else:
        return jsonify({'message': 'Invalid username and password'}, 401)

    return jsonify({'message': 'User logged in', 'user': user.json()}, 200)

@angular.route('/user/logout', methods=['GET'])
@login_required
def angular_user_logout():
    current_user.authenticated = False
    db.session.add(current_user)
    db.session.commit()
    logout_user()
    return jsonify({'message': 'User logged out'}, 200)

@angular.route('/user/<int:user_id>', methods=['GET'])
@login_required
def angular_get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if (user):
        return jsonify({'message': 'Here you go', 'user':user.json()})
    return jsonify({'message': 'No user found with that ID'}, 400)

@angular.route('/<query>', methods=['GET'])
def angular_error_catch(query):
    query = query.replace("script", "XSS ATTEMPT DETECTED")
    query = query.replace('<', '&lt;')
    query = query.replace('>', '&gt;')
    return render_template('error.html', err = query)
