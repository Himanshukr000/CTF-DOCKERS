from flask import render_template, request, flash
from ..app import db
from . import sql
from . import forms
from .models import User
import re
import sqlite3

flag1 = 'FCTF{we_kn0w_n0_k1ng_but_th3_K1nG_1n_Th3_N0rTH_K1NG_1N_Th3_N0rth!_omg_manderlys}'
flag2 = 'FCTF{duh_admin_password_is_like_the_best_cr3d3ntials}'

@sql.before_app_first_request
def init_flag():
    if (db.session.query(User).count() == 2):
        return
    jonsnow = User(username = 'jonsnow', password=flag1)
    admin = User(username = 'admin', password='password')
    db.session.add(jonsnow)
    db.session.add(admin)
    db.session.commit()

@sql.route('/', methods=['GET', 'POST'])
def sql_home():
    form = forms.login_form()
    if request.method == 'POST':
        username = request.form['username'] if request.form['username'] else ''
        password = request.form['password'] if request.form['password'] else ''
        if username == '':
            flash("Please enter a username")
            return render_template('login.html', form=form)
        if password == '':
            flash("Please enter a password")
            return render_template('login.html', form=form)

        con = sqlite3.connect('app/basic_app.sqlite')
        cur = con.cursor()
        try:
            query = """ SELECT User.username as sql_username, User.password as sql_password
                            FROM User
                            WHERE username = '%s' and password = '%s'""" % (sql_filter(username), sql_filter(password))
            cur.execute(query)
        except sqlite3.Error as e:
            error_msg = xss_filter("error: {0}.".format(e.args[0]))
            query = xss_filter("query: {0}.".format(query))
            print '[+] sql error: ', e
            flash( "{0}<br>{1}".format(error_msg, query))

        result = cur.fetchone()
        if result != None:
            sql_username = result[0]
            sql_password = result[1]

        if result == None:
            flash("No Username & Password combination found")
        elif sql_username != username:
            flash("Incorrect username")
        elif sql_username == username and sql_password != password:
            flash("Incorrect password")
        elif sql_username == 'admin' and sql_password == 'password':
            flash("I think the other user you\'re looking for is \'jonsnow\'. Here\'s your flag: {0}".format(flag2))
        elif sql_username == username and sql_password == password:
            flash("Should've checked the password. Good work. You're done. Go home")

    return render_template('login.html', form=form)

def xss_filter(payload):
    payload = payload.replace('<', '&lt;').replace('>', '&gt;')
    return payload

sql_blacklist = ['UPDATE', 'INSERT', 'UNION', 'DELETE', 'SELECT']

def sql_filter(payload):
    for badword in sql_blacklist:
        regex = re.compile(re.escape(badword), re.I)
        payload = regex.sub('woof', payload)
    return payload
