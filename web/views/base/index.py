# -*- coding:utf-8 -*-

from flask import render_template
from flask.views import MethodView

from modules.web.views.base import view

class BaseIndex(MethodView):

    def get(self):
        return render_template('base/index.jinja')

baseIndex = BaseIndex.as_view('index')
view.add_url_rule('', view_func=baseIndex)
