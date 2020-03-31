# -*- coding:utf-8 -*-

try:
    import simplejson as json
except:
    import json

from flask       import render_template, request, url_for
from flask.views import MethodView

from modules.web.views.statistics import view
from modules.web.cache            import queryCache
from modules.web.utils.view       import pagination

from modules.database import session
from modules.database.models import Product

from sqlalchemy import func

class StatsIndexView(MethodView):
    def get(self):
        return render_template('stats/index.jinja',
                               entries=Product.query.order_by(Product.name).all())

class StatsGraphView(MethodView):
    def get(self, product, count=10):
        QUERY = """select
	v.date,
	rt.val,
	count(*)
from pattern 
join product as p on pattern.product = p.id 
join product_version as pv on pattern.product = pv.product and pattern.pattern = pv.pattern
join version as v on pv.version = v.id
join file as f on pattern.file = f.id
join report as rpt on f.report = rpt.id
join report_type as rt on rpt.rt = rt.id
where
	pattern.product = :product AND
	pattern.pattern IN (select pattern from product_version where product = :product order by pattern desc limit :count)
group by v.date, rt.val
order by v.date, rt.val"""

        rows = session.execute(QUERY, { 'product': product, 'count': count})
        categories = set()

        res = []
        for a,b,c in rows:
            res.append( (str(a),
                         b,
                         c ) )
        
        d = {}
        for dt, rt, rs in res:
            categories.add(rt)
            if False == d.has_key(dt):
                d[dt] = {}
            d[dt][rt] = rs

        r = []
        for k,v in d.items():
            x = { 'date': k, 'sum': 0 }
            for _k, _v in v.items():
                x[_k] = _v
                x['sum'] += _v
                
            r.append(x)

        return render_template('stats/graph.jinja', data=res, chartdata=json.dumps(r), categories=json.dumps(list(categories)))

statsIndexView = StatsIndexView.as_view('index')
statsGraphView = StatsGraphView.as_view('graph')

view.add_url_rule('/', view_func=statsIndexView)
view.add_url_rule('graph/<int:product>/<int:count>', view_func=statsGraphView)
