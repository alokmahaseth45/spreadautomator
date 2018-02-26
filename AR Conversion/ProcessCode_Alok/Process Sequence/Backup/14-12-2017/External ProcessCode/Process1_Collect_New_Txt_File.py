import sys
import os
# import requests
import re
import csv
# import requesocks
import time
import datetime
from datetime import datetime
import random
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

page_break_error = 'D:\AR Conversion\Not_converted_single_pdf_files.txt'
call_log_bat = r'D:\AR Conversion\ProcessCode_Alok\Log\\log_request.bat'


def copy_to_omni(pdf_name_single,omni_filesave):

	print "pdf_name_single : ",pdf_name_single

	shutil.copyfile(pdf_name_single,omni_filesave)

	return

def break_pdf_page(pdf_link):
	try:
		varp = open(pdf_link, "rb")
		inputpdf = PdfFileReader(varp)
		# merger = PdfFileMerger()
		print "No of page in pdf : ",inputpdf.numPages
		total_page = inputpdf.numPages
		# print type(total_page)
		# pdb.set_trace()

		pdf_folder = pdf_link.split('\\')
		pdf_name = pdf_folder[-1]
		# print "pdf name is : ",pdf_name
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
		varp.close()

		return pdf_single_filesave

	except:
		varp.close()
		with open(page_break_error, "a") as text_file:
			text_file.write(pdf_link+'\n')

			page_not_break = 'Page not break'

			# varp.close()


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



omni_request_savedir = r'D:\AR Conversion\ProcessCode_Alok\Request\External Omni Request'
	
# pdb.set_trace()
New_Request_Path = r'D:\Annual Reports\Requests'
# search_dir = r'D:\Annual Reports\Requests'


