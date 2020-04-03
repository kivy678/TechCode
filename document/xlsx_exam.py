# -*- coding:utf-8 -*-

##########################################################################################

import xlsxwriter

workbook = xlsxwriter.Workbook(r"set\test.xlsx")
worksheet = workbook.add_worksheet('data1')


_properties = {'bold': True, 'font_color': 'red'}
cell_format = workbook.add_format(properties=_properties)

#_format.set_font_color(color)
#_format.set_bg_color(color)


#worksheet.write(0, 0, "hellow world", cell_format)         # 1개의 컬럼에 넣음
#worksheet.write_row(0, 0, "hellow world", cell_format)     # 행을 기준으로 각 컬럼에 넣음
#worksheet.write_column(row, col, data, cell_format)        # 열을 기준으로 각 컬럼에 넣음

workbook.close()
