# -*- coding:utf-8 -*-
# required python 3.5 이상
# pip install pyyaml

import os
import yaml

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
PATH = os.path.join(BASE_DIR, "exmple.yaml")

with open(PATH) as fr:
    print(yaml.load(fr.read()))

print('Done...')
