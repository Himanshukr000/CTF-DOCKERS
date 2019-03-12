# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms.fields import IntegerField, SubmitField, HiddenField
from wtforms import validators

class swap_form(Form):
    quantity = IntegerField("quantity", [
        validators.Regexp("^\d+$")])
    poke = SubmitField("Real to Moké".decode('utf-8'))
    real = SubmitField("Moké to Real".decode('utf-8'))

class shop_obj_form(Form):
    quantity = IntegerField("quantity", [
        validators.Regexp("^\d+$")])
    item_id = HiddenField("item_id", [
        validators.Regexp("^\d+$")])
    submit = SubmitField("Buy")
