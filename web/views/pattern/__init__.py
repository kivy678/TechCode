# -*- coding:utf-8 -*-

from flask import Blueprint, render_template

view = Blueprint('pattern', 'pattern')

def setup(app):
    app.register_blueprint(view, url_prefix='/pattern/')

import index
import report
import pattern
