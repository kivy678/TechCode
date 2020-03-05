# -*- coding:utf-8 -*-

# pip install simplejson

import os
try:
    import simplejson as json
except ImportError:
    import json


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

PATH = os.path.join(BASE_DIR, "exmple.json")

string = {
    "int": 1,
    "string": "str",
    "list": [
        {
            "doble list": [
                "aa",
                "bb",
            ],
            "doble list2": "cc"
        }
    ]
}

with open(PATH, 'w') as fw:
    json.dump(string, fw, indent=4, separators=(',', ': '))


with open(PATH) as fr:
    j = json.load(fr)


print(j)


print('Done...')
