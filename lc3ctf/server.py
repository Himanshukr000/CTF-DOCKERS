#!/usr/bin/env python3

"""server.py -- the main flask server module"""

import dataset
import json
import random
import time
import re
import urllib
import requests

from base64 import b64decode
from functools import wraps

from flask import Flask
from flask import jsonify
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from lc3achi.lc3achi import chkachi
from lc3achi.lc3achi import lc3_achivements

app = Flask(__name__, static_folder='static', static_url_path='')

langfile = 'lang.json'
configfile = 'config.json'
dbfile = 'sqlite:///ctf.db'


def login_required(f):
    """Ensures that an user is logged in"""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('error', msg='login_required'))
        return f(*args, **kwargs)
    return decorated_function


def get_user():
    """Looks up the current user in the database"""

    db = dataset.connect(dbfile)
    login = 'user_id' in session
    if login:
        user = db['users'].find_one(id=session['user_id'])
        db.executable.close()
        return (True, user)

    db.executable.close()
    return (False, None)


def get_task(task_id):
    """Finds a task with a given category and score"""

    if not task_id.isnumeric():
        return None
    db = dataset.connect(dbfile)
    tasks = list(db.query('''select t.* from tasks t, categories c, cat_task ct
        where t.id = ct.task_id and c.id = ct.cat_id
        and t.id=:tid''',
                          tid=task_id))
    if tasks:
        task = tasks[0]
    else:
        task = None
    db.executable.close()
    return task


def get_flags():
    """Returns the flags of the current user"""

    db = dataset.connect(dbfile)
    flags = db.query('''select f.task_id from flags f
        where f.user_id = :user_id''',
                     user_id=session['user_id'])
    flag = [f['task_id'] for f in list(flags)]
    db.executable.close()
    return flag


def register_login(sno):
    """Register and login user"""

    db = dataset.connect(dbfile)
    user_found = db['users'].find_one(sno=sno)
    if not user_found:
        new_user = dict(hidden=0, sno=sno, username=sno)
        db['users'].insert(new_user)

    user = db['users'].find_one(sno=sno)
    session['user_id'] = user['id']
    db.executable.close()


@app.errorhandler(404)
def not_found(e):
    """Handle 404 page"""

    return redirect(url_for('error', msg='404'))


@app.route('/error/<msg>')
def error(msg):
    """Displays an error message"""

    if msg in lang['error']:
        error = lang['error'][msg]
    else:
        error = lang['error']['unknown']

    login, user = get_user()

    render = render_template('frame.html', lang=lang, page='error.html',
                             message=error['msg'], login=login, user=user, active=default_active)
    return make_response(render), error['ec']


@app.route('/login')
def login():
    """Redirect to login page"""

    return redirect("https://acsa.ustc.edu.cn/ics/lc3ctf.php")


@app.route('/login/<ticket>')
def login_cas(ticket):
    """Check user"""

    if config['debug']:
        register_login(ticket)
        return redirect(url_for('tasks'))
    if len(ticket) != 35:
        return redirect(url_for('login'))

    pattern = re.compile(r'^ST-\w{32}$')
    if pattern.match(ticket) is None:
        return redirect(url_for('login'))
    # use ticket
    info = None
    API_URL = "https://passport.ustc.edu.cn/serviceValidate?ticket={ticket}&service={service}"
    service_url = urllib.parse.quote_plus(
        "https://acsa.ustc.edu.cn/ics/lc3ctf.php")
    api_url = API_URL.format(ticket=ticket, service=service_url)
    try:
        r = requests.get(api_url)
        info = r.text
    except:
        return redirect(url_for('login'))

    # format return info
    if info:
        pattern = re.compile(r'<cas:user>([a-zA-Z]{2}\d{8})</cas:user>')
        match = pattern.search(info)
        if match:
            sno = match.group(1).upper()
            register_login(sno)
            return redirect(url_for('tasks'))
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


@app.route('/tasks')
@login_required
def tasks():
    """Displays all the tasks in a grid"""

    login, user = get_user()
    flags = get_flags()
    active = default_active.copy()
    active['tasks'] = 'active'

    db = dataset.connect(dbfile)
    categories = list(db['categories'])

    tasks = db.query('''select c.id as cat_id, t.id as id, c.short_name as cat,
        t.score, t.row, t.name from categories c, tasks t, cat_task c_t
        where c.id = c_t.cat_id and t.id = c_t.task_id''')
    tasks = list(tasks)

    grid = []
    # Find the max row number
    max_row = max(t['row'] for t in tasks)

    for row in range(max_row + 1):

        row_tasks = []
        for cat in categories:

            # Find the task with the correct row
            for task in tasks:
                if task['row'] == row and task['cat_id'] == cat['id']:
                    break
            else:
                task = None

            row_tasks.append(task)

        grid.append(row_tasks)

    db.executable.close()
    # Render template
    render = render_template('frame.html', lang=lang, page='tasks.html',
                             login=login, user=user, categories=categories, grid=grid,
                             flags=flags, active=active)
    return make_response(render)


