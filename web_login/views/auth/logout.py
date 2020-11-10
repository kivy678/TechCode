# -*- coding:utf-8 -*-

from flask import redirect
from flask.views import MethodView
from flask_login import logout_user

from views.auth import view

class AuthLogout(MethodView):

    def get(self):
        logout_user()
        return redirect('/')


authLogout = AuthLogout.as_view('logout')
view.add_url_rule('logout', view_func=authLogout)
