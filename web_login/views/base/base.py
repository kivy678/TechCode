# -*- coding:utf-8 -*-

from flask import render_template, redirect
from flask.views import MethodView

from views.base import view


class AuthLogin(MethodView):

    def get(self):
        return render_template('base.jinja')

    def post(self):
        return redirect('/')


authLogin = AuthLogin.as_view('/')
view.add_url_rule('/', view_func=authLogin)
