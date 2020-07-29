# -*- coding:utf-8 -*-

from flask.views import MethodView
from flask import render_template, request

from flask import current_app as app


class FruitViwer(MethodView):
    template_name = None

    def __init__(self, template_name):
        self.template_name = template_name

    def get(self):
        fruit = request.args.get('fruit')
        text = request.args.get('text')

        print(fruit)
        return render_template(self.template_name,
                               fruit=fruit,
                               text=text)
