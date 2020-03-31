# -*- coding:utf-8 -*-

#################################################################
import requests
from functools import partial

URL = "https://google.com"

REQUEST_TIMEOUT = (5 * 60)
REQUEST_RECV_CHUNK_SIZE = 4096

rep = requests.get(URL)
print(rep.ok)

###################### exmaple ###############################
req = partial(requests.get, API_URL, params={'hash': _hash,}, URL, timeout=REQUEST_TIMEOUT, stream=True, verify=False,)

with open(out, 'wb') as fd:
    for chunk in req.iter_content(REQUEST_RECV_CHUNK_SIZE):
        fd.write(chunk)