@app.route('/tasks/<cat>/<task_id>')
@login_required
def task(cat, task_id):
    """Display task"""

    login, user = get_user()
    active = default_active.copy()
    active['tasks'] = 'active'

    task = get_task(task_id)
    if not task:
        return redirect(url_for('error', msg='task_not_found'))

    flags = get_flags()
    task_done = task['id'] in flags

    db = dataset.connect(dbfile)
    solutions = db['flags'].find(task_id=task['id'])
    solutions = len(list(solutions))
    db.executable.close()

    # Render template
    render = render_template('frame.html', lang=lang, page='task.html',
                             task_done=task_done, login=login, solutions=solutions,
                             user=user, category=cat, task=task, score=task['score'], active=active)
    return make_response(render)


@app.route('/submit/<task_id>/<flag>')
@login_required
def submit(task_id, flag):
    """Handles the submission of flags"""

    task = get_task(task_id)
    if not task:
        return redirect(url_for('error', msg='task_not_found'))
    flags = get_flags()
    task_done = task['id'] in flags

    db = dataset.connect(dbfile)
    result = {'success': False, 'new_achivement': False}
    if not task_done and task['flag'] == b64decode(flag).decode('utf-8'):

        timestamp = int(time.time() * 1000)

        # Insert flag
        new_flag = dict(task_id=task['id'], user_id=session['user_id'],
                        score=task['score'], timestamp=timestamp)
        db['flags'].insert(new_flag)

        result['success'] = True

    if chkachi(dbfile, 'submit', correct=result['success'], real_flag=task['flag'],
               flag=b64decode(flag).decode('utf-8')):
        result['new_achivement'] = True
    db.executable.close()
    return jsonify(result)


@app.route('/scoreboard')
@login_required
def scoreboard():
    """Displays the scoreboard"""

    active = default_active.copy()
    active['scoreboard'] = 'active'
    db = dataset.connect(dbfile)
    login, user = get_user()
    scores = db.query('''select u.username, ifnull(sum(f.score), 0) as score,
        max(timestamp) as last_submit from users u left join flags f
        on u.id = f.user_id where u.hidden = 0 group by u.username
        order by score desc, last_submit asc''')

    scores = list(scores)
    db.executable.close()

    # Render template
    render = render_template('frame.html', lang=lang, page='scoreboard.html',
                             login=login, user=user, scores=scores, active=active)
    return make_response(render)


@app.route('/achivements')
@login_required
def achivements():
    """Displays the achivements menu"""

    login, user = get_user()
    active = default_active.copy()
    active['achivements'] = 'active'

    db = dataset.connect(dbfile)
    achis = db.query('''select a.achi_id from achivements a
                where a.user_id = :user_id''', user_id=session['user_id'])
    achi = [a['achi_id'] for a in list(achis)]
    db.executable.close()

    ACh = [a for a in lc3_achivements if a['id'] in achi and not a['hidden']]
    ach = [a for a in lc3_achivements if a['id'] not in achi and not a['hidden']]
    ACH = [a for a in lc3_achivements if a['id'] in achi and a['hidden']]
    l___ = len(lc3_achivements)
    lAC_ = len([a for a in lc3_achivements if a['id'] in achi])
    lACh = len(ACh)
    lach = len(ach)
    lACH = len(ACH)
    l__H = len([a for a in lc3_achivements if a['hidden']])

    # Render template
    render = render_template('frame.html', lang=lang, page='achivements.html',
                             login=login, user=user, active=active,
                             ACh=ACh, ach=ach, ACH=ACH,
                             lACh=lACh, lach=lach, lACH=lACH, l__H=l__H,
                             width='%.2f'%(100*lAC_/l___))
    return make_response(render)


@app.route('/about')
@login_required
def about():
    """Displays the about menu"""

    login, user = get_user()
    active = default_active.copy()
    active['about'] = 'active'

    # Render template
    render = render_template('frame.html', lang=lang, page='about.html',
                             login=login, user=user, active=active)
    return make_response(render)


@app.route('/logout')
@login_required
def logout():
    """Logs the current user out"""

    del session['user_id']
    return redirect('/')


@app.route('/')
def index():
    """Displays the main page"""

    login, user = get_user()

    # Render template
    render = render_template('frame.html', lang=lang,
                             page='main.html', login=login, user=user, active=default_active)
    return make_response(render)


# Load config
config = json.loads(open(configfile, 'rb').read())
app.secret_key = config['secret_key']

# Load language
lang = json.loads(open(langfile, 'rb').read())

default_active = {'about': '', 'tasks': '',
                  'scoreboard': '', 'achivements': ''}

if __name__ == '__main__':
    """Initializes the database and sets up the language"""

    # Start web server
    app.run(host=config['host'], port=config['port'],
            debug=config['debug'], threaded=True)
