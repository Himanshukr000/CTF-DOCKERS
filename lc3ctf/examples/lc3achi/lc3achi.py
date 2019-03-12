#!/usr/bin/env python3

"""lc3_achi.py -- achivements module"""

import time
import dataset
from flask import session

lc3_achivements = [{'id': 0, 'hidden': False, 'title': 'Sleepless', 'desc': 'Submit a correct flag at night'},
                   {'id': 3, 'hidden': False, 'title': 'CTF Initiate', 'desc': 'Solve one problem'}
                  ]

def check_and_set(dbfile, id):
    db = dataset.connect('sqlite:///ctf.db')
    achis = db.query('''select a.achi_id from achivements a
                where a.user_id = :user_id''', user_id=session['user_id'])
    achi = [a['achi_id'] for a in list(achis)]
    if id in achi:
        db.executable.close()
        return False
    else:
        new_achi = dict(achi_id=id, user_id=session['user_id'])
        db['achivements'].insert(new_achi)
        db.executable.close()
        return True

def chkachi(dbfile, action, **kw):
    new_achi = False
    return new_achi