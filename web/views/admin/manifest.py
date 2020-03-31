# -*- coding:utf-8 -*-

from flask import render_template, request, url_for, redirect
from flask.views import MethodView
from flask.ext.login import current_user, login_required, login_user, logout_user

from modules.web.views.admin import view
from modules.web.user import admin_required

from modules.database import session
from modules.database.models import *

class ManifestView(MethodView):

    @admin_required
    def get(self, id):
        return render_template('admin/manifest/view.jinja', manifest=Manifest.query.get(id))

manifestView = ManifestView.as_view('manifest.view')
view.add_url_rule('manifest/view/<int:id>', view_func=manifestView)
