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
import Pdf_Text_To_Sql
from Pdf_Text_To_Sql import Insert_To_Sql
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

page_break_error = 'D:\AR Conversion\Not_converted_single_pdf_files.txt'
call_log_bat = r'D:\AR Conversion\ProcessCode_Alok\Log\\log_request.bat'

test_error_log = r"D:\AR Conversion\ProcessCode_Alok\Process Sequence\Log\Test_Error_Log.txt"



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


def call_log_new(Request_id,Process_Type,Process_Head,Process_Name,Process_Time,Current_Status,Time_Stamp):
	bat_text_profit_Bat =  'sqlcmd -E -S localhost -d Annual_Reports -Q'+' '+ '"Exec SP_Read_Conversion_TimeLog'+' '+"'"+Request_id+"'"+', '+"'"+Process_Type+"'"+', '+"'"+Process_Head+"'"+', '+"'"+Process_Name+"'"+', '+"'"+Process_Time+"'"+', '+"'"+Current_Status+"'"+', '+"'"+Time_Stamp+"'"+'"'
	print bat_text_profit_Bat
	# pdb.set_trace()
	with open(call_log_bat, "w") as text_file:
		text_file.write(str(bat_text_profit_Bat)+'\n')

	if os.path.isfile(call_log_bat):
		Function_bat_run(call_log_bat)

		



	
