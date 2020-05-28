# -*- coding:utf-8 -*-

from flask import Blueprint

view = Blueprint('test', __name__)

def setup(app):
    app.register_blueprint(view, url_prefix='/test/')


import blueprint.CsvViwer
