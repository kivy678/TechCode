# -*- coding:utf-8 -*-
# required python 3.5 이상
# pip install pyyaml

import os
import yaml

#BASE_DIR = os.path.dirname(os.path.realpath(__file__))
PATH = os.path.join("set", "exmple.yaml")

# 사전 형식으로 반환
with open(PATH) as fr:
    print(yaml.load(fr.read()))
# >>> {'root': {'sub_str': 'string', 'sub_int': 123, 'sub_bool': True, 'sub_lit': ['aaa', 'bbb', 'ccc']}}


print('Done...')
