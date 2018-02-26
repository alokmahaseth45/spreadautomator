import sys
path = str(sys.argv[1])
import xlrd
import os
import codecs
import pdb
import requests
from lxml import html
import re
# import xlsxwriter
import pdb

import numpy as np
import pandas as pd
import pypyodbc
from sqlalchemy import create_engine

def Function_bat_run(bat):
	# print bat
	# bat = '""'+bat+'""'
	# print bat
	os.system(bat)
	return "Successfully"

#engine = create_engine('mysql://username:password@host:port/database')
# engine = create_engine('mssql+pyodbc://sa:spot@99@127.0.0.1:1433/Sample100?driver=SQL Server')
engine = create_engine('mssql+pyodbc://sa:spot@99@127.0.0.1:1433/Annual_Reports_Raw?driver=SQL Server')


listpath_error = 'D:\BSE India Annual Report\error_read_excel_listpath_error.txt'

listpath = 'D:\BSE India Annual Report\error_read_excel.txt'

# path = r"D:\AR Conversion\Annual Reports Converted Omni\sameer\Pdf_Single_Files\2e574de3-ac3f-48c4-9d39-e1fe14986060_ENKEI WHEELS INDIA LIMITED 8th AnnualReport2016-17ofEWIL_74_GridLine_0001.xlsx"
excel_folder = path.split('\\')
excel_name = excel_folder[-1]
excel_name = excel_name.replace('.xlsx','')
print excel_name

# path = path.replace("\\","/")

"""
Open and read an Excel file
"""
# book = xlrd.open_workbook(path)
# # print number of sheets
# print book.nsheets
# print type(book.nsheets)
# exit()


# print sheet names
# print book.sheet_names()
# sheets = book.sheet_names()
# comp_sheet = book.sheet_by_index(0)
# print comp_sheet.row_values(0)

# exit()
try:
	xl = pd.ExcelFile(path)
	sheets = xl.sheet_names
except:
	xl = pd.ExcelFile(path)
	sheets = xl.sheet_names



for sheet in sheets:
	table_name = 'Excel_To_Table_'+excel_name+'_'+sheet

	# bat_text_profit_Bat =  'sqlcmd -E -S localhost -d Annual_Reports_Raw -Q'+' '+ '"Exec DeleleExistingTable'+' '+ "'"+table_name+ "'"+'"'
	# # with open(grid_sql_file, "w") as text_file:
	# # 	text_file.write(str(bat_text_profit_Bat)+'\n')
	# Function_bat_run(bat_text_profit_Bat)




	# df = xl.parse(sheet)
	try:
		df = pd.read_excel(xl,sheet)
	except:
		df = pd.read_excel(xl,sheet,header = None)

	# df = pd.read_excel(path)
	print 'hi'
	print sheet
	# print df 
	# nb_levels = len(df.index[0])
	nblevels = df.index.nlevels 
	# print nb_levels
	print "levels-----",nblevels
	exact_len = nblevels+len(df.columns)
	print exact_len
	try:
		list_row = []
		for i in range(1,exact_len+1):
			list_row.append('F'+str(i))
		df = xl.parse(sheet,header=None)
		df.columns = list_row
		df.to_sql(con=engine, name=table_name, if_exists='replace')
		# df.DataFrame.to_sql

	except:
		try:
			list_row = []
			for i in range(1,len(df.columns)+1):
				list_row.append('F'+str(i))
			try:
				df = xl.parse(sheet,header=None)
				df.columns = list_row
			except:
				df = xl.parse(sheet)
				df.columns = list_row
			df.to_sql(con=engine, name=table_name, if_exists='replace')

		except:
			with open(listpath_error, 'a') as f:
				f.write(path +'\n')
	








	# for sheet in sheets:
	# 	table_name = 'Excel_To_Table_'+excel_name+'_'+sheet
	# 	# df = xl.parse(sheet)
	# 	df = pd.read_excel(path)
	# 	print 'hi'
	# 	print sheet

	# 	# print df 
	# 	# nb_levels = len(df.index[0])
	# 	nblevels = df.index.nlevels 
	# 	# print nb_levels
	# 	print nblevels
	# 	exact_len = nblevels+len(df.columns)
	# 	print exact_len
	# 	try:
	# 		list_row = []
	# 		for i in range(1,exact_len+1):
	# 			list_row.append('F'+str(i))
	# 		df = xl.parse(sheet,header=None)
	# 		df.columns = list_row
	# 		df.to_sql(con=engine, name=table_name, if_exists='append')

	# 	except:
	# 		try:
	# 			list_row = []
	# 			for i in range(1,len(df.columns)+1):
	# 				list_row.append('F'+str(i))
	# 			df = xl.parse(sheet)
	# 			df.columns = list_row
	# 			df.to_sql(con=engine, name=table_name, if_exists='append')

	# 		except:
	# 			with open(listpath_error, 'a') as f:
	# 				f.write(path +'\n')
		
	# 	# df.to_sql(con=engine, name=table_name, if_exists='append')


	# 	# exit()
	# 	# df.to_sql(con=engine, name=table_name, if_exists='append')
	# 	# try:
	# 	# 	df.to_sql(con=engine, name=table_name, if_exists='append')

	# 	# except Exception,e:
	# 	# 	print str(e)
	# 	# 	# exit()
	# 	# 	print "----------",len(df.columns)
	# 	# 	list_row = []
	# 	# 	for i in range(1,len(df.columns)+1):
	# 	# 		list_row.append('F'+str(i))
	# 	# 	try:
	# 	# 		df = xl.parse(sheet,header=None)
	# 	# 		df.columns = list_row
	# 	# 	except:
	# 	# 		df = xl.parse(sheet)
	# 	# 		df.columns = list_row
	# 	# 	print df

	# 	# 	df.to_sql(con=engine, name=table_name, if_exists='append')
	# 	