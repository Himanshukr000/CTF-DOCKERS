from flask import Flask, flash
from flask import session, request, make_response, render_template, redirect, url_for, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import secure_filename
from subprocess import Popen, PIPE
import os, hashlib, base64

app = Flask(__name__)
app.secret_key = 'dajXDhpwJvROI1c8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
hash_secret = '5Y2g0rt6NbYzmwQF'

db = SQLAlchemy(app)
db.create_all()

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user = db.Column(db.String(255), unique=True)
  password = db.Column(db.String(255), unique=False)

  def __init__(self, username, password):
    self.user = username
    self.password = hashlib.sha256(password).hexdigest()

  @classmethod
  def login(self, username, password):
    result = User.query.filter_by(user=username).first()
    calc_pass = hashlib.sha256(password).hexdigest()
    if result and result.password == calc_pass:
      return True
    else:
      return False

def check_sig(signature):
  d = base64.b64decode(signature)
  #print "d is {}".format(d)
  # signature:username:0........:1 (sig hex encoded)
  split_vars = d.split(":")
  #print "split as {}".format(split_vars)
  #print
  # signature, username, 0..., 1
  sig = split_vars[0] # signature
  username = split_vars[1] # username
  role = split_vars[-1] # fake role
  h_string = hash_secret + ''.join(split_vars[1:])  # this needs to be the same as before with modified data
  #print "h_string being hashed... {}".format(h_string)
  h = hashlib.sha512(h_string).digest() #
  en = h.encode('hex')
  #print "signature calculated {}".format(en)
  #print "signature recieved.. {}".format(sig)
  if sig == en:
    return True
  else:
    return False

def generate_sig(username):
  # Here we need to generate a signature string so that when decoded, appears as
  # [Signature][Data] where [Data] is made up of [Username:Role]
  # id[0] will always be signature, id[1] will always be username (inconsequential), id[-1] will always be role
  # with the hash extension attack, the cookie will become [signature]:[username...................:1] with the same signature as [signature]:[username]:0
  # SIG = H(SECRET||USERNAME||ROLE)
  # hashsecret|username|:0
  h_string = hash_secret + username + "0"
  # print "string being hashed: {}".format(h_string)
  h = hashlib.sha512(h_string).digest()
  en = h.encode('hex')
  return base64.b64encode(en + ":" + username + ":0")

@app.route("/", methods=['GET', 'POST'])
def index():
  return render_template('index.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
  return render_template('register.html')

@app.route("/register/submit", methods=['GET', 'POST'])
def register_submit():
  if request.form['password'] != request.form['confirm-password']:
    flash('Passwords did not match')
    return redirect(url_for('index'))
  else:
    user = User(request.form['username'], request.form['password'])
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
  if User.login(request.form['user'], request.form['password']):
    response = make_response(redirect(url_for('profile')))
    response.set_cookie('id', generate_sig(request.form['user']))
    return response
  else:
    flash(u'Incorrect username or password.')
    return redirect(url_for('index'))

@app.route("/profile", methods=['GET', 'POST'])
def profile():
  if request.cookies.get('id'):
    if check_sig(request.cookies.get('id')):
      username = base64.b64decode(request.cookies.get('id')).split(":")[1]
      return render_template('profile.html', username=username)

  return redirect(url_for('index'))

@app.route("/logout", methods=['GET', 'POST'])
def logout():
  response = make_response(redirect(url_for('index')))
  response.set_cookie('id', '')
  return response

@app.route("/admin", methods=['GET', 'POST'])
def admin():
  if request.cookies.get('id'):
    if check_sig(request.cookies.get('id')):
      if base64.b64decode(request.cookies.get('id')).split(":")[-1] == "1":
        return render_template('admin.html')

  return redirect(url_for('index'))

@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('/home/ctf/hash/fonts', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('/home/ctf/hash/templates/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('/home/ctf/hash/templates/css', path)

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('/home/ctf/hash/templates/assets', path)

if __name__ == "__main__":
  db.create_all()
  app.threaded = True
  app.run(
    host="0.0.0.0",
    port=10000
  )
