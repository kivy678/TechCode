# -*- coding:utf-8 -*-

##########################################################################################

import xlsxwriter

##########################################################################################

SAVE_PATH 		= r"C:\tmp\test.xlsx"

##########################################################################################

workbook 		= xlsxwriter.Workbook(SAVE_PATH)
worksheet 		= workbook.add_worksheet('data1')						# 시트 이름


_properties 	= {'bold': True, 'font_color': 'red'}
cell_format 	= workbook.add_format(properties=_properties)			# 각 셀에 프로퍼티 값을 넣을 수 있음

#_format.set_font_color(color)											# 메소드를 이용한 프로퍼티 설정
#_format.set_bg_color(color)

#worksheet.write(		0,   0,   "hellow world", cell_format)         	# (0, 0) 쉘에 hellow world 단어를 넣음
#worksheet.write_row(	0, 	 0,   "hellow world", cell_format)     		# (0, 0) 을 기준으로 각 컬럼에 한 문자씩 넣음 (행 단위)
#worksheet.write_column(row, col, data, 		  cell_format)        	# (row, col) 을 기준으로 각 컬럼에 한 문자씩 넣음 (열 단위)

workbook.close()


print("Main Done...")
