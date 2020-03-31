# -*- coding:utf-8 -*-

from flask import render_template
from flask.views import MethodView

from modules.web.views.product import view

from modules.database.models import Product, Manifest

class ProductAttr(MethodView):
    def get(self, id):
        productObj = Product.query.get(id)

        return render_template('product/attribute.jinja', entries=productObj.r_attribute)

class ManifestAttr(MethodView):
    def get(self, id):
        manifestObj = Manifest.query.get(id)

        return render_template('product/attribute.jinja', entries=manifestObj.r_attribute)

productAttr  = ProductAttr.as_view('attr.product')
manifestAttr = ManifestAttr.as_view('attr.manifest')

view.add_url_rule('attribute/product/<int:id>', view_func=productAttr)
view.add_url_rule('attribute/manifest/<int:id>', view_func=manifestAttr)
