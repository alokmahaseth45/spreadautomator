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


def Check_Server_File_Count(server_list):
	server_list_count = []
	server_list_count_dict = {}
	
	for s in server_list:
		# print glob.glob(s+'/*')
		x = len(glob.glob(s+'/*'))	
		server_list_count.append(x)
		server_list_count_dict.update({s: x})
	print server_list_count_dict
	s_count = server_list_count[0]
	print s_count
	if int(s_count)>50:
		exit()
	return min(server_list_count_dict,key=server_list_count_dict.get)


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

	
Process_Type = 'External'


page_break_error = 'D:\AR Conversion\Not_converted_single_pdf_files.txt'
html_move_problem = 'D:\AR Conversion\html_move_problem.txt'
server_txt_path = r"D:\Omni Servers\use servers.txt"
server_name_path =r'D:\Omni Servers\\' 
omni_savedir = r'E:\BSE India Annual Report\ProcessCode 100\OmniWatch100'

test_error_log = r"D:\AR Conversion\ProcessCode_Alok\Process Sequence\Log\Test_Error_Log.txt"

sql_process_path = 'D:\AR Conversion\ProcessCode_Alok\Request\External Process Sql Request\\'
New_Request_Path = r'D:\AR Conversion\ProcessCode_Alok\Request\External Omni Request'