New_Request_Path = r'D:\AR Conversion\ProcessCode_Alok\Request\External Process Sql Request'
# search_dir = r'D:\Annual Reports\Requests'
while 1 == 1:
	os.chdir(New_Request_Path)
	New_Request_List = filter(os.path.isfile, os.listdir(New_Request_Path))
	New_Request_List = [os.path.join(New_Request_Path, f) for f in New_Request_List if f.endswith('_New.txt')] # add path to each file
	New_Request_List.sort(key=lambda x: os.path.getmtime(x))
	# print New_Request_List
	if len(New_Request_List) == 0:
		print "Ext process 3 db insert",datetime.now()


	Process_Type = 'External'

	for listpath_new in New_Request_List:
		listpath_Pending  = listpath_new.replace('_New','_Pending')
		os.rename(listpath_new,listpath_Pending)
		listpath = listpath_Pending
		# pdb.set_trace()

		# if 'Num1' in listpath_Pending:
		# 	print listpath_Pending
		# 	y = listpath_Pending.split('_')
		# 	# print y[-2]
		# 	num_l = y[-2]
		# 	num_l = num_l.split('-')
		# 	# print num_l[-1]
		# 	num_n = 'Num'+num_l[-1]
		# 	no_of_pages = num_l[-1]
		# 	final_n_path = listpath_Pending.replace('Num1',num_n).replace('_Pending','_Converted')

		if 'Num' in listpath_Pending:
			print listpath_Pending
			y = listpath_Pending.split('_')
			# print y[-2]
			num_l = y[-2]
			num_l = num_l.split('-')
			# print num_l[-1]
			num_f = num_l[0]
			print num_f
			num_n = 'Num'+num_l[-1]
			print num_n
			no_of_pages = num_l[-1]
			final_n_path = listpath_Pending.replace(num_f,num_n).replace('_Pending','_Converted')
			# print final_n_path




		with open(listpath) as f:
			inputrow = f.readlines()
		# f.close()
		# print inputrow
		pdf_files = [x.replace('\n','') for x in inputrow]
		# print inputrow

		request = listpath.split('\\')
		txt_file_name = request[-1]
		# Request_id = request[-1].replace('_New.txt','')
		Request_id = request[-1].replace('_Pending.txt','')

		Request_id = Request_id.strip()
		Request_id = Request_id.split('_')
		Request_id = Request_id[0].strip()
		print "Request Id Is : ",Request_id

		log_request = r'D:\AR Conversion\ProcessCode_Alok\Log\\'+Request_id+'_External.txt'
		call_log_bat = r'D:\AR Conversion\ProcessCode_Alok\Log\\log_request.bat'


		#------------------------ Start Log Files ---------------------------------#
		start_date = datetime.now()
		status = 'Start External insert text in sql'
		Process_Head = 'Db Insert'
		Process_Name = 'Test Db Insert'
		Process_Time = '0'
		Current_Status = status
		Time_Stamp = str(start_date)
		# cal_end = end_date - start_date
		# Process_Time =  str(cal_end.total_seconds())
		call_log_new(Request_id,Process_Type,Process_Head,Process_Name,Process_Time,Current_Status,Time_Stamp)
		#------------------------ End Log Files ---------------------------------#



		#----------------- Start To Insert Data Into MYSQL Database----------------------
		try:
			Insert_To_Sql(pdf_files,Request_id)
			convert_error =1
		except Exception,e:
			print "Error in inserting to sql",str(e)

			with open(test_error_log,'a') as er:
				er.write(Request_id+'|'+'Error in inserting Text to sql '+str(e)+'|'+str(datetime.now())+'\n')

		#----------------- End To Insert Data Into MYSQL Database----------------------


		#------------------------ Start Log Files ---------------------------------#
		end_date = datetime.now()
		status = 'End External insert text in sql'
		Process_Head = 'Db Insert'
		Process_Name = 'Test Db Insert'
		Process_Time = '0'
		Current_Status = status
		Time_Stamp = str(end_date)
		cal_end = end_date - start_date
		Process_Time =  str(cal_end.total_seconds())
		call_log_new(Request_id,Process_Type,Process_Head,Process_Name,Process_Time,Current_Status,Time_Stamp)
		#------------------------ End Log Files ---------------------------------#



		#------------------------ Start Log Files ---------------------------------#
		# start_date  = time.strftime("%x %H:%M:%S")
		start_date = datetime.now()
		status = 'Start External excel data in sql'
		Process_Head = 'Db Insert'
		Process_Name = 'Excel Db Insert'
		Process_Time = '0'
		Current_Status = status
		Time_Stamp = str(start_date)
		# cal_end = end_date - start_date
		# Process_Time =  str(cal_end.total_seconds())
		call_log_new(Request_id,Process_Type,Process_Head,Process_Name,Process_Time,Current_Status,Time_Stamp)
		#------------------------ End Log Files ---------------------------------#


		#----------------- Start To Insert Data Into MYSQL Database----------------------
		try:

			read_m_bat = "D:\AR Conversion\ProcessCode_Alok\Process Sequence\External ProcessCode\DB_Insert MT Batch.bat"
			multi_bat_path = r"D:\AR Conversion\ProcessCode_Alok\Process Sequence\External ProcessCode\multi_bat_file.bat"

			if os.path.isfile(multi_bat_path):
				os.remove(multi_bat_path)
				
			with open(read_m_bat,'r') as rd:
				inp = rd.read()
			inp = inp.replace('filename',txt_file_name)
			# print inp
			with open(multi_bat_path,'w') as wr:
				wr.write(inp)

			if os.path.isfile(multi_bat_path):
				Function_bat_run(multi_bat_path)

			converted_flag = 0
				
		except Exception,e:
			print "Error in inserting to sql",str(e)
			converted_flag = 1

			with open(test_error_log,'a') as er:
				er.write(Request_id+'|'+'Error in inserting Single Excel to sql '+str(e)+'|'+str(datetime.now())+'\n')

		# try:
		# 	read_excel_and_insert_to_db(pdf_files,Request_id)
		# 	converted_flag =0
		# except Exception,e:
		# 	print "Error in inserting to sql",str(e)
		# 	converted_flag = 1
		#----------------- End To Insert Data Into MYSQL Database----------------------


		#------------------------ Start Log Files ---------------------------------#
		end_date = datetime.now()
		status = 'End External excel data in sql'
		Process_Head = 'Db Insert'
		Process_Name = 'Excel Db Insert'
		Process_Time = '0'
		Current_Status = status
		Time_Stamp = str(end_date)
		cal_end = end_date - start_date
		Process_Time =  str(cal_end.total_seconds())
		call_log_new(Request_id,Process_Type,Process_Head,Process_Name,Process_Time,Current_Status,Time_Stamp)
		#------------------------ End Log Files ---------------------------------#

		


		if converted_flag == 1:
			listpath_converting = listpath.replace('_Pending','_Error')
		else:
			listpath_converting = listpath.replace('_Pending','_Converted')

		

		try:
			os.rename(listpath,listpath_converting)
		except:
			os.remove(listpath_converting)
			os.rename(listpath,listpath_converting)

		proc_check_flag = 0
		for i in range(1,int(no_of_pages)+1):
			final_n_path = 'D:\AR Conversion\ProcessCode_Alok\Request\External Process Sql Request\\'+Request_id+'_Num'+str(i)+'-'+no_of_pages+'_Converted.txt'
			print final_n_path
			if os.path.isfile(final_n_path):
				proc_check_flag = 1
				# pdb.set_trace()
			else:
				proc_check_flag = 0
				break
		# print final_n_path
		# print proc_check_flag
		# print '-------------------------------------'
		# pdb.set_trace()


		if proc_check_flag == 1:
		# if os.path.isfile(final_n_path):
			#====================Start Proc Call =========================#
			log_time_var = str(datetime.now())
			log_time_var = log_time_var.replace(':','-')

			bat_filesave = 'D:\AR Conversion\Request_ID\\'+str(Request_id)+'.bat'
			if os.path.isfile(bat_filesave):
				os.remove(bat_filesave)
			# sqlcmd -E -S localhost -d Annual_Reports -Q "Exec Annual_Reports.dbo.Update_OverviewNewSite_OnClick 'U24236MH1987PTC044813'">
			# bat_text =  'sqlcmd -E -S localhost -d Annual_Reports -Q'+' '+ '"Exec Annual_Reports.dbo.SPV_AR_Process_1'+' '+ "'"+Request_id+ "'"+'"'
			Proc_log = 'D:\AR Conversion\ProcessCode_Alok\Proc log\\'+'SPV_AR_Process_1_'+Request_id+'_'+log_time_var+'.txt'
			bat_text =  'sqlcmd -E -S localhost -d Annual_Reports -Q'+' '+ '"Exec Annual_Reports.dbo.SPV_AR_Process_1'+' '+ "'"+Request_id+ "'"+' "'+'>>'+'"'+Proc_log+'"'
			
			with open(bat_filesave, "w") as text_file:
				text_file.write(str(bat_text)+'\n')
				text_file.write("exit"+'\n')


			if os.path.isfile(bat_filesave):
				# Function_bat_run(bat_filesave)
				bat = '"start "" "'+bat_filesave+'""'
				print bat
				while not os.path.isfile(Proc_log):
					os.system(bat)
					time.sleep(1)
				# os.system(bat)

			#====================End Proc Call =========================#
	
	time.sleep(2)



		






	


