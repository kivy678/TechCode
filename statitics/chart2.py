# -*- coding:utf-8 -*-

###################################################### Environment ######################################################

import os, tempfile
import random

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

matplotlib.rcParams['axes.unicode_minus'] = False

path = r'C:\WINDOWS\Fonts\NanumBarunGothic.ttf'
font_name = fm.FontProperties(fname=path, size=48).get_name()
plt.rc('font', family=font_name)

#plt.rcParams['figure.figsize'] = (15,8)    #(x, y)
plt.rcParams['figure.figsize'] = (32,16)    #(x, y)
plt.rcParams['lines.linewidth'] = 2
#plt.rcParams['lines.color'] = 'r'
plt.rcParams['axes.grid'] = True 

########################################################################################################################

barWidth = 0.25
 
hbars1 = [392398, 459065, 1314316]
tbars1 = [970739, 1003285, 732869]

hbars2 = [256486, 298572, 879483]
tbars2 = [220829, 268517, 213728]

hbars3 = [238246, 280371, 859896]
tbars3 = [109035, 108496, 88687]
 
r1 = np.arange(len(hbars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

plt.bar(r1, hbars1, color='#48d1cc', width=barWidth, edgecolor='white', label=u'1-chart')
plt.bar(r2, hbars2, color='#6495ed', width=barWidth, edgecolor='white', label=u'2-chart')
plt.bar(r3, hbars3, color='#c71585', width=barWidth, edgecolor='white', label=u'3-chart')

plt.xlabel(u'x축', fontweight='bold')
plt.ylabel(u'y축', fontweight='bold')

plt.xticks([r + barWidth for r in range(len(hbars1))], [u'a~~~', u'b~~~', u'c~~~'])

plt.legend()
plt.show()

#f = tempfile.NamedTemporaryFile(dir='.', suffix='.png', delete=False)
#plt.savefig(f)
#f.close()

