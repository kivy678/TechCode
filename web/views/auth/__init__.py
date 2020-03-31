# -*- coding:utf-8 -*-

from flask import Blueprint, render_template

view = Blueprint('auth', 'auth')

def setup(app):
    app.register_blueprint(view, url_prefix='/auth/')

import login
import logout
