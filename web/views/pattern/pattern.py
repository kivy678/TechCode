# -*- coding:utf-8 -*-

from flask       import render_template, request, url_for
from flask.views import MethodView

from modules.web.views.pattern import view
from modules.web.cache         import queryCache
from modules.web.utils.view    import pagination

from modules.database import session
from modules.database.models import Product, ProductVersion, ReportType, ReportString, Report, Pattern, File

from sqlalchemy import func

ROWS = 25

class PatternVersionProduct(MethodView):
    def get(self):
        return render_template('pattern/pattern/1.jinja',
                               entries = Product.query.order_by(Product.name).all())

class PatternVersionPatterns(MethodView):
    def get(self, product, page=0):
        cacheKey = 'pattern.version.patterns.total.{}'.format(product)
        total = queryCache(cacheKey,
                           lambda: session.query(func.count(ProductVersion.product))\
                           .filter(ProductVersion.product == product)\
                           .scalar())
        pageData = pagination(page,
                              ROWS,
                              total,
                              lambda x: url_for('pattern.version.patterns', product=product, page=x))
        
        return render_template('pattern/pattern/2.jinja',
                               pageData = pageData,
                               entries = ProductVersion.query\
                               .filter(ProductVersion.product == product)\
                               .order_by(ProductVersion.pattern.desc())\
                               .offset(page * ROWS)\
                               .limit(ROWS)\
                               .all())

class PatternVersionView(MethodView):
    def get(self, product, pattern):
        return render_template('pattern/pattern/3.jinja',
                               entries = Pattern.query\
                               .join(File)\
                               .join(Report)\
                               .join(ReportType)\
                               .join(ReportString)\
                               .filter(Pattern.product == product)\
                               .filter(Pattern.pattern == pattern)\
                               .order_by(Pattern.cmd)\
                               .order_by(ReportType.val)\
                               .order_by(ReportString.val)\
                               .all())
                               
patternVersionProduct  = PatternVersionProduct.as_view('version.product')
patternVersionPatterns = PatternVersionPatterns.as_view('version.patterns')
patternVersionView     = PatternVersionView.as_view('version.view')

view.add_url_rule('version/1', view_func=patternVersionProduct)
view.add_url_rule('version/2/<int:product>/<int:page>', view_func=patternVersionPatterns)
view.add_url_rule('version/3/<int:product>/<int:pattern>', view_func=patternVersionView)

################################################################################
