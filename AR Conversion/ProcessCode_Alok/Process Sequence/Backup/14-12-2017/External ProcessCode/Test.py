import sys
import os
# import requests
import re
import csv
# import requesocks
import time
import datetime
import random
import datetime
import pdb
# from inclu import *
import codecs
import shutil
from shutil import copyfile
import glob
# import Pdf_Text_To_Sql
# from Pdf_Text_To_Sql import Insert_To_Sql
from pyPdf import PdfFileWriter, PdfFileReader
import pypyodbc

# from pyPdf import PdfFileWriter, PdfFileReader

# from PyPDF2 import PdfFileMerger
# pdf = "D:\AR Conversion\Annual Reports\\admin\Pdf_Single_Files\\14db0fba-2827-4e96-a269-692be4c6a365_Attach P P OIL PRIVATE LIMITED 2016_1.pdf"
# print type(pdf)
# input1 = PdfFileReader(file(pdf, "rb"))
# print "1st done"

# bat_filesave = "D:\AR Conversion\Request_ID\e1cf758a-66a5-48c4-b97e-978fea80e75f.bat"
# bat = '"start "" "'+bat_filesave+'""'
# print bat
# os.system(bat)

# exit()


def copy_to_omni(pdf_name_single,omni_filesave):

	print "pdf_name_single : ",pdf_name_single

	shutil.copyfile(pdf_name_single,omni_filesave)

	return

def break_pdf_page(pdf_link):
	try:
		# print "pdf lins is : ",pdf_link

		inputpdf = PdfFileReader(open(pdf_link, "rb"))
		# merger = PdfFileMerger()
		print "No of page in pdf : ",inputpdf.numPages
		total_page = inputpdf.numPages
		# print type(total_page)
		# pdb.set_trace()

		pdf_folder = pdf_link.split('\\')
		pdf_name = pdf_folder[-1]
		print "pdf name is : ",pdf_name
		# pdb.set_trace()
		pdf_single_filesave = pdf_link.replace(pdf_name,'')
		pdf_single_filesave = pdf_single_filesave+'Pdf_Single_Files/'
		# print pdf_single_filesave
		# pdb.set_trace()
		if not os.path.exists(pdf_single_filesave):
			os.makedirs(pdf_single_filesave)
		# print pdf_single_filesave
		

		for page_no in range(0,total_page):
			i = page_no

			# pdf_folder = pdf_link.split('\\')
			# pdf_name = pdf_folder[-1]
			output = PdfFileWriter()
			pdf_sub_files = pdf_name.replace('.pdf','_'+str(i+1)+'.pdf')
			sub_filesave =pdf_single_filesave +pdf_sub_files 
			if not os.path.isfile(sub_filesave):
				output.addPage(inputpdf.getPage(i))
				with open(sub_filesave, "wb") as outputStream:
					output.write(outputStream)

		return pdf_single_filesave

	except:
		with open(page_break_error, "a") as text_file:
			text_file.write(pdf_link+'\n')

			page_not_break = 'Page not break'

		return page_not_break

def Function_bat_run(bat):
	# print bat
	bat = '""'+bat+'""'
	print bat
	os.system(bat)
	# pdb.set_trace()
	return


def call_log(Request_id,status,call_log_bat):
	bat_text_profit_Bat =  'sqlcmd -E -S localhost -d Annual_Reports -Q'+' '+ '"Exec SP_Read_Conversion_Log'+' '+"'"+Request_id+"'"+', '+"'"+status+"'"+'"'
	with open(call_log_bat, "w") as text_file:
		text_file.write(str(bat_text_profit_Bat)+'\n')

	if os.path.isfile(call_log_bat):
		Function_bat_run(call_log_bat)

file_name = '5329150317_Num1-4_Converted.txt'
read_m_bat = "D:\AR Conversion\ProcessCode_Alok\Process Sequence\External ProcessCode\DB_Insert MT Batch.bat"


multi_bat_path = r"D:\AR Conversion\ProcessCode_Alok\Process Sequence\External ProcessCode\multi_bat_file.bat"

with open(read_m_bat,'r') as rd:
	inp = rd.read()
inp = inp.replace('filename',file_name)
print inp


with open(multi_bat_path,'w') as wr:
	wr.write(inp)

Function_bat_run(multi_bat_path)











x = '5329380317_Num1-2_New'
# y = x.split('_')
# print y[-2]
# num_l = y[-2]
# num_l = num_l.split('-')
# print num_l[-1]

if 'Num1' in x:
	print x
	y = x.split('_')
	print y[-2]
	num_l = y[-2]
	num_l = num_l.split('-')
	print num_l[-1]
	num_n = 'Num'+num_l[-1]
	z = x.replace('Num1',num_n)
	print z
















# exit()



