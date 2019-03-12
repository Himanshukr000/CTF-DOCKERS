from flask import Flask, flash
from flask import session, request, make_response, render_template, redirect, url_for, send_from_directory, abort, Markup
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import secure_filename
from subprocess import Popen, PIPE
import os, hashlib, base64, random, string
from pprint import pprint

app = Flask(__name__)
app.secret_key = 'RI3Ij80NKfDuer15'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'

db = SQLAlchemy(app)
db.create_all()

class User(db.Model):
  __tablename__ = 'users'
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

class BugReport(db.Model):
  __tablename__ = 'bugs'
  id = db.Column(db.Integer, primary_key=True)
  author = db.Column(db.String(255), unique=False)
  content = db.Column(db.String(65536), unique=False)

  def __init__(self, author, content):
    self.author = author
    self.content = content

@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)

def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = some_random_string()
    return session['_csrf_token']

def some_random_string():
  return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

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
    session['username'] = request.form['user']
    response = make_response(redirect(url_for('profile')))
    return response
  else:
    flash(u'Incorrect username or password.')
    return redirect(url_for('index'))

@app.route("/admin/stats", methods=['GET', 'POST'])
def stats():
  if session.has_key('username') and session['username'] == "admin":
    session['num1'] = random.randint(1,1000)
    session['num2'] = random.randint(1,1000)
    return render_template('stats.html', num1=session['num1'], num2=session['num2'])

  return redirect(url_for('index'))

@app.route("/admin/stats/retrieve", methods=['GET', 'POST'])
def retrieve():
  if session.has_key('username') and session['username'] == "admin":
    sup_ans = request.form['captcha']
    ans = session['num1'] + session['num2']
    if int(ans) == int(sup_ans):
      query = request.form['query']
      result = db.engine.execute("select * from users where user = '{}';".format(query))
      return render_template('done.html', results=result)

  return redirect(url_for('index'))

@app.route("/admin/report", methods=['GET', 'POST'])
def admin_report():
  if session.has_key('username') and session['username'] == "admin":
    results = BugReport.query.all()    
    return render_template('admin_report.html', results=results)

  return redirect(url_for('index'))

@app.route("/admin/clear", methods=['GET', 'POST'])
def admin_clear():
  if session.has_key('username') and session['username'] == "admin":
    BugReport.query.delete()
    db.session.commit()
    flash(u'All reports cleared')
    return redirect(url_for('admin'))

  return redirect(url_for('index'))
@app.route("/report", methods=['GET', 'POST'])
def report():
  if session.has_key('username'):
    return render_template('report.html')

  return redirect(url_for('index'))

@app.route("/profile", methods=['GET', 'POST'])
def profile():
  if session.has_key('username'):
    return render_template('profile.html')
    
  return redirect(url_for('index'))

@app.route("/profile/submit", methods=['GET', 'POST'])
def profile_submit():
  if session.has_key('username'):
    report = BugReport(session['username'], request.form['submission'])
    db.session.add(report)   
    try:
      db.session.commit()
    except:
      flash('Could not submit report')
      return redirect(url_for('profile'))
    
    flash('Report Submitted. Our staff will review shortly.')
    return redirect(url_for('profile'))

  return redirect(url_for('index'))

@app.route("/logout", methods=['GET', 'POST'])
def logout():
  session.pop("username", None)
  response = make_response(redirect(url_for('index')))
  return response

@app.route("/admin", methods=['GET', 'POST'])
def admin():
  if session.has_key('username') and session['username'] == "admin":
    return render_template('admin.html')

  return redirect(url_for('index'))

@app.route('/fonts/<path:path>')
def send_fonts(path):
  return send_from_directory('/home/ctf/hopscotch/fonts', path)

if __name__ == "__main__":
  db.create_all()
  app.jinja_env.globals['csrf_token'] = generate_csrf_token
  app.threaded = True
  app.SESSION_COOKIE_HTTPONLY = True 
  app.run(
    host="0.0.0.0",
    port=10000
  )
