# -*- coding:utf-8 -*-

import math

from pprint import pprint

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

class UpdateIndex(MethodView):
    @admin_required
    def get(self):
        return render_template('admin/update/index.jinja')

class UpdateAdd(MethodView):
    @admin_required
    def get(self):

        data = session.query(func.count(File.id),
                             Report.id,
                             Report.rt,
                             File.priority)\
                      .join(Report)\
                      .filter(File.status == -1)\
                      .filter(File.filesize != None)\
                      .group_by(File.priority)\
                      .group_by(Report.id)\
                      .all()

        entries = {}
        for c, r, rt, p in data:
            d = entries.get(r, { 'id': r, 'type': rt, 'normal': 0, 'high': 0 })
            if False == d.has_key('name'):
                d['name'] = Report.query.get(r).r_rs.val
                d['tname'] = ReportType.query.get(rt).val

            if 0 == p:
                d['normal'] = c
            else:
                d['high'] = c

            entries.update({r: d})

        return render_template('admin/update/add.jinja',
                               entries = sorted(entries.values(), key=lambda x: x.get('name')))

    @admin_required
    def post(self):
        try:
            session.execute('DELETE FROM staging WHERE cmd = 0')

            for fObj in File.query.filter(File.status == -1).filter(File.priority > 0).all():
                session.add(Staging(fObj, 0))

            addPattern = filter(lambda x: x[1] > 0, map(lambda x: (int(x[0]), int(x[1])), request.form.items()))

            for r, c in addPattern:
                for fObj in File.query\
                                .filter(File.status == -1)\
                                .filter(File.priority == 0)\
                                .filter(File.report == r)\
                                .filter(File.filesize != None)\
                                .order_by(File.id.desc())\
                                .limit(c)\
                                .all():
                    session.add(Staging(fObj, 0))

            session.commit()
        except Exception, msg:
            session.rollback()
            return redirect(url_for('base.error',
                                    head='데이터베이스 오류',
                                    message = str(msg),
                                    next=url_for('admin.update.add')))
        
        return redirect(url_for('admin.update.add'))

class UpdateDel(MethodView):

    @admin_required
    def get(self):
        return render_template('admin/update/del.jinja')

    @admin_required
    def post(self):
        m = request.args.get('mode', None)
        h = request.form.get('val', None)
        
        try:
            if m is None or h is None:
                raise IOError('Wrong parameter')

            v = h.decode('hex')

            fObj = None
            if m == 'md5':
                fObj = File.query.filter(File.status != -1).filter(File.file_md5 == v).first()
            else:
                fObj = File.query.filter(File.status != -1).filter(File.file_sha1 == v).first()

            if fObj is None:
                raise IOError('File not found')

            session.add(Staging(fObj, 1))
            session.commit()

            return render_template('admin/update/del.jinja', message="제거 패턴 추가 완료")
        except Exception, msg:
            session.rollback()
            return render_template('admin/update/del.jinja', message="제거 패턴 추가 실패: %r" % (str(msg), ))

class UpdateStatus(MethodView):
    @admin_required
    def get(self):
        return render_template('admin/update/status.jinja',
                               add_entries = Staging.query\
                               .join(File)\
                               .join(Report)\
                               .join(ReportType)\
                               .join(ReportString)\
                               .filter(Staging.cmd == 0)\
                               .order_by(File.priority)\
                               .order_by(ReportType.val)\
                               .order_by(ReportString.val)\
                               .all(),
                               del_entries = Staging.query\
                               .join(File)\
                               .join(Report)\
                               .join(ReportType)\
                               .join(ReportString)\
                               .filter(Staging.cmd == 1)
                               .order_by(ReportType.val)\
                               .order_by(ReportString.val)\
                               .all())

updateIndex  = UpdateIndex.as_view('update.index')
updateAdd    = UpdateAdd.as_view('update.add')
updateDel    = UpdateDel.as_view('update.del')
updateStatus = UpdateStatus.as_view('update.status')

view.add_url_rule('update/', view_func=updateIndex)
view.add_url_rule('update/add', view_func=updateAdd)
view.add_url_rule('update/del', view_func=updateDel)
view.add_url_rule('update/status', view_func=updateStatus)

################################################################################
