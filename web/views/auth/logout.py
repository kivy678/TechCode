# -*- coding:utf-8 -*-

import hashlib

from flask import render_template, request, url_for, redirect
from flask.views import MethodView
from flask.ext.login import current_user, login_required, login_user, logout_user

from modules.web.user import FlaskUser

from modules.web.views.auth import view
from modules.database.models import Users

class AuthLogout(MethodView):

    def get(self):
        logout_user()
        return redirect('/')


authLogout = AuthLogout.as_view('logout')
view.add_url_rule('logout', view_func=authLogout)
