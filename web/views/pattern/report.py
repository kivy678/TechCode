# -*- coding:utf-8 -*-

from flask       import render_template, request, url_for
from flask.views import MethodView

from modules.web.views.pattern import view
from modules.web.cache         import queryCache
from modules.web.utils.view    import pagination

from modules.database import session
from modules.database.models import Product, ReportType, ReportString, Report, Pattern, File

from sqlalchemy import func

ROWS = 25

class PatternReportProduct(MethodView):
    def get(self):
        return render_template('pattern/report/1.jinja',
                               entries = Product.query.order_by(Product.name).all())

class PatternReportTypes(MethodView):
    def get(self, product):
        return render_template('pattern/report/2.jinja',
                               product=product,
                               entries = ReportType.query.order_by(ReportType.val).all())

class PatternReportList(MethodView):
    def get(self, product, rt, page=0):

        cacheKey = 'pattern.report.3.{}.total'.format(rt)
        total = queryCache(cacheKey,
                           lambda: session.query(func.count(Report.id))\
                           .filter(Report.rt == rt)\
                           .scalar())
        pageData = pagination(page, ROWS, total, lambda x: url_for('pattern.report.list', product=product, rt=rt, page=x))
        return render_template('pattern/report/3.jinja',
                               pageData = pageData,
                               product=product,
                               entries = Report.query\
                               .join(ReportString)\
                               .filter(Report.rt == rt)\
                               .order_by(ReportString.val)\
                               .offset(page * ROWS)\
                               .limit(ROWS)\
                               .all())

class PatternReportView(MethodView):
    def get(self, product, id, page=0):
        cacheKey = 'pattern.report.4.{}.{}.total'.format(product, id)
        total = queryCache(cacheKey,
                           lambda: session.query(func.count(Pattern.file))\
                           .join(File)\
                           .filter(Pattern.product == product)\
                           .filter(File.report == id)\
                           .scalar())
        pageData = pagination(page, ROWS, total, lambda x: url_for('pattern.report.view', product=product, id=id, page=x))
        
        return render_template('pattern/report/4.jinja',
                               pageData = pageData,
                               entries = Pattern.query\
                               .join(File)\
                               .filter(Pattern.product == product)\
                               .filter(File.report == id)\
                               .order_by(Pattern.extend)\
                               .offset(ROWS * page)\
                               .limit(ROWS)\
                               .all())
                               

patternReportProduct = PatternReportProduct.as_view('report.product')
patternReportTypes   = PatternReportTypes.as_view('report.types')
patternReportList    = PatternReportList.as_view('report.list')
patternReportView    = PatternReportView.as_view('report.view')

view.add_url_rule('report/1', view_func=patternReportProduct)
view.add_url_rule('report/2/<int:product>', view_func=patternReportTypes)
view.add_url_rule('report/3/<int:product>/<int:rt>/<int:page>', view_func=patternReportList)
view.add_url_rule('report/4/<int:product>/<int:id>/<int:page>', view_func=patternReportView)
