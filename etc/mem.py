# -*- coding:utf-8 -*-

from joblib import Memory

MEM = Memory('CACHE_DIR', verbose=0)

@MEM.cache
def test():
	pass
