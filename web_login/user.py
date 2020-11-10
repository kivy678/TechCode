# -*- coding:utf-8 -*-

from flask import redirect
from flask_login import current_user
from functools import wraps

from database.user import User, Users

class FlaskUser(object):
    user = None

    def __init__(self, user_id=None):
        if isinstance(user_id, User):
            self.user = user_id
        elif isinstance(user_id, (int)):
            for user in Users:
                if user.id == user_id:
                    self.user = user
                    break
        else:
            self.user = None

    @property
    def is_authenticated(self):
        return not (self.user is None)

    @property
    def is_active(self):
        return not (self.user is None)

    @property
    def is_anonymous(self):
        return not (self.user is None)

    @property
    def is_admin(self):
        if False == self.is_authenticated:
            return False
        if 0 == self.user.admin:
            return False
        return True

    def get_id(self):
        if self.user is None:
            return None

        return self.user.id

    def __repr__(self):
        return '<FlaskUser (%r, %r)>' % (self.get_id(), self.user)


def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        try:
            if False == current_user.is_admin:
                return redirect('/')
        except:
            return redirect('/')

        return func(*args, **kwargs)
    return decorated_view
