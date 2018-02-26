import sys
import os
# import requests
import re
import csv
import requesocks
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
from pyPdf import PdfFileWriter, PdfFileReader
import GridLines
from GridLines import Convert_png_and_pdf
# pdf = r"C:\Users\john\Desktop\Resize_Pdf_Dpi\ahmedabad_cause_list_1.pdf"

# Request_id = str(sys.argv[1])
# # Request_id = 'e1cf758a-66a5-48c4-b97e-978fea80e75f'

# Internal_process = str(sys.argv[2])
# # Internal_process = 'Internal_1'

# try:
# 	page_type = str(sys.argv[3])
# except:
# 	page_type = 0

# page_type = str(page_type)
# # 0 Balance Sheet
# # 1 Notes
# try:
# 	reverse = str(sys.argv[4])
# except:
# 	reverse = 0
# Request_id = 'df6630c2-5594-42da-bcff-d463253120f2'






def copy_to_omni(pdf_name_single,omni_filesave):

	print "pdf_name_single : ",pdf_name_single

	shutil.copyfile(pdf_name_single,omni_filesave)

	return

def copy_xlsx_to_main_path(pdf_xlsx_omni,pdf_xlsx):

	shutil.copyfile(pdf_xlsx_omni,pdf_xlsx)

	return 



def Function_bat_run(bat):
	print bat
	bat = '""'+bat+'""'
	print bat
	os.system(bat)
	# pdb.set_trace()
	return



def call_log_new(Request_id,Process_Type,Process_Head,Process_Name,Process_Time,Current_Status,Time_Stamp):
	bat_text_profit_Bat =  'sqlcmd -E -S localhost -d Annual_Reports -Q'+' '+ '"Exec SP_Read_Conversion_TimeLog'+' '+"'"+Request_id+"'"+', '+"'"+Process_Type+"'"+', '+"'"+Process_Head+"'"+', '+"'"+Process_Name+"'"+', '+"'"+Process_Time+"'"+', '+"'"+Current_Status+"'"+', '+"'"+Time_Stamp+"'"+'"'
	print bat_text_profit_Bat
	# pdb.set_trace()
	with open(call_log_bat, "w") as text_file:
		text_file.write(str(bat_text_profit_Bat)+'\n')

	if os.path.isfile(call_log_bat):
		Function_bat_run(call_log_bat)

def Check_Server_File_Count(server_list):
	server_list_count = []
	server_list_count_dict = {}
	
	for s in server_list:
		# print glob.glob(s+'/*')
		x = len(glob.glob(s+'/*'))	
		server_list_count.append(x)
		server_list_count_dict.update({s: x})
	print server_list_count_dict
	# print min(server_list_count_dict,key=server_list_count_dict.get)
	return min(server_list_count_dict,key=server_list_count_dict.get)




omni_request_savedir = r'D:\AR Conversion\ProcessCode_Alok\Request\Internal Omni Request'



page_break_error = 'D:\AR Conversion\ProcessCode_Alok\Process Sequence\Internal ProcessCode\Not_converted_single_pdf_files.txt'
html_move_problem = 'D:\AR Conversion\ProcessCode_Alok\Process Sequence\Internal ProcessCode\html_move_problem.txt'
# Request_id = 'e3b6f8af-9717-4e50-83d3-571f80db3777'


# bat_xlsx = "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Bat_Call_Excel\\"+Request_id+".bat"

# if os.path.isfile(bat_xlsx):
# 	os.remove(bat_xlsx)

