import sys
import os
# import requests
import re
import csv
# import requesocks
import time
import datetime
import random
import pdb
# from inclu import *
import codecs
import shutil
from shutil import copyfile
import glob
# import Pdf_Text_To_Sql
# from Pdf_Text_To_Sql import Insert_To_Sql
import function_read_excel_and_insert
from function_read_excel_and_insert import read_excel_and_insert_to_db
from pyPdf import PdfFileWriter, PdfFileReader
import pypyodbc
from datetime import datetime


# from pyPdf import PdfFileWriter, PdfFileReader

# from PyPDF2 import PdfFileMerger
# pdf = "D:\AR Conversion\Annual Reports\\admin\Pdf_Single_Files\\14db0fba-2827-4e96-a269-692be4c6a365_Attach P P OIL PRIVATE LIMITED 2016_1.pdf"
# print type(pdf)
# input1 = PdfFileReader(file(pdf, "rb"))
# print "1st done"






def Function_bat_run(bat):
	try:
		print bat
		# bat = '""'+bat+'""'
		bat = '"start "" "'+bat+'""'
		# print bat
		os.system(bat)
		# pdb.set_trace()
		text = "Sucess"
	except:
		text = 'Error'
	return text	


# omni_request_savedir = r'D:\AR Conversion\ProcessCode_Alok\Omni Request'
	
# pdb.set_trace()
New_Request_Path = r'D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path'
# search_dir = r'D:\Annual Reports\Requests'
os.chdir(New_Request_Path)
New_Request_List = filter(os.path.isfile, os.listdir(New_Request_Path))
New_Request_List = [os.path.join(New_Request_Path, f) for f in New_Request_List if f.endswith('Call.bat')] # add path to each file
New_Request_List.sort(key=lambda x: os.path.getmtime(x))
print New_Request_List

# Process_Type = 'External'

for listpath_new in New_Request_List:

	listpath_new_pending  = listpath_new.replace('_Call.bat','_Pending.bat')
	try:
		os.rename(listpath_new,listpath_new_pending)
	except:
		os.remove(listpath_new_pending)
		os.rename(listpath_new,listpath_new_pending)
		

	text = Function_bat_run(listpath_new_pending)
	if "Sucess" in text:
		print "sucess"
		listpath_new_done = listpath_new_pending.replace('_Pending.bat','_Done.bat')
		# print listpath_new_done
		# pdb.set_trace()
		try:
			os.rename(listpath_new_pending,listpath_new_done)
		except:
			if os.path.isfile(listpath_new_done):
				os.remove(listpath_new_done)
				os.rename(listpath_new_pending,listpath_new_done)

	if 'Error' in text:
		listpath_new_done = listpath_new_pending.replace('_Pending.bat','_Error.bat')
		try:
			os.rename(listpath_new_pending,listpath_new_done)
		except:
			if os.path.isfile(listpath_new_done):
				os.remove(listpath_new_done)
				os.rename(listpath_new_pending,listpath_new_done)
		# os.rename(listpath_new,listpath_new_done)


