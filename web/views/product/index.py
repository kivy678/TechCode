# -*- coding:utf-8 -*-

from flask import render_template
from flask.views import MethodView

from modules.web.views.product import view

from modules.database.models import Product

class ProductIndex(MethodView):
    def get(self):
        return render_template('product/index.jinja', entries = Product.query.order_by(Product.priority).all())

productIndex = ProductIndex.as_view('index')
view.add_url_rule('', view_func=productIndex)
