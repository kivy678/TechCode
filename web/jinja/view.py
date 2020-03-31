# -*- coding:utf-8 -*-

from flask import url_for
from modules.utils.report import IntToExtend

def pagination(data):
    ret = '<center><ul class="pagination">'
    
    if data.has_key('prev'):
        ret += '<li><a href="{}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(data.get('prev'))

    for display, link in data.get('page'):
        if '#' == link:
            ret += '<li class="active"><a href="{}">{}</a></li>'.format(link, display)
        else:
            ret += '<li><a href="{}">{}</a></li>'.format(link, display)

    if data.has_key('next'):
        ret += '<li><a href="{}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(data.get('next'))
        
    ret += '</ul></center>'
    
    return ret

def ReportExtend(s):
    if -1 == s:
        return ''
    else:
        return '.' + IntToExtend(s)

def PatternCommand(s):
    if -1 == s:
        return 'Ready'

    c = (s & 0x00000003)

    if 0 == c:
        return 'ADD'
    elif 1 == c:
        return 'DELETE'
    else:
        return 'UNKNOWN'

def MergeReport(r, e):
    if e is None or e == -1:
        return r

    return r + "." + IntToExtend(e)

def setup(app):
    app.jinja_env.globals.update(pagination=pagination)
    app.jinja_env.globals.update(ReportExtend=ReportExtend)
    app.jinja_env.globals.update(PatternCommand=PatternCommand)
    app.jinja_env.globals.update(MergeReport=MergeReport)
