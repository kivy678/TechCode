# -*- coding:utf-8 -*-

import os

from flask import Flask, g
from flask.ext.login import LoginManager, current_user

from modules.database import session
from modules.web.user import FlaskUser

from modules.web.cache import setup as CacheSetup
from modules.web.jinja import setup as JinjaSetup

################################################################################

WEB_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask('UpdateSystem',
            static_folder = os.path.join(WEB_DIR, 'static'),
            template_folder = os.path.join(WEB_DIR, 'templates'))
app.config.from_object('modules.web.config')

################################################################################

loginManager = LoginManager()
loginManager.login_view = 'auth.login'
loginManager.init_app(app)

@loginManager.user_loader
def load_user(id):
    return FlaskUser(id)

################################################################################

@app.teardown_request
def shutdown_session(exception=None):
    session.remove()

@app.before_request
def before_request():
    g.user = current_user

################################################################################

CacheSetup(app)
JinjaSetup(app)

################################################################################

from modules.web.views.base import setup as BaseSetup
from modules.web.views.auth import setup as AuthSetup
from modules.web.views.product import setup as ProductSetup
from modules.web.views.pattern import setup as PatternSetup
from modules.web.views.statistics import setup as StatsSetup
from modules.web.views.admin import setup as AdminSetup

BaseSetup(app)
AuthSetup(app)
ProductSetup(app)
PatternSetup(app)
StatsSetup(app)
AdminSetup(app)

################################################################################
