from flask import Flask
from flask import render_template,  session,  redirect,  flash, request
from flask_wtf import Form
from wtforms import TextField, SubmitField

from PIL import Image, ImageFont, ImageDraw, ImageFilter
from cStringIO import StringIO
import base64
import time
import random

class ConfigClass(object):
    SECRET_KEY = 'ifq2li3jtq2o8efo9dshg9q38oiq23toiqtuh3tlqn'

app = Flask(__name__)
app.config.from_object(__name__+'.ConfigClass')

WINNER = 200
flag = 'FCTF{b8e1a726842ce9ad327433be05cb42f8}'

class captcha_form(Form):
    secret = TextField("secret")
    submit = SubmitField("verify")

def valid_session():
    cur_time = float(time.time())
    if ('time' not in session) or (cur_time - session['time'] > 10):
        session['time'] = time.time()
        return False
    if ('count' not in session):
        session['count'] = 0
        return False
    return True

def reset_session():
    flash("Your session is invalid. Start again")
    session['count'] = 0
    redirect('/')

@app.route('/',  methods=['GET',  'POST'])
def home():
    if (not valid_session()):
        reset_session()

    if (request.method == 'POST'):
        if (session['count'] >= WINNER):
            flash("congratulations {}".format(flag))
            redirect('/')

        secret = request.form['secret'] if request.form['secret'] else ''

        if (secret != session['secret']):
            reset_session()

        session['count'] += 1

    x, y = generateCaptcha()
    b64image = base64.b64encode(y)

    session['secret'] = x
    session['time'] = time.time()
    return render_template('index.html', image=b64image, form = captcha_form(), count = session['count'], oopsie = x)

"""
    This code is taken from and is copyright to:
    http://code.activestate.com/recipes/440588/
"""
FONT_FILE = './comicsans.ttf'
def gen_captcha(text,  fnt,  fnt_sz,  f,  fmt='PNG'):
    """Generate a captcha image"""

    # randomly select the foreground color
    fgcolor = random.randint(0, 0xffff00)

    # make the background color the opposite of fgcolor
    bgcolor = fgcolor ^ 0xffffff

    # create a font object 
    font = ImageFont.truetype(fnt, fnt_sz)

    # determine dimensions of the text
    dim = font.getsize(text)

    # create a new image slightly larger that the text
    im = Image.new('RGB',  (dim[0]+5, dim[1]+5),  bgcolor)
    d = ImageDraw.Draw(im)
    x,  y = im.size
    r = random.randint

    # draw 100 random colored boxes on the background
    #for num in range(100):
    #    d.rectangle((r(0, x), r(0, y), r(0, x), r(0, y)), fill=r(0, 0xffffff))

    # add the text to the image
    d.text((3, 3),  text,  font=font,  fill=fgcolor)
    im = im.filter(ImageFilter.EDGE_ENHANCE_MORE)

    # save the image to a file
    im.save(f,  format=fmt)

def gen_random_word(wordLen=6):
    """Generate a random word of length wordLen. Some characters have been removed
    to avoid ambiguity such as i, l, o, I, L, 0,  and 1"""
    allowedChars = "abcdefghjkmnpqrstuvwzyzABCDEFGHJKMNPQRSTUVWZYZ23456789"
    word = ""

    for i in range(0,  wordLen):
        word = word + allowedChars[random.randint(0, 0xffffff) % len(allowedChars)]

    return word

def generateCaptcha():
    """Generate a captcha image in memory using a randomly generated word and a font
    file on the system. Returns the word and the image"""

    word = gen_random_word()
    buf = StringIO()
    gen_captcha(word.strip(),  FONT_FILE,  50,  buf)
    s = buf.getvalue()
    buf.close()
    return word,  s
