# -*- coding:utf-8 -*-

from flask import Blueprint, render_template

view = Blueprint('product', 'product')

def setup(app):
    app.register_blueprint(view, url_prefix='/product/')

import index
import manifest
import attrs
