from flask import render_template, request, render_template_string, flash, current_app, redirect
from multiprocessing import Process
import re
import urlparse
from ..app import db
from . import dankblog
from .models import Post

@dankblog.before_app_first_request
def init_flag():
    if (db.session.query(Post).count() != 0):
        return
    flag = "FCTF{1ns3cur3_0bj3c+_r3f3rnces_are_dank}"
    secret_posts = ['wow you got the flag: {0}'.format(flag),
                    'hello world',
                    'omg another dank blog',
                    '1337 haxor',
                    'lyk omg hwo many posts are there ',
                    'dis is awesome w0w',
                    'i love this blog',
                    'aaaaaaaayyyyyyyyy lets gooo',
                    'im running out of ideas for posts',
                    'how about monty python quotes',
                    'What... is the air-speed velocity of an unladen swallow?']
    for a in secret_posts:
        db.session.add(Post(content=a))
    db.session.commit()

@dankblog.route('/<xss_id>')
def xss_post_page(xss_id):
    xss = Post.query.filter_by(id=xss_id).scalar()
    if xss is None:
        return render_template_string("404")
    return render_template('xss_post.html', xss=xss)

@dankblog.route('/')
def xss_create_page():
    posts2 = Post.query.filter(Post.id != 1).all()
    return render_template('post_base.html', post_list = posts2)