while 1 == 1:
	
	with open(server_txt_path, 'r') as read_server:
		server_name = read_server.readlines()
	server_name = ['D:\Omni Servers\\'+x.replace('\n','') for x in server_name]
	check_server = Check_Server_File_Count(server_name)
	omni_savedir = check_server

	
	# search_dir = r'D:\Annual Reports\Requests'


	os.chdir(New_Request_Path)
	New_Request_List = filter(os.path.isfile, os.listdir(New_Request_Path))
	New_Request_List = [os.path.join(New_Request_Path, f) for f in New_Request_List if f.endswith('_New.txt')] # add path to each file
	New_Request_List.sort(key=lambda x: os.path.getmtime(x))
	# print New_Request_List
	if len(New_Request_List) == 0:
		print "Ext No Omni Request Remaining",datetime.now()


	for listpath_new in New_Request_List:

		try:

			#------------------------ Start Log Files ---------------------------------#
			# start_date  = time.strftime("%x %H:%M:%S")
			start_date = datetime.now()

			#------------------------ End Log Files ---------------------------------#

			print listpath_new
			if os.path.isfile(listpath_new):

				with open(listpath_new, 'r') as r:
					pdfinput = r.readlines()
				pdfinput = [x.replace('\n','') for x in pdfinput ]



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
				# Internal_process = req_new[1]+'_'+req_new[2]

				


				log_request = r'D:\AR Conversion\ProcessCode_Alok\Log\\'+Request_id+'_External.txt'
				call_log_bat = r'D:\AR Conversion\ProcessCode_Alok\Log\\log_request.bat'


				
				#------------------------ Start Log Files ---------------------------------#
				status = 'Start External Pixel conversion'
				Process_Head = 'Pixel Convert'
				Process_Name = 'Pixel Convert'
				Process_Time = '0'
				Current_Status = status
				Time_Stamp = str(start_date)
				# cal_end = end_date - start_date
				# Process_Time =  str(cal_end.total_seconds())
				# call_log(Request_id,status,call_log_bat)
				call_log_new(Request_id,Process_Type,Process_Head,Process_Name,Process_Time,Current_Status,Time_Stamp)
				#------------------------ End Log Files ---------------------------------#



				pdf_list = [x.replace('\n','') for x in pdfinput]

				bat_xlsx = listpath_new.replace('External Omni Request','External Process Sql Request')

				if os.path.isfile(bat_xlsx):
					os.remove(bat_xlsx)


				for pdf in pdf_list:
					input1 = PdfFileReader(open(pdf, "rb"))
					input1.getPage(0).mediaBox
					pxcel_files  = list(input1.getPage(0).mediaBox)
					
					if int(pxcel_files[2])>2015 or int(pxcel_files[3])>2015:
						x =  float(1000/float(pxcel_files[3]))
						print x
						# print input1.getPage(0).scale(0.5, 0.5)
						print input1.getPage(0).scaleBy(.3)
						output = PdfFileWriter()
						print input1.getPage(0).mediaBox
						file_folder = pdf.split('\\')
						p_name  = file_folder[-1]
						omni_filesave= omni_savedir+'\\'+p_name
						output.addPage(input1.getPage(0))
						outDoc = open(omni_filesave, 'wb')
						output.write(outDoc)
						outDoc.close()
						# pdb.set_trace()

					else:
						try:
							shutil.copy(pdf,omni_savedir)
						except Exception,e:
							print "Error in copying file to Omni Folder",str(e)

				for pdf in pdf_list:
					#-------- Start To Find Single Pdf Name   -----------
					pdf_path  =  pdf.split('\\')
					pdf_name = pdf_path[-1]
					#-------- End To Find Single Pdf Name  -----------
					
					
					#-------- Prefix Befor Excel and Text Name -----------
					prefix = '_000'
					pdf_xlsx_parameter = prefix+'1.xlsx'
					pdf_txt_parameter = prefix+'1.txt'
					pdf_htm_parameter = prefix+'1_Page1.htm'
					#-------- End Prefix Befor Excel and Text Name -----------
					

					#---------Start To Create Excel And Text Files In Main Folder------------
					pdf_xlsx= pdf.replace('.pdf',pdf_xlsx_parameter)
					pdf_txt = pdf.replace('Annual Reports','Annual Reports Converted Omni')
					pdf_txt= pdf_txt.replace('.pdf',pdf_txt_parameter)
					pdf_xlsx_main = pdf_xlsx= pdf.replace('.pdf','.xlsx')

					#---------End To Create Excel And Text Files In Main Folder------------

					#-------- Start "BSE Annual Reports Converted" xlsx_dir and xlsx_file  -----------
					xlsx_dir = pdf.replace(pdf_name,'').replace('Annual Reports','Annual Reports Converted Omni')
					xlsx_filesave = xlsx_dir+pdf_name
					xlsx_filesave_main = xlsx_filesave.replace('.pdf','.xlsx')
					xlsx_filesave = xlsx_filesave.replace('.pdf',pdf_xlsx_parameter)
					#-------- End "BSE Annual Reports Converted" xlsx_dir and xlsx_file  -----------

					#-------- Start To Create Excel And Text Files In Omni Folder   -----------
					omni_pdf_filesave = omni_savedir+'/'+pdf_name
					pdf_xlsx_omni= omni_pdf_filesave.replace('.pdf',pdf_xlsx_parameter)
					pdf_txt_omni= omni_pdf_filesave.replace('.pdf',pdf_txt_parameter)
					pdf_xlsx_main_omni= omni_pdf_filesave.replace('.pdf','.xlsx')
					# print "xxxxxxxxxxxxxxxxxxxxxxxxx",pdf_txt_omni

					#---------End To Create Excel And Text Files In Omni Folder------------

					omni_htm_dir = pdf_txt_omni.replace('.txt','_Dir')
					extra_omni_htm= pdf_xlsx_omni.replace('.xlsx','.htm')
					folder_name = omni_htm_dir.split('/')
					htm_name = folder_name[-1]
					htm_name = htm_name.replace('_Dir','_Page1.htm')
					omni_htm_filesave = omni_htm_dir+'/'+htm_name
					omni_htm_filesave_css = omni_htm_filesave.replace('_Page1.htm','.css')

					# D:\OmniWatch100\5000021210_3_0001_Dir

					htm_filesave = xlsx_filesave.replace('.xlsx','_Page1.htm')
					htm_filesave_css = htm_filesave.replace('_Page1.htm','.css')
					
					count_waiting = 0
					count_waiting1 = 0
					main_flag = 1
					converted_flag = 0
					
					while main_flag ==1:
						if os.path.isfile(omni_pdf_filesave) and os.path.isfile(pdf_xlsx_omni) and os.path.isfile(pdf_txt_omni):

							if not os.path.exists(xlsx_dir):
								os.makedirs(xlsx_dir)

							#-------- Move Excel And Text Files to Main And Converted Folder ----------
							
							# shutil.move(pdf_xlsx_omni,pdf_xlsx)
							# shutil.move(pdf_xlsx_omni,xlsx_filesave)
							try:
								shutil.move(pdf_xlsx_omni,xlsx_filesave)
							except:
								pass

							try:
								shutil.move(pdf_xlsx_main_omni,xlsx_filesave_main)
							except:
								pass

							# shutil.move(pdf_txt_omni,pdf_txt)


							try:
								shutil.move(pdf_txt_omni,pdf_txt)
							except:
								pass


							os.remove(omni_pdf_filesave)
							
							

							print "File moved to original folder"
							count_waiting = 0
							main_flag = 0
						else:
							print "waiting for Text and Excel  ",time.strftime("%x %H:%M:%S")
							time.sleep(30)
							count_waiting = count_waiting+1
							if count_waiting >30:
								count_waiting = 0
								count_waiting1 = count_waiting1+1
								if count_waiting1>5:
									main_flag = 0
									converted_flag = 1

				##----------------- Start To Append Excel File Path To VB script Bat file----------------------
				xlsx_bat =  "\n".join(pdf_list)
				with open(bat_xlsx, "w") as text_file:
					text_file.write(str(xlsx_bat)+'\n')
				##----------------- End To Append Excel File Path To VB script Bat file----------------------


			#------------------------ Start Log Files ---------------------------------#
			end_date = datetime.now()
			status = 'End External Pixel conversion'
			Process_Head = 'Pixel Convert'
			Process_Name = 'Pixel Convert'
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
				listpath_converting = listpath.replace('_Pending','_Ready')

			# if convert_error == 1:
			try:
				os.rename(listpath,listpath_converting)
			except:
				os.remove(listpath_converting)
				os.rename(listpath,listpath_converting)

		except Exception,e:
			print str(e)
			with open(test_error_log,'a') as er:
				er.write(Request_id+'|'+str(e)+'|'+str(datetime.now))
		
	time.sleep(2)
