from flask import Flask, flash
from flask import session, request, make_response, render_template, redirect, url_for, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import secure_filename
from subprocess import Popen, PIPE
import os, hashlib

app = Flask(__name__)
app.secret_key = 'L;Ai:x<dom.;Q$Uyibdi&?Tb2Tq>@J#F'
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def get_exif():
  imagelist = os.listdir("./uploads/")
  results = []
  output = ""
  for i in imagelist:
    i = "./uploads/" + i
    p = Popen(["exiftool", i], stdout=PIPE)
    (output, err) = p.communicate()
    exit_code = p.wait()
    if exit_code == 0:
      results.append(output)
    os.remove(i)

  return output
 
@app.route("/", methods=['GET', 'POST'])
def index():
  return render_template('index.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
	return render_template('register.html')

@app.route("/register/submit", methods=['GET', 'POST'])
def register_submit():
  file = request.files['profile']
  if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  
  return render_template('submit.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
  if User.login(request.form['user'], request.form['password']):
    session['username'] = request.form['user']
    response = make_response(redirect(url_for('admin')))
    return response
  else:
    flash(u'Incorrect username or password. If you believe this should be valid, it may be your account has not been approved.', 'error')
    return redirect(url_for('index'))

@app.route("/logout", methods=['GET', 'POST'])
def logout():
  session.pop("username", None)
  response = make_response(redirect(url_for('index')))
  return response

@app.route("/c54c497c-38b6-408a-a597-5aa25bd0bd88")
def process():
  return str(get_exif())

@app.route("/admin", methods=['GET', 'POST'])
def admin():
  if session.has_key('username') and session['username'] == 'admin':
    return render_template('admin.html')
  else:
    return redirect(url_for('index'))

@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('fonts', path)

if __name__ == "__main__":
  db.create_all() 
  app.threaded = True 
  app.run(
    host="0.0.0.0",
    port=5001
  )
