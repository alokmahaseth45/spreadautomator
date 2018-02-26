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
import datetime

#engine = create_engine('mysql://username:password@host:port/database')
# engine = create_engine('mssql+pyodbc://sa:spot@99@127.0.0.1:1433/Sample100?driver=SQL Server')
engine = create_engine('mssql+pyodbc://sa:spot@99@127.0.0.1:1433/Annual_Reports_Raw?driver=SQL Server')

listpath_error = r'D:\AR Conversion\ProcessCode_Alok\error_read_excel_listpath_error.txt'
listpath = r'D:\BSE India Annual Report\error_read_excel.txt'
excel_listpath_error = r'D:\AR Conversion\ProcessCode_Alok\Process Sequence\Log\error_read_excel_listpath_error.txt'



# path = r"D:\AR Conversion\Annual Reports\admin\Pdf_Single_Files\50566b18-abdc-4798-94fb-4058c38f21fd_wildef-suitfiled-Oct-17_2_GridLine.pdf"
# path = r'C:\Users\john\Desktop\ProcessCodes\42f1566f-939f-4844-a69a-a5f49129cfa4_Attach bl HIMSKAF SYSTEMS PRIVATE LIMITED_1_0001.xlsx'
# path = r'D:\AR Conversion\Annual Reports\admin\Pdf_Single_Files\05ecf310-60c0-4d9d-95a4-e3f649af4ac6_NANA LAYJA POWER_1.pdf'
pdf_excel_path = path.replace('.pdf','_0001.xlsx')
pdf_excel_path = pdf_excel_path.replace('Annual Reports','Annual Reports Converted Omni')




if os.path.isfile(pdf_excel_path):
	ecount = 0
	excel_error = 1
	while excel_error == 1:
		try:
			print pdf_excel_path
			id_code = pdf_excel_path.split('\\')
			page_no = id_code[-1].replace('_0001','')
			# print id_code[-3]
			# unique = id_code[-3]
			page_no = page_no.replace('.txt','')
			# print "Page No Is : ",page_no


			# path = r'C:\Users\john\Desktop\ProcessCodes\42f1566f-939f-4844-a69a-a5f49129cfa4_Attach bl HIMSKAF SYSTEMS PRIVATE LIMITED_1_0001.xlsx'
			excel_folder = pdf_excel_path.split('\\')
			excel_name = excel_folder[-1]
			excel_name = excel_name.replace('.xlsx','')
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

			xl = pd.ExcelFile(pdf_excel_path)
			sheets = xl.sheet_names

			for sheet in sheets:
		
				table_name = 'Excel_To_Table_'+excel_name+'_'+sheet
				print table_name
				
				# df = xl.parse(sheet)
				# try:
				# 	df = pd.read_excel(xl,sheet)
				# except:
				# 	df = pd.read_excel(xl,sheet,header = None)

				# df = pd.read_excel(xl,sheet)

				try:
					df = pd.read_excel(xl,sheet,dtype=str)
					# df = pd.read_excel(path,dtype=str)
				except:
					# df = pd.read_excel(path,header = None)
					try:
						df = pd.read_excel(xl,sheet)
					except:	
						df = pd.read_excel(xl,sheet,header = None)


				

				# df = pd.read_excel(path)
				# print 'hi'
				print sheet
				# print df 
				# nb_levels = len(df.index[0])
				nblevels = df.index.nlevels 
				# print nb_levels
				# print "levels-----",nblevels
				exact_len = nblevels+len(df.columns)
				# print exact_len
				try:
					list_row = []
					for i in range(1,len(df.columns)+1):
						list_row.append('F'+str(i))
					try:
						df = pd.read_excel(xl,sheet,dtype=str,header = None)
					except:
						try:
							df = pd.read_excel(xl,sheet,header = None)
						except:	
							df = pd.read_excel(xl,sheet)

					df.replace(to_replace=['nan'], value='', inplace=True, limit=None, regex=False, method='pad', axis=None)

						
					df.columns = list_row
					df.to_sql(con=engine, name=table_name, if_exists='append')

				except:
					try:
						list_row = []
						for i in range(1,exact_len+1):
							list_row.append('F'+str(i))
						# df = xl.parse(sheet,header=None)
						try:
							df = pd.read_excel(xl,sheet,dtype=str,header = None)
						except:
							try:
								df = pd.read_excel(xl,sheet,header = None)
							except:	
								df = pd.read_excel(xl,sheet)

						df.replace(to_replace=['nan'], value='', inplace=True, limit=None, regex=False, method='pad', axis=None)
								
						df.columns = list_row
						df.to_sql(con=engine, name=table_name, if_exists='append')

					except Exception,e:
						print str(e)
						with open(excel_listpath_error, 'a') as f:
							f.write(pdf_excel_path +'|'+str(e)+'\n')
			
			excel_error = 0
		except Exception,e:
			ecount = ecount+1
			if ecount >4:

				with open(excel_listpath_error,'a') as er:
					er.write('Excel To DB Insertion Error '+'|'+pdf_excel_path+'|'+str(e)+'\n')

				excel_error = 0

else:
	with open(excel_listpath_error,'a') as lg:
		lg.write('Excel Not Found '+'|'+pdf_excel_path+str(datetime.datetime.now())+'\n')