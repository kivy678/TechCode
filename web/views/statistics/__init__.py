# -*- coding:utf-8 -*-

from flask import Blueprint, render_template

view = Blueprint('stats', 'stats')

def setup(app):
    app.register_blueprint(view, url_prefix='/stats/')

import statView