while 1 == 1:

	New_Request_Path = r"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path"
	# search_dir = r'D:\Annual Reports\Requests'
	os.chdir(New_Request_Path)
	New_Request_List = filter(os.path.isfile, os.listdir(New_Request_Path))
	New_Request_List = [os.path.join(New_Request_Path, f) for f in New_Request_List if f.endswith('_New.txt')] # add path to each file
	New_Request_List.sort(key=lambda x: os.path.getmtime(x))

	if len(New_Request_List) == 0:
		print "Int Process 1 ",datetime.now()

	for listpath_new in New_Request_List:
		#------------------------ Start Log Files ---------------------------------#
		# start_date  = time.strftime("%x %H:%M:%S")
		start_date = datetime.now()
		#------------------------ End Log Files ---------------------------------#
		print listpath_new
		if os.path.isfile(listpath_new):

			try:

				with open(listpath_new, 'r') as r:
					pdfinput = r.readlines()
				pdfinput = [x.replace('\n','') for x in pdfinput ]
				# print pdfinput
				# exit()

				# req = listpath_new.split('\\')
				# Request_id = req[-1].replace('_New.txt','')

				listpath_Pending  = listpath_new.replace('_New.txt','_Pending.txt')
				try:
					os.rename(listpath_new,listpath_Pending)
				except:
					os.remove(listpath_Pending)
					os.rename(listpath_new,listpath_Pending)

				listpath = listpath_Pending

				req_name = listpath.split('\\')
				req = req_name[-1]
				req_new = req.split('_')
				print req_new
				Request_id = req_new[0]
				Internal_process = req_new[1]+'_'+req_new[2]
				Process_Type = Internal_process
				print Internal_process
				print Request_id

				if "Internal_1" in Internal_process:
					log_request = r'D:\AR Conversion\ProcessCode_Alok\Log\\'+Request_id+'_Internal_1.txt'
				else:
					log_request = r'D:\AR Conversion\ProcessCode_Alok\Log\\'+Request_id+'_Internal_2.txt'


				call_log_bat = r'D:\AR Conversion\ProcessCode_Alok\Log\\log_request.bat'

				if os.path.isfile(log_request):
					os.remove(log_request)

				#------------------------ Start Log Files ---------------------------------#
				# start_date  = time.strftime("%x %H:%M:%S")
				start_date = datetime.now()
				start_date1 = datetime.now()
				status = 'Start '+Internal_process+ ' Pdf To GridLine Pdf'

				with open(log_request ,'a') as log:
					log.write('Start Collexting Pdf Files-->'+str(start_date)+'\n')

				Process_Head = Internal_process+' GridLine Code'
				Process_Name = Internal_process+' GridLine Code'
				Process_Time = '0'
				Current_Status = status
				Time_Stamp = str(start_date)

				call_log_new(Request_id,Process_Type,Process_Head,Process_Name,Process_Time,Current_Status,Time_Stamp)

				#------------------------ End Log Files ---------------------------------#


				


				if  os.path.isfile(listpath):
					with open(listpath,'r') as f:
						pdf_list = f.readlines()

				pdf_list = [x.replace('\n','') for x in pdf_list]

				pdf_files = []

				if len(pdf_list)>0:

					for pdf_p in pdf_list:
						p = pdf_p.split('|')

						try:
							page_type = p[1]
						except:
							page_type = 0
						page_type = str(page_type)
						try:
							reverse = p[2]
						except:
							reverse = 0

						pdf_g = p[0]
						pdf_g = pdf_g.strip()
						pdf_name = pdf_g.split('\\')[-1]
						# pdf_name_new = 'Gridline_'+pdf_name
						# pdf_new = pdf_g.replace(pdf_name,pdf_name_new)
						pdf_new = pdf_g
						print pdf_name
						print pdf_new
						# shutil.copy(pdf_g,pdf_new)

						# pdf_txt = pdf_link.replace('.pdf','.txt')
						if os.path.isfile(pdf_new):
							exe_file = "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\AutoBatch Pdf To Png.bat"
							bat_text = 'Call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\AutoBatch Pdf To Png.bat"'+' '+'"'+pdf_new+'"'
							print bat_text

							os.system(bat_text)
							pdf_new_png = pdf_new.replace('.pdf','.png')
							if os.path.isfile(pdf_new_png):
								print "xxxxxx"

								# call = "call " + '"D:\BSE India Annual Report\ProcessCode\GridLines.py"'+' '+'"'+pdf_new+'"'
								# os.system(call)

								return_converted_pdf = Convert_png_and_pdf(pdf_new,page_type,reverse)
								print return_converted_pdf

								pdf_files.append(return_converted_pdf)

					pdf_files_omni_request = "\n".join(pdf_files)
					omni_request_filesave = omni_request_savedir +'\\'+Request_id+'_'+Internal_process+'_New.txt'
					with open(omni_request_filesave,'w') as r:
						r.write(str(pdf_files_omni_request))

					#------------------------ Start Log Files ---------------------------------#
					# end_date  = time.strftime("%x %H:%M:%S")
					end_date = datetime.now()
					status = 'End '+Internal_process+ ' Pdf To GridLine Pdf'

					with open(log_request ,'a') as log:
						log.write('End Date to create Gridline Pdf and png-->'+str(end_date)+'\n')

					Process_Head = Internal_process+' GridLine Code'
					Process_Name = Internal_process+' GridLine Code'
					Process_Time = '0'
					Current_Status = status
					Time_Stamp = str(end_date)
					cal_end = end_date - start_date1
					Process_Time =  str(cal_end.total_seconds())

					call_log_new(Request_id,Process_Type,Process_Head,Process_Name,Process_Time,Current_Status,Time_Stamp)

					converted_flag = 0


					#------------------------ End Log Files ---------------------------------#

				else:

					#------------------------ Start Log Files ---------------------------------#
					# end_date  = time.strftime("%x %H:%M:%S")
					end_date = datetime.now()
					status = 'End '+Internal_process+ ' Pdf To GridLine Pdf Blank'

					with open(log_request ,'a') as log:
						log.write('End Date to create Gridline Pdf and png-->'+str(end_date)+'\n')

					Process_Head = Internal_process+' GridLine Code'
					Process_Name = Internal_process+' GridLine Code'
					Process_Time = '0'
					Current_Status = status
					Time_Stamp = str(start_date)
					cal_end = end_date - start_date1
					Process_Time =  str(cal_end.total_seconds())

					call_log_new(Request_id,Process_Type,Process_Head,Process_Name,Process_Time,Current_Status,Time_Stamp)

					bat_filesave = 'D:\AR Conversion\Request_ID\\'+str(Request_id)+'.bat'
					bat_text =  'sqlcmd -E -S localhost -d Annual_Reports -Q'+' '+ '"Exec Annual_Reports.dbo.SPV_Process_Internal_2'+' '+ "'"+Request_id+ "'"+'"'
					with open(bat_filesave, "w") as text_file:
						text_file.write(str(bat_text)+'\n')
						text_file.write("exit"+'\n')



					if os.path.isfile(bat_filesave):
						# Function_bat_run(bat_filesave)
						bat = '"start "" "'+bat_filesave+'""'
						print bat
						os.system(bat)

					converted_flag = 0


			except:
				converted_flag = 0

			if converted_flag == 1:
				listpath_converting = listpath.replace('_Pending','_Error')
			else:
				listpath_converting = listpath.replace('_Pending','_Done')

			# if convert_error == 1:
			try:
				os.rename(listpath,listpath_converting)
			except:
				os.remove(listpath_converting)
				os.rename(listpath,listpath_converting)

	time.sleep(2)
