# -*- coding:utf-8 -*-

from flask import redirect
from flask.ext.login import current_user
from functools import wraps

from modules.database.models import Users

class FlaskUser(object):
    user = None

    def __init__(self, id=None):
        if isinstance(id, Users):
            self.user = id
        elif isinstance(id, (int, long)):
            self.user = Users.query.get(id)
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
