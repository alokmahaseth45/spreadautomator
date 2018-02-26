import sys
# path = str(sys.argv[1])
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

#engine = create_engine('mysql://username:password@host:port/database')
# engine = create_engine('mssql+pyodbc://sa:spot@99@127.0.0.1:1433/Sample100?driver=SQL Server')
# engine = create_engine('mssql+pyodbc://sa:Alok@1234@127.0.0.1:1433/Sample100?driver=SQL Server')
engine = create_engine('mssql+pyodbc://sa:spot@99@127.0.0.1:1433/Annual_Reports_Raw?driver=SQL Server')


#engine = create_engine('mssql://localhost/1433?driver=SQL Server?trusted_connection=yes?Database=demo')
#exit()

# connection = pypyodbc.connect('Driver={SQL Server};'
# 								'Server=127.0.0.1,1433;'
# 								'Database=new_details;'
# 								'uid=sa;pwd=Alok@1234') 
# cursor = connection.cursor()
# import requesocks
# session = requesocks.session()
# session.proxies = {'http': 'socks5://127.0.0.1:9050',
# 					'https': 'socks5://127.0.0.1:9050'}
# listpath_error = 'D:\BSE India Annual Report\error_read_excel_listpath_error.txt'

# listpath = 'D:\BSE India Annual Report\error_read_excel.txt'
# # listpath = listpath.replace("\\", "/")
# print listpath
# with open(listpath) as f:
#     inputrow = f.readlines()
# f.close()
# inputrow = [x.replace('\n','') for x in inputrow]
# print inputrow
# exit()

pdf_paths = r'D:\AR Conversion\Test Excel'
inputrow = []
for root, dirs, files in os.walk(pdf_paths):
	for file in files:
		if file.endswith(".xlsx") or file.endswith(".xlsx"):
			# print(os.path.join(root, file))
			listpath1 = (os.path.join(root, file))
			# print listpath1
			# if "Pdf_Single_Files"  in listpath1
			# 	with open(pdf_text, "a") as text_file:
	  #               text_file.write(str(listpath1)+'\n')
			inputrow.append(listpath1)
		else:
			print "pdf not exixt in server folder"

for path in inputrow:
	print path
	# exit()


	# path = r'D:\BSE India Annual Report\BSE Annual Reports Converted 100\500092_CRISIL\Pdf_Single_Files\5000921216_214_0001.xlsx'
	excel_folder = path.split('\\')
	excel_name = excel_folder[-1]
	excel_name = excel_name.replace('.xlsx','')
	print excel_name
	
	# path = path.replace("\\","/")

	"""
	Open and read an Excel file
	"""
	book = xlrd.open_workbook(path)
	# # print number of sheets
	# print book.nsheets
	# print type(book.nsheets)
	# exit()


	# print sheet names
	# print book.sheet_names()
	sheets = book.sheet_names()
	# comp_sheet = book.sheet_by_index(0)
	# print comp_sheet.row_values(0)

	# exit()

	xl = pd.ExcelFile(path)
	# sheets = xl.sheet_names

	for sheet in sheets:
		table_name = 'Excel_To_Table_'+excel_name+'_'+sheet
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
			df.to_sql(con=engine, name=table_name, if_exists='append')

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
				df.to_sql(con=engine, name=table_name, if_exists='append')

			except:
				with open(listpath_error, 'a') as f:
					f.write(path +'\n')
	







