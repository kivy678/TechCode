# -*- coding:utf-8 -*-

import os
import csv

from flask.views import MethodView
from flask import render_template, request

from settings import TMP_DIR

from blueprint import view


class CsvViwer(MethodView):
    template_name = None

    def __init__(self, template_name):
        self.template_name = template_name

    def get(self):
        csv_path = os.path.join(TMP_DIR, 'test.csv')
        with open(csv_path, 'r') as fr:
            cr = csv.reader(fr, delimiter=',', quotechar="'",
                            quoting=csv.QUOTE_ALL)

            return render_template(self.template_name, enter=cr)


csv_view = CsvViwer.as_view('csv', template_name='test/csv.jinja')
view.add_url_rule('csv', view_func=csv_view, methods=['GET'])