while 1 == 1:
	os.chdir(New_Request_Path)
	New_Request_List = filter(os.path.isfile, os.listdir(New_Request_Path))
	New_Request_List = [os.path.join(New_Request_Path, f) for f in New_Request_List if f.endswith('_New.txt')] # add path to each file
	New_Request_List.sort(key=lambda x: os.path.getmtime(x))
	# print New_Request_List
	if len(New_Request_List) == 0:
		print 'Ext Collect New Req',datetime.now()

	Process_Type = 'External'


	for listpath_new in New_Request_List:
		
		# start_date  = time.strftime("%x %H:%M:%S")
		start_date = datetime.now()
		print listpath_new
		# pdb.set_trace()
		if os.path.isfile(listpath_new):
			converted_flag = 0

			try:
				# listpath_done = listpath.replace('_New','_Done')
				listpath_Pending  = listpath_new.replace('_New','_Pending')
				os.rename(listpath_new,listpath_Pending)
				listpath = listpath_Pending
				# pdb.set_trace()

				with open(listpath) as f:
					inputrow = f.readlines()
				f.close()
				# print inputrow
				inputrow = [x.replace('\n','') for x in inputrow]
				print inputrow

				request = listpath.split('\\')
				# Request_id = request[-1].replace('_New.txt','')
				Request_id = request[-1].replace('_Pending.txt','')

				Request_id = Request_id.strip()
				print "Request Id Is : ",Request_id
				# pdb.set_trace()

				log_request = r'D:\AR Conversion\ProcessCode_Alok\Log\\'+Request_id+'_External.txt'
				call_log_bat = r'D:\AR Conversion\ProcessCode_Alok\Log\\log_request.bat'

				if os.path.isfile(log_request):
					os.remove(log_request)


				#------------------------ Start Log Files ---------------------------------#
				status = 'Start External Collecting New Files'
				Process_Head = 'Collect New Req'
				Process_Name = 'Collect New Req'
				Process_Time = '0'
				Current_Status = status
				Time_Stamp = str(start_date)
				call_log_new(Request_id,Process_Type,Process_Head,Process_Name,Process_Time,Current_Status,Time_Stamp)
				#------------------------ Start Log Files ---------------------------------#


				company_name = inputrow[0]
				company=company_name.split('::')
				company = company[1].strip()
				print "Company Name Is : ",company
				# pdb.set_trace()

				pdf_value = inputrow[1]
				pdf_name=pdf_value.split('::')
				pdf_name = pdf_name[1].strip()
				print "Main Pdf Name Is : ",pdf_name
				# pdb.set_trace()

				user_name_value = inputrow[3]
				username=user_name_value.split('::')
				username = username[1].strip()
				print "Pdf Path Is : ",username
				# pdb.set_trace()

				CIN_Value = inputrow[4]
				CIN=CIN_Value.split('::')
				CIN = CIN[1].strip()
				print "Pdf Path Is : ",CIN

				pdf_path_value = inputrow[2]
				pdf_upload_path=pdf_path_value.split('::')
				pdf_upload_path = pdf_upload_path[1].strip()
				print "Pdf Upload Path Is : ",pdf_upload_path
				# pdb.set_trace()

				# pdf_dir = r'D:\BSE India Annual Report\BSE Annual Reports/'+CIN
				pdf_dir = 'D:\\AR Conversion\\Annual Reports\\'+username
				
				end_date = datetime.now()

				
				#------------------------ Start Log Files ---------------------------------#
				status = 'End External Collecting New Files'

				Process_Head = 'Collect New Req'
				Process_Name = 'Collect New Req'
				Process_Time = '0'
				Current_Status = status
				Time_Stamp = str(end_date)
				cal_end = end_date - start_date
				Process_Time =  str(cal_end.total_seconds())
				call_log_new(Request_id,Process_Type,Process_Head,Process_Name,Process_Time,Current_Status,Time_Stamp)

				#------------------------ End Log Files ---------------------------------#



				pdf_path = pdf_dir+'\\'+ pdf_name
				# if os.path.isfile(pdf_path):
				# 	os.remove(pdf_path)


				if not os.path.isfile(pdf_path):
					if not os.path.exists(pdf_dir):
						os.makedirs(pdf_dir)
					shutil.copy(pdf_upload_path,pdf_dir)

					if '.PDF' in pdf_path:
						# print pdf_path
						# pdb.set_trace()
						pdf_path_1 = pdf_path.replace('.PDF','.pdf')
						os.rename(pdf_path,pdf_path_1)
						pdf_path = pdf_path_1
						pdf_name = pdf_name.replace('.PDF','.pdf')
						time.sleep(1)

				else:
					print "PDF is aready exist in BSE Folder"
				

				print "Pdf BSE Path Is : ",pdf_path
				# pdb.set_trace()

				CompanyID_Value = inputrow[4]
				CompanyID = CompanyID_Value.split('::')
				CompanyID = CompanyID[1].strip()
				print "Pdf Path Is : ",CompanyID

				# start_date  = time.strftime("%x %H:%M:%S")
				start_date = datetime.now()

				return_output = break_pdf_page(pdf_path)
				print "Return Out Put Is :",return_output


				

				if "Page not break"  in return_output:
					print "Page not break"
					shutil.copy(pdf_path,'D:\AR Conversion\ProcessCode_Alok\Process Sequence\Pdf Not Break\\')
					# shutil.copy(pdf_path,pdf_dir)

					exe_file = "D:\AR Conversion\ProcessCode_Alok\Process Sequence\External ProcessCode\AutoBatch Optimize Pdf.bat"
					bat_text_break = 'Call "D:\AR Conversion\ProcessCode_Alok\Process Sequence\External ProcessCode\AutoBatch Optimize Pdf.bat"'+' '+'"'+pdf_path+'"'
					print bat_text_break
					os.system(bat_text_break)
					# os.remove(pdf_path)
					pdf_path1 = pdf_dir+'\\'+'Break_'+pdf_name
					os.rename(pdf_path1,pdf_path)
					return_output = break_pdf_page(pdf_path)
					if "Page not break"  in return_output:
						print "Again Page not break"
						listpath_converting = listpath.replace('_Pending','_Error_Page_not_break')
						os.rename(listpath,listpath_converting)
						break
				else:

					#------------------------ Start Log Files ---------------------------------#
					start_date = datetime.now()
					status = 'Start External Collecting Single Pdf Files'
					Process_Head = 'Collect New Req'
					Process_Name = 'Break Pdf Page'
					Process_Time = '0'
					Current_Status = status
					# Time_Stamp = str(end_date)
					# cal_end = end_date - start_date
					# Process_Time =  str(cal_end.total_seconds())
					call_log_new(Request_id,Process_Type,Process_Head,Process_Name,Process_Time,Current_Status,Time_Stamp)
					#------------------------ End Log Files ---------------------------------#

					pdf_single_filesave = return_output
					# print pdf_single_filesave
					pdf_name_without_extention = pdf_name.replace('.pdf','')
					# print pdf_name_without_extention


					#-------- Start To Get Single Pdf Files   -----------
					pdf_files = glob.glob(pdf_single_filesave+'/*'+'.pdf')
					# print "pdf files is : ",pdf_files
					pdf_files = [x for x in pdf_files if pdf_name_without_extention in x]
					#-------- End To Get Single Pdf Files   -----------


					# pdf_files_omni_request = "\n".join(pdf_files)
					# omni_request_filesave = omni_request_savedir +'\\'+Request_id+'_New.txt'
					# with open(omni_request_filesave,'w') as r:
					# 	r.write(str(pdf_files_omni_request))


					n = 80
					pdf_page_break_list = [pdf_files[i:i + n] for i in xrange(0, len(pdf_files), n)]
					counter_pdf_list = 0

					for pdf_list in pdf_page_break_list:
						print "Count of file move to omni from pdf list",len(pdf_list)
						counter_pdf_list = counter_pdf_list+1
						# bat_xlsx = 'D:\AR Conversion\ProcessCode_Alok\Process Sql Request\\'+str(Request_id)+'_Num'+str(counter_pdf_list)+'-'+str(len(pdf_page_break_list))+'_New.txt'
						bat_xlsx = omni_request_savedir+'\\'+str(Request_id)+'_Num'+str(counter_pdf_list)+'-'+str(len(pdf_page_break_list))+'_New.txt'
						xlsx_bat =  "\n".join(pdf_list)
						with open(bat_xlsx, "w") as text_file:
							text_file.write(str(xlsx_bat)+'\n')

					


					#------------------------ Start Log Files ---------------------------------#
					# end_date  = time.strftime("%x %H:%M:%S")
					end_date = datetime.now()
					
					status = 'End External Collecting Single Pdf Files'
					Process_Head = 'Collect New Req'
					Process_Name = 'Break Pdf Page'
					Process_Time = '0'
					Current_Status = status
					Time_Stamp = str(end_date)
					cal_end = end_date - start_date
					Process_Time =  str(cal_end.total_seconds())
					# call_log(Request_id,status,call_log_bat)
					call_log_new(Request_id,Process_Type,Process_Head,Process_Name,Process_Time,Current_Status,Time_Stamp)
					# call_log(Request_id,status,call_log_bat)
					converted_flag = 0

					#------------------------ End Log Files ---------------------------------#
			except:
				converted_flag = 1



			if converted_flag == 1:
				listpath_converting = listpath.replace('_Pending','_Error')
			else:
				listpath_converting = listpath.replace('_Pending','_Converted')

			try:
				os.rename(listpath,listpath_converting)
			except:
				os.remove(listpath_converting)
				os.rename(listpath,listpath_converting)


	time.sleep(2)
