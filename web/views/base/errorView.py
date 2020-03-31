# -*- coding:utf-8 -*-

from flask import render_template
from flask.views import MethodView

from modules.web.views.base import view

class BaseError(MethodView):

    def get(self):
        return render_template('base/error.jinja')

baseError = BaseError.as_view('error')
view.add_url_rule('error', view_func=baseError)
