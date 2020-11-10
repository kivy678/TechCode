# -*- coding:utf-8 -*-

from flask import Blueprint

view = Blueprint('/', '/')

def setup(app):
    app.register_blueprint(view, url_prefix='/')

import views.base.base
