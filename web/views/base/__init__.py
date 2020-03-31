# -*- coding:utf-8 -*-

from flask import Blueprint, render_template

view = Blueprint('base', 'base')

def setup(app):
    app.register_blueprint(view, url_prefix='/')

import index
import errorView
