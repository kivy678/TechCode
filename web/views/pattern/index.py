# -*- coding:utf-8 -*-

from flask import render_template
from flask.views import MethodView

from modules.web.views.pattern import view

from modules.database.models import Product

class PatternIndex(MethodView):
    def get(self):
        return render_template('pattern/index.jinja', entries = Product.query.order_by(Product.priority).all())

patternIndex = PatternIndex.as_view('index')
view.add_url_rule('', view_func=patternIndex)
