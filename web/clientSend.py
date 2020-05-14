# -*- coding:utf-8 -*-

import requests


try:
    fr = open("FilePath", 'rb')

    res = requests.post("URL", data={'options': 'hello'},
                        files={'file': ("FileName", fr.read(), "multipart/form-data")})

finally:
    fr.close()
