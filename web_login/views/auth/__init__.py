# -*- coding:utf-8 -*-

from flask import Blueprint

view = Blueprint('auth', 'auth')

def setup(app):
    app.register_blueprint(view, url_prefix='/auth/')

import views.auth.login
import views.auth.logout
