# -*- coding:utf-8 -*-

import os

DBI = 'postgresql+psycopg2://a1:qwer1234@localhost/mus'

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
SITE_DIR   = os.path.join(BASE_DIR, 'data', 'site')
WORK_DIR   = os.path.join(BASE_DIR, 'data', 'work')
TMP_DIR    = os.path.join(BASE_DIR, 'data', 'tmp')
MANUAL_DIR = os.path.join(BASE_DIR, 'data', 'manual')
