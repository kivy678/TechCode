# -*- coding:utf-8 -*-

#################################################################
import requests
from functools import partial

URL = ""

REQUEST_TIMEOUT = (5 * 60)
REQUEST_RECV_CHUNK_SIZE = 4096

res = requests.get(URL)
print(res.ok)

###################### exmaple ###############################
res = partial(requests.get, URL, params={'arg': "arg", }, timeout=REQUEST_TIMEOUT, stream=True, verify=False,)

with open("FILE_PATH", 'wb') as fd:
    for chunk in res.iter_content(REQUEST_RECV_CHUNK_SIZE):
        fd.write(chunk)


fr = open("FILE_PATH", 'rb')
res = requests.post(URL, data={'arg': "arg", }, files={'file': ("fName", fr.read(), "multipart/form-data")})
fr.close()
