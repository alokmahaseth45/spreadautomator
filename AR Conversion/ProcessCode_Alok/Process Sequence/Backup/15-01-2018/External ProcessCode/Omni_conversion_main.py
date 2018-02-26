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
from pyPdf import PdfFileWriter, PdfFileReader
from datetime import datetime



page_break_error = 'D:\AR Conversion\Not_converted_single_pdf_files.txt'
call_log_bat = r'D:\AR Conversion\ProcessCode_Alok\Log\\log_request.bat'

def copy_to_omni(pdf_name_single,omni_filesave):

	print "pdf_name_single : ",pdf_name_single

	shutil.copyfile(pdf_name_single,omni_filesave)

	return

def copy_xlsx_to_main_path(pdf_xlsx_omni,pdf_xlsx):

	shutil.copyfile(pdf_xlsx_omni,pdf_xlsx)

	return 


def Function_bat_run(bat):
	# print bat
	bat = '""'+bat+'""'
	print bat
	os.system(bat)
	# pdb.set_trace()
	
	return


def Check_Server_File_Count(server_list):
	server_list_count = []
	server_list_count_dict = {}
	
	for s in server_list:
		# print glob.glob(s+'/*')
		x = len(glob.glob(s+'/*.pdf'))
		server_list_count.append(x)
		server_list_count_dict.update({s: x})
	print server_list_count_dict
	s_count = server_list_count[0]
	print s_count
	# pdb.set_trace()

	# if int(s_count)>50:
	# 	exit()
	return min(server_list_count_dict,key=server_list_count_dict.get),s_count


# check for txt log and rerun if not present
def call_log_new(Request_id,Process_Type,Process_Head,Process_Name,Process_Time,Current_Status,Time_Stamp):
	bat_text_profit_Bat =  'sqlcmd -E -S localhost -d Annual_Reports -Q'+' '+ '"Exec SP_Read_Conversion_TimeLog'+' '+"'"+Request_id+"'"+', '+"'"+Process_Type+"'"+', '+"'"+Process_Head+"'"+', '+"'"+Process_Name+"'"+', '+"'"+Process_Time+"'"+', '+"'"+Current_Status+"'"+', '+"'"+Time_Stamp+"'"+'"'
	print bat_text_profit_Bat
	# pdb.set_trace()
	with open(call_log_bat, "w") as text_file:
		text_file.write(str(bat_text_profit_Bat)+'\n')

	if os.path.isfile(call_log_bat):
		Function_bat_run(call_log_bat)

	


page_break_error = 'D:\AR Conversion\Not_converted_single_pdf_files.txt'
html_move_problem = 'D:\AR Conversion\html_move_problem.txt'
server_txt_path = r"D:\Omni Servers\use servers.txt"
server_name_path =r'D:\Omni Servers\\' 
omni_savedir = r'D:\Omni Servers\localhost'



