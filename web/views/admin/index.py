# -*- coding:utf-8 -*-

from flask import render_template
from flask.views import MethodView

from modules.web.views.admin import view

class AdminIndex(MethodView):

    def get(self):
        return render_template('admin/index.jinja')

adminIndex = AdminIndex.as_view('index')
view.add_url_rule('', view_func=adminIndex)
