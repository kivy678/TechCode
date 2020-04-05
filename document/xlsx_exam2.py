# -*- coding:utf-8 -*-

import pandas as pd

data = pd.read_excel(r"set\test.xlsx", sheet_name="data1", header=None, names=['A', 'B'])
print(data.head())


import xlsxwriter

workbook = xlsxwriter.Workbook(r"set\test2.xlsx")
worksheet = workbook.add_worksheet('data1')


_properties = {'bold': True, 'font_color': 'red'}
cell_format = workbook.add_format(properties=_properties)



row = 0
for i in data['A']:
	worksheet.write(row, 0, i, cell_format)         # 1개의 컬럼에 넣음
	row+=1


row = 0
for i in data['B']:
	worksheet.write(row, row, i)         # 1개의 컬럼에 넣음
	row+=1



workbook.close()