while 1 == 1:
	New_Request_List = []
	Request_Id_path = r"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path"
	test_error_log = r"D:\AR Conversion\ProcessCode_Alok\Process Sequence\Log\Test_Error_Log.txt"
	sql_process_path = 'D:\AR Conversion\ProcessCode_Alok\Request\Internal Process Sql Request\\'
	New_Request_Path = r'D:\AR Conversion\ProcessCode_Alok\Request\Internal Omni Request'


	os.chdir(New_Request_Path)
	New_Request_List = filter(os.path.isfile, os.listdir(New_Request_Path))
	New_Request_List = [os.path.join(New_Request_Path, f) for f in New_Request_List if f.endswith('_New.txt')] # add path to each file
	New_Request_List.sort(key=lambda x: os.path.getmtime(x))
	# print New_Request_List
	# exit()
	if len(New_Request_List) == 0:
		print "No new Int Process 2 Omni Conversion ",datetime.now()
		IntFlag = 0
	else:
		IntFlag = 1

	# print New_Request_List
	# pdb.set_trace()



	if IntFlag == 1:
		for listpath_new in New_Request_List:

			with open(server_txt_path, 'r') as read_server:
				server_name = read_server.readlines()
			server_name = ['D:\Omni Servers\\'+x.replace('\n','') for x in server_name]
			# check count from function only, do not check count again here
			check_server = Check_Server_File_Count(server_name)
			check_server,om_pdf_count = Check_Server_File_Count(server_name)
			omni_savedir = check_server
			running_text = omni_savedir+'/running.txt'

			# om_pdf_count  = len(glob.glob(omni_savedir+'/*.pdf'))
			print om_pdf_count


			if om_pdf_count == 0 and not os.path.isfile(running_text):
				listpath_Pending  = listpath_new.replace('_New.txt','_Pending.txt')
				try:
					if os.path.isfile(listpath_Pending):
						os.remove(listpath_Pending)
					os.rename(listpath_new,listpath_Pending)
				except Exception,e:
					# Write this error to txt file
					print str(e)
					

				omni_pdf_bat = r"D:\AR Conversion\ProcessCode_Alok\Process Sequence\External ProcessCode\omni_pdf_bat.bat"
				if os.path.isfile(omni_pdf_bat):
					os.remove(omni_pdf_bat)

				omni_pdf_text = 'call '+'"D:\AR Conversion\ProcessCode_Alok\Process Sequence\External ProcessCode\omni_code.py"' +' '+'"'+listpath_Pending+'"'+' '+'"'+omni_savedir+'"'+' '+'"Internal"'
				with open(omni_pdf_bat, 'w') as bt:
					bt.write(str(omni_pdf_text)+'\n')
					bt.write("exit"+'\n')

				# Function_bat_run(omni_pdf_bat)
				bat = '"start "" "'+omni_pdf_bat+'""'
				# bat = '""'+omni_pdf_bat+'""'
				os.system(bat)
				time.sleep(10)
			break

			# else:
			# 	break


			# # Start External Code if IntFlag == 0


	if IntFlag == 0:
		Process_Type = 'External'

		test_error_log = r"D:\AR Conversion\ProcessCode_Alok\Process Sequence\Log\Test_Error_Log.txt"
		sql_process_path = 'D:\AR Conversion\ProcessCode_Alok\Request\External Process Sql Request\\'
		New_Request_Path = r'D:\AR Conversion\ProcessCode_Alok\Request\External Omni Request'
		
		# search_dir = r'D:\Annual Reports\Requests'

		os.chdir(New_Request_Path)
		New_Request_List = filter(os.path.isfile, os.listdir(New_Request_Path))
		New_Request_List = [os.path.join(New_Request_Path, f) for f in New_Request_List if f.endswith('_New.txt')] # add path to each file
		New_Request_List.sort(key=lambda x: os.path.getmtime(x))
		print New_Request_List
		# pdb.set_trace()
		if len(New_Request_List) == 0:
			print "Ext No Omni Request Remaining",datetime.now()
			# time.sleep(1)

		else:

			for listpath_new in New_Request_List:

				with open(server_txt_path, 'r') as read_server:
					server_name = read_server.readlines()
				server_name = ['D:\Omni Servers\\'+x.replace('\n','') for x in server_name]
				check_server,om_pdf_count = Check_Server_File_Count(server_name)
				omni_savedir = check_server

				# om_pdf_count  = len(glob.glob(omni_savedir+'/*.pdf'))
				print om_pdf_count
				# pdb.set_trace()
				running_text = omni_savedir+'/running.txt'

				if om_pdf_count == 0 and not os.path.isfile(running_text):
					listpath_Pending  = listpath_new.replace('_New.txt','_Pending.txt')

					try:
						if os.path.isfile(listpath_Pending):
							os.remove(listpath_Pending)
						os.rename(listpath_new,listpath_Pending)
					except Exception,e:
						# Write this error to txt file
						print str(e)

					omni_pdf_bat = r"D:\AR Conversion\ProcessCode_Alok\Process Sequence\External ProcessCode\omni_pdf_bat.bat"
					if os.path.isfile(omni_pdf_bat):
						os.remove(omni_pdf_bat)

					omni_pdf_text = 'call '+'"D:\AR Conversion\ProcessCode_Alok\Process Sequence\External ProcessCode\omni_code.py"' +' '+'"'+listpath_Pending+'"'+' '+'"'+omni_savedir+'"'+' '+'"External"'
					with open(omni_pdf_bat, 'w') as bt:
						bt.write(str(omni_pdf_text)+'\n')
						bt.write("exit"+'\n')

					# Function_bat_run(omni_pdf_bat)
					bat = '"start "" "'+omni_pdf_bat+'""'
					# bat = '""'+omni_pdf_bat+'""'
					os.system(bat)
					time.sleep(10)

				break
				
		# time.sleep(2)

	time.sleep(2)
