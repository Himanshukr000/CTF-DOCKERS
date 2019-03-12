from flask import render_template, request, render_template_string, flash, current_app, redirect
from multiprocessing import Process
import re
import urlparse
from ..app import db
from . import base_xss
from . import forms
from . import phantom
from .models import Xss

@base_xss.route('/10f3d0e863695295fcd7c2902713a0a0')
def xss_set_flag_cookie():
    redirect_to_index = redirect('/')
    response = current_app.make_response(redirect_to_index)
    response.set_cookie('totally_not_the_flag',value='FCTF{D0NT_You_L0V3_UN10n_SqL_InJ3cT10n}')
    return response

@base_xss.route('/<xss_id>')
def xss_post_page(xss_id):

    if 'hyaku_percent_not_the_flag' not in request.cookies:
        return render_template_string('')
    if xss_id == '404':
        return render_template_string('')

    print '[+] XSS Payload Request: ID: ', xss_id,
    xss = Xss.query.filter_by(id=xss_id).scalar()
    if xss is None:
        return render_template_string("404")
    print xss.content, '|', xss.id
    return render_template('xss_post.html', xss=xss)

@base_xss.route('/', methods=['GET', 'POST'])
@base_xss.route('/create', methods=['GET', 'POST'])
def xss_create_page():
    message = ''
    if request.method == 'GET':
        form = forms.base_xss_form()
        return render_template('xss_create.html', message=message, form=form)
    elif request.method == 'POST':
        content = request.form['content'] if request.form['content'] else ''

        try:
            hostname = urlparse.urlparse(request.url_root).netloc
        except:
            flash('Please submit a url for this site')
            form = forms.base_xss_form()
            return render_template('xss_create.html', message=message, form=form)

        if not re.match(r'http://{0}/.*'.format(hostname), content):
            flash('Please submit a url for this site')
            form = forms.base_xss_form()
            return render_template('xss_create.html', message=message, form=form)
        new_xss = Xss(content=content)
        db.session.add(new_xss)
        db.session.commit()

        if "PhantomJS" not in request.headers['User-Agent']:
            print request.url, 'just before process spooky'
            p = Process(target=phantom.xss_get, args=(content,))
            p.start()
        return render_template('xss_success.html', content=content)

def xss_filter(payload):
    payload = payload.replace("script", "XSS ATTEMPT DETECTED")
    return payload
