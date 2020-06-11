# -*- coding:utf-8 -*-

import plotly.graph_objects as go


labels = ['a', 'b', 'c', 'd', 'e', 'f']
values = [55296824, 1043066, 1540694, 353, 954113, 1134911]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()

