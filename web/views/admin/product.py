# -*- coding:utf-8 -*-

from flask import render_template, request, url_for, redirect
from flask.views import MethodView
from flask.ext.login import current_user, login_required, login_user, logout_user

from modules.web.views.admin import view
from modules.web.user import admin_required

from modules.database import session
from modules.database.models import *

class ProductIndex(MethodView):

    @admin_required
    def get(self):
        return render_template('admin/product/index.jinja')

class ProductList(MethodView):

    @admin_required
    def get(self):
        return render_template('admin/product/list.jinja',
                               entries = Product.query.order_by(Product.priority).all())

class ProductView(MethodView):

    @admin_required
    def get(self, id):
        return render_template('admin/product/view.jinja', product = Product.query.get(id))

productIndex = ProductIndex.as_view('product.index')
productList  = ProductList.as_view('product.list')
productView  = ProductView.as_view('product.view')

view.add_url_rule('product/', view_func=productIndex)
view.add_url_rule('product/list', view_func=productList)
view.add_url_rule('product/view/<int:id>', view_func=productView)
