# -*- coding:utf-8 -*-

import hashlib

from flask import render_template, request, url_for, redirect
from flask.views import MethodView
from flask.ext.login import current_user, login_required, login_user, logout_user

from modules.web.user import FlaskUser

from modules.web.views.auth import view
from modules.database.models import Users

class AuthLogin(MethodView):

    def get(self):
        return render_template('auth/login.jinja')

    def post(self):
        print request.form.get('user_id', None)
        print request.form.get('user_password', '')

        md5 = hashlib.md5()
        md5.update(request.form.get('user_password', ''))

        uid = request.form.get('user_id', None)
        upw = md5.digest()

        userObj = Users.query\
                       .filter(Users.userid == uid)\
                       .filter(Users.userpass == upw)\
                       .first()

        if userObj is None:
            return redirect(url_for('base.error',
                                    head='로그인 오류',
                                    message='로그인에 실패하였습니다.',
                                    next=url_for('auth.login')))

        login_user(FlaskUser(userObj))

        return redirect('/')


authLogin = AuthLogin.as_view('login')
view.add_url_rule('login', view_func=authLogin)
