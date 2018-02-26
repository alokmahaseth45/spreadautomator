import sys
list_path = str(sys.argv[1])
import xlrd
import os
import codecs
import pdb
import requests
from lxml import html
import re
# import xlsxwriter
import pdb
import datetime

import numpy as np
import pandas as pd
import pypyodbc
from sqlalchemy import create_engine

import uuid

#engine = create_engine('mysql://username:password@host:port/database')
# engine = create_engine('mssql+pyodbc://sa:spot@99@127.0.0.1:1433/Sample100?driver=SQL Server')
engine = create_engine('mssql+pyodbc://sa:spot@99@127.0.0.1:1433/Annual_Reports_Raw?driver=SQL Server')

listpath_error = r'D:\AR Conversion\ProcessCode_Alok\error_read_excel_listpath_error.txt'
listpath = r'D:\BSE India Annual Report\error_read_excel.txt'
excel_listpath_error = r'D:\AR Conversion\ProcessCode_Alok\Process Sequence\Log\error_read_excel_listpath_error.txt'

#engine = create_engine('mysql://username:password@host:port/database')
# engine = create_engine('mssql+pyodbc://sa:spot@99@127.0.0.1:1433/Sample100?driver=SQL Server')
engine = create_engine('mssql+pyodbc://sa:spot@99@127.0.0.1:1433/Annual_Reports_Raw?driver=SQL Server')

listpath_error = r'D:\AR Conversion\ProcessCode_Alok\error_read_excel_listpath_error.txt'
listpath = r'D:\BSE India Annual Report\error_read_excel.txt'
excel_listpath_error = r'D:\AR Conversion\ProcessCode_Alok\Process Sequence\Log\error_read_excel_listpath_error.txt'

list_path = list_path.replace("\\", "/")
print list_path
with open(list_path) as f:
    inputrow = f.readlines()
f.close()
inputrow = [x.replace('\n','') for x in inputrow]
# print inputrow
# exit()

pdf_links_list = list(inputrow)

pdf_links_list = [x for x in pdf_links_list if "Pdf_Single_Files"  in x]
for pdf_link in pdf_links_list:
	pdf_excel_path = pdf_link.replace('.pdf','_0001.xlsx')
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

				
				# print 'read excel',datetime.datetime.now()
				xl = pd.ExcelFile(pdf_excel_path)
				sheets = xl.sheet_names
				# print 'read excel done',datetime.datetime.now()

				for sheet in sheets:
					# print sheet
					table_name = 'Excel_To_Table_'+excel_name+'_'+sheet
					print table_name
					csv_name = r"D:\CSV Files"+'\\'+table_name+'.csv'
					
					if os.path.isfile(csv_name):
						os.remove(csv_name)
					
					df = pd.read_excel(xl,sheet,header=None)
					# df.replace(to_replace=['|'], value=' ', inplace=True, limit=None, regex=False, method='pad', axis=None)


					# print 'to sql',datetime.datetime.now()
					# df.to_sql(con=engine, name=table_name, if_exists='replace')
					# print csv_name
					df.to_csv(csv_name, sep='|',encoding='utf-8')
					log_name = str(uuid.uuid4())
					log_path = r"D:\CSV Files\Sql Log\\" + log_name + '.txt'
					query = 'sqlcmd -E -S WIN-6M9N8542A8D -d Annual_Reports_Raw -Q'+' '+ '"Exec Read_CSV '+"'"+csv_name+"','"+table_name+"'"+'"'+'>>"'+log_path+'"'
					# print query
					query_run_flag = 0
					while query_run_flag == 0:
						os.system(query)
						if os.path.isfile(log_path):
							query_run_flag = 1
							os.remove(log_path)
					# print 'to sql done',datetime.datetime.now()
					if os.path.isfile(csv_name):
						os.remove(csv_name)

				excel_error = 0
			except Exception,e:
				print 'Error2:',str(e)
				ecount = ecount+1
				if ecount >4:

					with open(excel_listpath_error,'a') as er:
						er.write('Excel To DB Insertion Error '+'|'+pdf_excel_path+'|'+str(e)+'|'+str(datetime.datetime.now())+'\n')

					excel_error = 0

	else:
		with open(excel_listpath_error,'a') as lg:
			lg.write('Excel Not Found '+'|'+pdf_excel_path+'|'+str(datetime.datetime.now())+'\n')
			







