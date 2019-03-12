from flask import Flask, flash
from flask import session, request, make_response, render_template, redirect, url_for, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
import os, sys, hmac, base64, pickle, hashlib, StringIO

app = Flask(__name__)
app.secret_key = ':n7!E|=WZf"&}N5O4xxdS">?7l8NuFR?'
hmac_secret = 'XQRm$VKq]cxyU==]:z5!c}<>|>s{ehR.'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)
db.create_all()

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user = db.Column(db.String(255), unique=True)
  email = db.Column(db.String(255), unique=False)
  password = db.Column(db.String(255), unique=False)
  
  def __init__(self, username, password, email):
    self.user = username
    self.email = email
    self.password = hashlib.sha256(password).hexdigest()

  @classmethod
  def login(self, username, password):
    result = User.query.filter_by(user=username).first()
    calc_pass = hashlib.sha256(password).hexdigest()
    if result and result.password == calc_pass:
      return True
    else:
      return False
  
def generate_sig(username):
  h = hmac.new(hmac_secret, username, hashlib.sha256)
  c = pickle.dumps(username + ":" + h.hexdigest())
  return base64.encodestring(c)

def check_sig(username, h):
  h_new = hmac.new(hmac_secret, username, hashlib.sha256).hexdigest()
  if h == h_new:
    return True

  return False 

@app.route("/", methods=['GET', 'POST'])
def index():
  if request.cookies.get('r'):
    e = base64.decodestring(request.cookies.get('r'))
    c = pickle.loads(e)
    name, h = c.split(":") 
    if check_sig(name, h):
      session['username'] = name
      response = make_response(redirect(url_for('profile')))
      return response
  
  return render_template('index.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
  if request.form['password'] != request.form['confirm-password']:
    flash('Passwords did not match')
    return redirect(url_for('index'))
  else:
    user = User(request.form['username'], request.form['password'], request.form['email'])
    db.session.add(user)
    try:
      db.session.commit()
    except:
      flash('Could not create user')
      return redirect(url_for('index'))
    flash('User created, you may now login')

  return redirect(url_for('index'))

@app.route("/login", methods=['GET', 'POST'])
def login():
  if User.login(request.form['username'], request.form['password']):
    session['username'] = request.form['username']
    response = make_response(redirect(url_for('profile')))
    if ('remember' in request.form) and request.form['remember']:
      response.set_cookie('r', generate_sig(request.form['username']))
    return response
  else:
    flash('Dirty Hacker')
    return redirect(url_for('index'))

@app.route("/logout", methods=['GET', 'POST'])
def logout():
  session.pop("username", None)
  response = make_response(redirect(url_for('index')))
  response.set_cookie('r','')
  return response

@app.route("/profile", methods=['GET', 'POST'])
def profile():
  if session.has_key('username'):
    username = session['username']
    return render_template('profile.html', username=username)
  else:
    return redirect(url_for('index'))

@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('fonts', path)

if __name__ == "__main__":
  db.create_all()  
  app.run(
    host="0.0.0.0",
    port=5000
  )
