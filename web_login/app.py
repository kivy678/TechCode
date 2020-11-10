# -*- coding:utf-8 -*-

import os

from flask import Flask, g
from flask_login import LoginManager, current_user

from user import FlaskUser

################################################################################

WEB_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask('TEST WEBPAGE',
            static_folder = os.path.join(WEB_DIR, 'static'),
            template_folder = os.path.join(WEB_DIR, 'templates'))

app.config.from_object('config')

################################################################################

loginManager = LoginManager()
loginManager.login_view = 'auth.login'
loginManager.init_app(app)

@loginManager.user_loader
def load_user(user_id):
    return FlaskUser(user_id)

################################################################################

@app.before_request
def before_request():
    g.user = current_user

################################################################################

from views.base import setup as BaseSetup
from views.auth import setup as AuthSetup

BaseSetup(app)
AuthSetup(app)

################################################################################

if __name__ == '__main__':
    # Flask running
    app.run(host="0.0.0.0", port=8888, debug=True)
    print("Main done...")
