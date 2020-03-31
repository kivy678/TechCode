# -*- coding:utf-8 -*-

from flask import render_template
from flask.views import MethodView

from modules.web.views.product import view

from modules.database.models import Manifest

class ProductManifest(MethodView):
    def get(self, id):
        entries = Manifest.query.filter(Manifest.product == id).order_by(Manifest.id).all()

        return render_template('product/manifest.jinja', entries = entries)

productManifest = ProductManifest.as_view('manifest')
view.add_url_rule('manifest/<int:id>', view_func=productManifest)
        
