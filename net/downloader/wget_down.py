# -*- coding:utf-8 -*-

#############################################################################

from subprocess import call as subCall

WEB_USER = ''
WEB_PASSWD = ''
WEB_URL = ''
FILE_PATH = ''

#############################################################################

conn = f"wget -q --spider --http-user={WEB_USER} --http-passwd={WEB_PASSWD} {WEB_URL}"
if subCall(conn) != 0:
	print("Connect Faile")
	return False

down = f"wget -q -c --http-user={WEB_USER} --http-passwd={WEB_PASSWD} -O {FILE_PATH} {WEB_URL}"
subCall(down)
