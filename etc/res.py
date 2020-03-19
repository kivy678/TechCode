# -*- coding:utf-8 -*-

#################################################################
import requests
from functools import partial

URL = "https://google.com"

rep = requests.get(URL)
print(rep.ok)

###################### exmaple ###############################
partial(requests.get, API_URL, params={'hash': _hash,}, verify=False, stream=True)
