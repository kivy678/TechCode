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

xline = list(range(10))

one_chart = list(range(10))
two_chart = list(range(10))

random.shuffle(one_chart)
random.shuffle(two_chart)


ind = np.arange(len(xline))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, one_chart, width, color='SkyBlue', label=u'one_chart')
plot = ax.plot(ind, one_chart)

rects2 = ax.bar(ind + width/2, two_chart, width, color='IndianRed', label=u'two_chart')
plot = ax.plot(ind, two_chart)

ax.set_ylabel(u'x축')
ax.set_title(u' y축')

ax.set_xticks(ind)
ax.set_xticklabels(xline)

ax.legend()


def autolabel(rects, xpos='center'):
    xpos = xpos.lower()
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.47, 'left': 0.83}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
autolabel(rects2, "right")

plt.show()

#f = tempfile.NamedTemporaryFile(dir='.', suffix='.png', delete=False)
#plt.savefig(f)
#f.close()
