# -*- coding:utf-8 -*-

from flask import render_template, request, url_for, redirect
from flask.views import MethodView
from flask.ext.login import current_user, login_required, login_user, logout_user

from modules.web.views.admin import view
from modules.web.user import admin_required

from modules.web.cache import queryCache
from modules.web.utils.view import pagination

from modules.database import session
from modules.database.models import *

from sqlalchemy import func

FILE_LIST_ROWS = 25

class FileIndex(MethodView):
    @admin_required
    def get(self):
        return render_template('admin/file/index.jinja')

class FileList(MethodView):
    @admin_required
    def get(self):
        page = int(request.args.get('page', '0'))

        total = queryCache('admin.file.list.total',
                           lambda: session.query(func.count(File.id)).scalar())

        pageData = pagination(page,
                              FILE_LIST_ROWS,
                              total,
                              lambda x: url_for('admin.file.list', page=x))

        return render_template('admin/file/list.jinja',
                               total = total,
                               pageData = pageData,
                               entries = File.query\
                               .order_by(File.status)\
                               .order_by(File.priority.desc())\
                               .offset(page * FILE_LIST_ROWS)\
                               .limit(FILE_LIST_ROWS)\
                               .all())
    
class FileSearch(MethodView):
    
    @admin_required
    def get(self, mode='index', step=0):
        f = 'fetch_{}_{}'.format(mode, step)
        if False == hasattr(self, f):
            return redirect(url_for('base.error',
                                    head='오류',
                                    message='해당 페이지를 찾을 수 없습니다.',
                                    next=url_for('admin.file.search')))

        try:
            return getattr(self, f)()
        except:
            return redirect(url_for('base.error',
                                    head='오류',
                                    message='해당 페이지 처리에 오류가 존재합니다.',
                                    next=url_for('admin.file.search')))

    def fetch_index_0(self, *args, **kwargs):
        return render_template('admin/file/search.jinja')

    def fetch_report_0(self):
        return render_template('admin/file/search_report.0.jinja', entries = Product.query.order_by(Product.priority).all())

    def fetch_report_1(self):
        return render_template('admin/file/search_report.1.jinja',
                               entries = ReportType.query.order_by(ReportType.val).all())
    def fetch_report_2(self):
        return render_template('admin/file/search_report.2.jinja',
                               entries = Report.query\
                               .join(ReportString)\
                               .filter(Report.rt == request.args.get('rtid'))\
                               .order_by(ReportString.val)\
                               .all())

    def fetch_report_3(self):
        pid = int(request.args.get('pid'))
        rid = int(request.args.get('rid'))
        page = int(request.args.get('page', '0'))
        
        tk = 'admin.file.search.total.{}.{}'.format(pid, rid)

        total = queryCache(tk,
                           lambda: session.query(func.count(Pattern.file))\
                           .join(File)\
                           .filter(Pattern.product == pid)\
                           .filter(File.report == rid)\
                           .scalar())

        pageData = pagination(page, FILE_LIST_ROWS, total, lambda x: url_for('admin.file.search', mode='report', pid=pid, rid=rid, page=x))

        return render_template('admin/file/search_report.3.jinja',
                               total = total,
                               entries = Pattern.query\
                               .join(File)\
                               .filter(Pattern.product == pid)\
                               .filter(File.report == rid)\
                               .order_by(Pattern.pattern)\
                               .offset(page * FILE_LIST_ROWS)\
                               .limit(FILE_LIST_ROWS)\
                               .all(),
                               pageData = pagination(page, FILE_LIST_ROWS, total, lambda x: url_for('admin.file.search', mode='report', pid=pid, rid=rid, page=x)))

    def fetch_md5_0(self):
        return render_template('admin/file/search_md5.jinja')

    def fetch_md5_1(self):
        h = request.args.get('md5', '').strip().decode('hex')

        return render_template('admin/file/search_md5.jinja', entries=Pattern.query\
            .join(File)\
            .join(Product)\
            .filter(File.file_md5 == h)\
            .order_by(Product.priority)\
            .order_by(Pattern.pattern).all())

    def fetch_sha1_0(self):
        return render_template('admin/file/search_sha1.jinja')
    def fetch_sha1_1(self):
        h = request.args.get('sha1', '').strip().decode('hex')
        return render_template('admin/file/search_sha1.jinja', entries=Pattern.query\
                               .join(File)\
                               .join(Product)\
                               .filter(File.file_sha1 == h)\
                               .order_by(Product.priority)\
                               .order_by(Pattern.pattern).all())
    
fileIndex  = FileIndex.as_view('file.index')
fileList   = FileList.as_view('file.list')
fileSearch = FileSearch.as_view('file.search')

view.add_url_rule('file/', view_func=fileIndex)
view.add_url_rule('file/list', view_func=fileList)
view.add_url_rule('file/search/', view_func=fileSearch)
view.add_url_rule('file/search/<mode>', view_func=fileSearch)
view.add_url_rule('file/search/<mode>/<int:step>', view_func=fileSearch)

