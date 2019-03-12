# -*- coding: utf-8 -*-
from flask import render_template, request, flash, g, render_template_string
from flask_user import SQLAlchemyAdapter, UserManager, current_user, login_required
from multiprocessing import Process
from ..app import db
from ..app import app
from . import race
from . import forms
from . import flag
from models import User, Product
import time
import json

db_adapter = SQLAlchemyAdapter(db, User)        # Register the User model
user_manager = UserManager(db_adapter, app,
                           password_validator=lambda x,y: None)

@race.before_request
def set_flag():
    g.user = User.query.filter_by(id = current_user.get_id()).scalar()
    if not g.user:
        return
    g.user.flagstring = flag.flag
    pokeballs = json.loads(g.user.pokeballs)
    split_len = len(flag.flag)/(db.session.query(Product).count() - 1)
    print pokeballs, split_len
    for k,v in pokeballs.iteritems():
        i = Product.query.filter_by(name = k).scalar().id - 1
        if not (v > 0):
            portion=flag.flag[(split_len * i):(split_len * (i + 1))]
            g.user.flagstring = g.user.flagstring.replace(portion, '~' * split_len)
    db.session.commit()

@race.route('/')
def race_home_page():
    return render_template_string("""
        {% extends "base.html" %}
        {% block content %}
            <h2>Grand re-opening of the MokéStore</h2>
            <p>Welcome to the MokéStore 2. You can actually buy things now and there isn\'t a stupid broken bot to make you cry</p>
        {% endblock %}
        """.decode('utf-8'), user=g.user)

@race.route('/shop', methods=['GET', 'POST'])
@login_required
def race_shop_page():
    product_list = Product.query.all()
    success = False
    message = ''
    if request.method == 'POST':
        quantity = int(request.form['quantity']) if request.form['quantity'] else ''
        item_id = int(request.form['item_id']) if request.form['item_id'] else ''
        if (item_id == ''):
            flash("no product selected. stop tampering with that, you dont need to")
            return render_template('shop.html', message=message, form=forms.shop_obj_form(), user=g.user, success=success)

        product = Product.query.filter_by(id = item_id).scalar()
        if (product == None):
            flash("invalid product. stop tampering with that. you dont need to")
            return render_template('shop.html', message=message, form=forms.shop_obj_form(), user=g.user, success=success)

        g.user = User.query.filter_by(id = current_user.get_id()).scalar()
        if (product.currency == 'poke'):
            if (g.user.pokedollars < product.price * quantity):
                flash("Not enough pokedollars to complete purchase")
            else:
                g.user.pokedollars -= product.price * quantity
                #save user pokeballs here.
                pokeballs = json.loads(g.user.pokeballs)
                pokeballs[product.name] += quantity
                g.user.pokeballs = json.dumps(pokeballs)
                db.session.commit()
                set_flag()
                flash("Purchased {} {}".decode('utf-8').format(quantity, product.name))
        elif (product.currency == 'real'):
            if (g.user.realdollars < product.price * quantity):
                flash("Not enough realdollars to complete purchase")
            else:
                g.user.realdollars -= product.price * quantity
                #save g.user realballs here.
                db.session.commit()
                set_flag()
                flash("Purchased {} {}".decode('utf-8').format(quantity, product.name))

    return render_template('shop2.html', message=message, form=forms.shop_obj_form(), user=g.user, success=success, products_list = product_list)


@race.route('/swap', methods=['GET', 'POST'])
@login_required
def race_swap_page():
    cur_poke = db.session.query(User.pokedollars).filter_by(id = current_user.get_id()).scalar()
    #time.sleep(2)
    cur_real = db.session.query(User.realdollars).filter_by(id = current_user.get_id()).scalar()
    success = False

    message = 'Exchange your MokéDollars for `real` money here!'.decode('utf-8')
    if request.method == 'POST':
        quantity = int(request.form['quantity']) if request.form['quantity'] else ''
        if ('poke' in request.form):
            # real -> poke conversion -> 1 real = 10 poke
            if (cur_real >= quantity):
                g.user.pokedollars += quantity * 10
                db.session.commit()

                # we intentionally want to get new values to mess with
                g.user = User.query.filter_by(id = current_user.get_id()).scalar()
                cur_real -= quantity
                g.user.realdollars = cur_real
                db.session.commit()
            else:
                flash("insufficient real dollars")
        elif ('real' in request.form):
            # poke -> real conversion -> 10 poke = 1 real

            if (quantity % 10 != 0):
                flash("can only convert multiples of 10")
                g.user = User.query.filter_by(id = current_user.get_id()).scalar() # very database heavy
                return render_template('swap.html', message=message, form=forms.swap_form(), user=g.user, success=success)

            if (cur_poke >= quantity):
                g.user.realdollars += quantity / 10
                db.session.commit()

                # we intentionally want to get new values to mess with
                g.user = User.query.filter_by(id = current_user.get_id()).scalar()
                cur_poke -= quantity
                g.user.pokedollars = cur_poke
                db.session.commit()
            else:
                flash("insufficient poke dollars")


    g.user = User.query.filter_by(id = current_user.get_id()).scalar() # very database heavy
    return render_template('swap.html', message=message, form=forms.swap_form(), user=g.user, success=success)
