from flask import render_template, request, render_template_string, flash, redirect
from sqlalchemy import desc
from multiprocessing import Process
from ..app import db
from . import sql
from . import forms
from .models import Post
from .models import FLAG
import sqlite3
import binascii
import time
import os
import hashlib

illegal_chars = ['\'', '"', ';', '-']
def encode_post_id(post_id):
    return ''.join(hex(ord(a))[2:] for a in post_id)

def create_post(title, content, hidden = '', uid = ''):
    post_id = filter(lambda x: x not in illegal_chars, title)
    print '[+] NEW POST ID', encode_post_id(post_id)
    uid = binascii.hexlify(os.urandom(3)) if uid == '' else uid
    enc_post_id = encode_post_id(post_id) + '-' + uid
    md5checksum = hashlib.md5(enc_post_id).hexdigest()[0:6]

    new_post = Post(id=post_id, title=title, content=content, hash=enc_post_id + '-' + md5checksum, uid = uid, time = time.time(), hidden = hidden)
    return new_post

@sql.before_app_first_request
def init_flag():
    if (db.session.query(FLAG).count() == 1):
        return
    flag = "FCTF{D4mn_s0n_wh3rd_y0u_encryp+_Th4t}"
    winner = FLAG(flag = flag)
    db.session.add(winner)

    secret_posts = [('hello world', 'omg my first blog. i think i\'ll call it something original. like wobblog', '', '1010101'),
                    ('1337 haxor', 'dis blog just got rekt h4h4 ', 'hah this blogs security is no match for my awesome magic sql automator. what type of column name is \'flag\'??!?!?!??!?!!', '1010102')]
    for a in secret_posts:
        db.session.add(create_post(a[0], a[1], a[2], a[3]))
    db.session.commit()

@sql.route('/<post_id>')
def post_post_page(post_id):
    print '[+] post request id: ', post_id
    hash_id = ''
    post_split = post_id.split('-')
    print '[+] post_split:' ,post_split
    try:
        hash_id = binascii.unhexlify(post_split[0])
        print '[+] hash_id: ', hash_id
    except:
        flash("Unable to decode post id")
        return render_template('post.html')

    hash_key = "{0}-{1}".format(str(post_split[0]), str(post_split[1]))
    print '[+] hash_key:', hash_key
    if (hashlib.md5(hash_key).hexdigest()[0:6] != post_split[2]):
        flash("Md5 checksum incorrect. query has been tampered with")
        return render_template('post.html')

    con = sqlite3.connect('app/basic_app.sqlite')
    cur = con.cursor()
    try:
        query = """ SELECT post.title AS post_title, post.content AS post_content, post.hidden as post_hidden
                        FROM post
                        WHERE id = '%s'""" % hash_id
        cur.execute(query)
    except sqlite3.Error as e:
        print '[+] sql error: ', e
        return render_template_string("""
            {% extends "base.html" %}
            {% block content %}
            <p>error: {{ error }}</p>
            <p>query: {{ query }}</p>
            {% endblock %}
                                      """, error = e.args[0],
                                           query = query)
    temp_post = cur.fetchall()
    print temp_post
    post_list = []
    for tp in temp_post:
        post = Post()
        post.title = tp[0] if tp[0] else ''
        post.content = tp[1] if tp[1] else ''
        post.hidden = tp[2] if tp[2] else ''
        post_list.append(post)
    print post_list

# insert the formatting into a Post class here and pass it onwards.
    if len(post_list) == 0:
        return render_template_string("404")
    return render_template('post.html', post_list=post_list)

@sql.route('/')
def post_home():
    posts = Post.query.order_by(desc(Post.time)).limit(10).all()
    posts2 = Post.query.filter((Post.uid == '1010101') | (Post.uid == '1010102')).all()
    for p in posts2:
        if p not in posts:
            posts.append(p)
    return render_template('post_base.html', post_list = posts)

@sql.route('/create', methods=['GET', 'POST'])
def post_create_page():
    if request.method == 'GET':
        message = 'hello'
        form = forms.post_form()
        return render_template('create.html', message=message, form=form)
    elif request.method == 'POST':
        title = request.form['title'] if request.form['title'] else ''
        title = title.replace('<','&lt;').replace('>','&gt;')
        content = request.form['content'] if request.form['content'] else ''
        content = content.replace('<','&lt;').replace('>','&gt;')
        hidden = request.form['hidden'] if request.form['hidden'] else ''
        hidden = hidden.replace('<','&lt;').replace('>','&gt;')
        db.session.add(create_post(title, content, hidden))
        db.session.commit()
        flash("This is going straight to the front page!")
        return redirect('/')

