# -*- coding:utf-8 -*-

from flask import Blueprint, render_template

view = Blueprint('admin', 'admin')

def setup(app):
    app.register_blueprint(view, url_prefix='/admin/')

import index
import product
import manifest
import fileView
import updateView
