# -*- coding:utf-8 -*-

from pprint import pprint
import sys
import difflib

################################## context_diff ##################################
s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']

diff = difflib.context_diff(s1, s2, fromfile='beforename', tofile='aftername')
#sys.stdout.writelines(diff)


##################################### ndiff #####################################
diff = difflib.ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
                     'ore\ntree\nemu\n'.splitlines(keepends=True))

#print(''.join(diff), end="")

################################# unified_diff #################################
s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']

diff = difflib.unified_diff(s1, s2, fromfile='beforename', tofile='aftername')
#sys.stdout.writelines(diff)

#################################### Differ ####################################
with open(r'set\t1.txt') as fr:
    text1 = fr.readlines()

with open(r'set\t2.txt') as fr:
    text2 = fr.readlines()

d = difflib.Differ()
result = list(d.compare(text1, text2))
#pprint(result)
sys.stdout.writelines(result)
