# -*- coding:utf-8 -*-

import hashlib

from flask import render_template, request, url_for, redirect
from flask.views import MethodView
from flask_login import login_user

from user import FlaskUser

from views.auth import view
from database.user import Users

class AuthLogin(MethodView):

    def get(self):
        return render_template('auth/login.jinja')

    def post(self):
        name = request.form.get('user_id', None)
        passwd = request.form.get('user_password', '')

        for user in Users:
            if user.name == name:
                login_user(FlaskUser(user))
                return redirect('/')

        return "로그인 실패"


authLogin = AuthLogin.as_view('login')
view.add_url_rule('login', view_func=authLogin)
