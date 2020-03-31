# -*- coding:utf-8 -*-

import math

def pagination(c, r, t, f):

    ret = {}

    lp = int(math.floor(t/r))
    if 0 < (t % r):
        lp += 1

    sp = c - (c % 10)
    ep = min(sp + 10, lp)

    if 0 < sp:
        ret.update({'prev': f(sp-1)})

    if ep < lp:
        ret.update({'next': f(ep)})

    pages = []
    for page in xrange(sp, ep):
        if c == page:
            pages.append((page+1, '#'))
        else:
            pages.append((page + 1, f(page)))
    ret.update({'page': pages})

    return ret
