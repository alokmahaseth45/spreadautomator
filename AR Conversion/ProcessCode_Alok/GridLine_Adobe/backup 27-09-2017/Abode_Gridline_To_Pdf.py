import sys
import os
# import requests
import re
import csv
import requesocks
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
# from pyPdf import PdfFileWriter, PdfFileReader
import GridLines
from GridLines import Convert_png_and_pdf
# pdf = r"C:\Users\john\Desktop\Resize_Pdf_Dpi\ahmedabad_cause_list_1.pdf"
# shutil.copy(pdf,pdf_new)

Request_id = str(sys.argv[1])
# Request_id = '5000021210'

start_date  = time.strftime("%x %H:%M:%S")
print start_date
log_request = r'D:\AR Conversion\ProcessCode_Alok\Log\\'+Request_id+'.txt'



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


page_break_error = 'D:\AR Conversion\Not_converted_single_pdf_files.txt'
html_move_problem = 'D:\AR Conversion\html_move_problem.txt'
# Request_id = 'e3b6f8af-9717-4e50-83d3-571f80db3777'
server_txt_path = r"D:\BSE India Annual Report\ProcessCode 100\Omni Servers\use servers.txt"
server_name_path =r'D:\BSE India Annual Report\ProcessCode 100\Omni Servers\\' 
omni_savedir = r'D:\BSE India Annual Report\ProcessCode 100\OmniWatch100'
Request_Id_path = r"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path"

bat_xlsx = "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Bat_Call_Excel\\"+Request_id+".bat"

if os.path.isfile(bat_xlsx):
	os.remove(bat_xlsx)

# with open(server_txt_path, 'r') as read_server:
# 	server_name = read_server.readlines()
# server_name = ['D:\BSE India Annual Report\ProcessCode 100\Omni Servers\\'+x.replace('\n','') for x in server_name]
# check_server = Check_Server_File_Count(server_name)
# omni_savedir = check_server



start_date  = time.strftime("%x %H:%M:%S")

request_txt = Request_Id_path+'\\'+Request_id+'.txt'
print request_txt
if  os.path.isfile(request_txt):
	with open(request_txt,'r') as f:
		pdf_list = f.readlines()

pdf_list = [x.replace('\n','') for x in pdf_list]

end_date  = time.strftime("%x %H:%M:%S")
with open(log_request ,'a') as log:
	log.write('Start Date of collecting New.txt File-->'+start_date+'\n')
	log.write('End Date of collecting New.txt File-->'+end_date+'\n')

# print pdf_list
# exit()
pdf_files = []



# pdf_files = ['C:\\Users\\john\\Desktop\\Resize_Pdf_Dpi\\GridLine_Pdf\\Gridline_91d0b8f2-fddb-4f42-b3b1-04340698b106_AURUM SOFT SYSTEMS LIMITED 110820161470882709Aurum Annual Report- 2016_E-Version_48_converted.pdf','C:\\Users\\john\\Desktop\\Resize_Pdf_Dpi\\GridLine_Pdf\\Gridline_91d0b8f2-fddb-4f42-b3b1-04340698b106_AURUM SOFT SYSTEMS LIMITED 110820161470882709Aurum Annual Report- 2016_E-Version_52_converted.pdf','C:\\Users\\john\\Desktop\\Resize_Pdf_Dpi\\GridLine_Pdf\\Gridline_91d0b8f2-fddb-4f42-b3b1-04340698b106_AURUM SOFT SYSTEMS LIMITED 110820161470882709Aurum Annual Report- 2016_E-Version_54_converted.pdf','C:\\Users\\john\\Desktop\\Resize_Pdf_Dpi\\GridLine_Pdf\\Gridline_91d0b8f2-fddb-4f42-b3b1-04340698b106_AURUM SOFT SYSTEMS LIMITED 110820161470882709Aurum Annual Report- 2016_E-Version_56_converted.pdf','C:\\Users\\john\\Desktop\\Resize_Pdf_Dpi\\GridLine_Pdf\\Gridline_91d0b8f2-fddb-4f42-b3b1-04340698b106_AURUM SOFT SYSTEMS LIMITED 110820161470882709Aurum Annual Report- 2016_E-Version_58_converted.pdf','C:\\Users\\john\\Desktop\\Resize_Pdf_Dpi\\GridLine_Pdf\\Gridline_91d0b8f2-fddb-4f42-b3b1-04340698b106_AURUM SOFT SYSTEMS LIMITED 110820161470882709Aurum Annual Report- 2016_E-Version_60_converted.pdf','C:\\Users\\john\\Desktop\\Resize_Pdf_Dpi\\GridLine_Pdf\\Gridline_91d0b8f2-fddb-4f42-b3b1-04340698b106_AURUM SOFT SYSTEMS LIMITED 110820161470882709Aurum Annual Report- 2016_E-Version_62_converted.pdf','C:\\Users\\john\\Desktop\\Resize_Pdf_Dpi\\GridLine_Pdf\\Gridline_91d0b8f2-fddb-4f42-b3b1-04340698b106_AURUM SOFT SYSTEMS LIMITED 110820161470882709Aurum Annual Report- 2016_E-Version_8_converted.pdf', 'C:\\Users\\john\\Desktop\\Resize_Pdf_Dpi\\GridLine_Pdf\\Gridline_Gridline_91d0b8f2-fddb-4f42-b3b1-04340698b106_AURUM SOFT SYSTEMS LIMITED 110820161470882709Aurum Annual Report- 2016_E-Version_48_converted.pdf']
start_date  = time.strftime("%x %H:%M:%S")


for pdf_g in pdf_list:
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

			return_converted_pdf = Convert_png_and_pdf(pdf_new)
			print return_converted_pdf

			pdf_files.append(return_converted_pdf)

end_date  = time.strftime("%x %H:%M:%S")
with open(log_request ,'a') as log:
	log.write('Start Date to create Gridline Pdf and png-->'+start_date+'\n')
	log.write('End Date to create Gridline Pdf and png-->'+end_date+'\n')
 


# print pdf_files

start_date  = time.strftime("%x %H:%M:%S")

# print type(pdf_files)
for pdf in pdf_files:
	# print pdf 
	# pdf = "D:\AR Conversion\Annual Reports\\admin\Pdf_Single_Files\\14db0fba-2827-4e96-a269-692be4c6a365_Attach P P OIL PRIVATE LIMITED 2016_1.pdf"
	# print type(pdf)
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

end_date  = time.strftime("%x %H:%M:%S")
with open(log_request ,'a') as log:
	log.write('Start Date_Time to copy single pdf in server folder for omni coversion-->'+start_date+'\n')
	log.write('End Date_Time to copy single pdf in server folder for omni coversion-->'+end_date+'\n')


# time.sleep(5)

# bat_xlsx = 'D:\BSE Report Upload Check\VB Script Open Close Excel bat/'+str(Request_id)+'.bat'



start_date  = time.strftime("%x %H:%M:%S")

excel_run_flag = 0
for pdf in pdf_files:
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
	
	print pdf

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
	print xlsx_filesave
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
	print "--------------",omni_htm_filesave
	# 


	htm_filesave = xlsx_filesave.replace('.xlsx','_Page1.htm')
	htm_filesave_css = htm_filesave.replace('_Page1.htm','.css')
	# print htm_filesave
	# pdb.set_trace()


	# print omni_pdf_filesave
	
	# print pdf_xlsx_omni
	# print pdf_txt_omni
	# pdb.set_trace()

	count_waiting = 0
	count_waiting1 = 0
	main_flag = 1
	converted_flag = 0
	# print omni_pdf_filesave
	# print pdf_xlsx_omni
	# print pdf_txt_omni
	# print omni_htm_filesave
	# print extra_omni_htm
	# pdb.set_trace()



	while main_flag ==1:
		if os.path.isfile(omni_pdf_filesave) and os.path.isfile(pdf_xlsx_omni) and os.path.isfile(pdf_txt_omni) and os.path.isfile(extra_omni_htm):
		# if os.path.isfile(omni_pdf_filesave) and os.path.isfile(pdf_xlsx_omni) and os.path.isfile(pdf_txt_omni) and os.path.isfile(omni_htm_filesave) and os.path.isfile(extra_omni_htm):

		# if os.path.isfile(omni_pdf_filesave) and os.path.isfile(pdf_xlsx_omni) and os.path.isfile(pdf_xlsx_main_omni) and os.path.isfile(pdf_txt_omni) and os.path.isfile(extra_omni_htm):

			if not os.path.exists(xlsx_dir):
				os.makedirs(xlsx_dir)

			#-------- Move Excel And Text Files to Main And Converted Folder ----------
			
			# shutil.move(pdf_xlsx_omni,pdf_xlsx)
			shutil.move(pdf_xlsx_omni,xlsx_filesave)
			# try:
			# 	shutil.move(pdf_xlsx_main_omni,xlsx_filesave_main)
			# except:
			# 	pass
			shutil.move(pdf_txt_omni,pdf_txt)
			try:
				shutil.move(omni_htm_filesave,htm_filesave)
			except:
				# pass
				print omni_htm_filesave
				with open(html_move_problem, "a") as text_file:
					text_file.write(omni_htm_filesave+'|'+htm_filesave+'|'+pdf+'\n')

			try:
				shutil.copy(omni_htm_filesave_css,htm_filesave_css)
			except:
				pass


			#-------- Converted To Move Excel And Text Files to Main And Converted Folder ----------


			#-------- Start Delete Pdf Files From Omni ----------

			os.remove(omni_pdf_filesave)
			try:
				shutil.rmtree(omni_htm_dir)
			except:
				print "Folder not deleted"
			try:
				os.remove(extra_omni_htm)
			except:
				pass

			#-------- End Delete Pdf Files From Omni ----------


			xlsx_filesave_main = xlsx_filesave.replace('_GridLine_','_')


			#----------------- Start To Append Excel File Path To VB script Bat file----------------------

			xlsx_bat =  'call '+'"D:\AR Conversion\ProcessCode_Alok\Open Excel And Read Data\open_And_Read_Excel_Omni_Gridline.py"'+' '+'"'+xlsx_filesave+'"'
			xlsx_bat_main =  'call '+'"D:\AR Conversion\ProcessCode_Alok\Open Excel And Read Data\open_And_Read_Excel_Omni_Gridline.py"'+' '+'"'+xlsx_filesave_main+'"'

			with open(bat_xlsx, "a") as text_file:
				text_file.write(str(xlsx_bat)+'\n')

			with open(bat_xlsx, "a") as text_file:
				text_file.write(str(xlsx_bat_main)+'\n')

			#----------------- End To Append Excel File Path To VB script Bat file----------------------

			

			print "File moved to original folder"
			count_waiting = 0
			main_flag = 0
			excel_run_flag = 1
		else:
			# print omni_pdf_filesave
			# print pdf_xlsx_omni
			# print pdf_txt_omni
			# print omni_htm_filesave
			# print extra_omni_htm
			print "waiting for Text and Excel"
			time.sleep(30)
			count_waiting = count_waiting+1
			if count_waiting >30:
				count_waiting = 0
				count_waiting1 = count_waiting1+1
				if count_waiting1>5:
					main_flag = 0
					converted_flag = 1

end_date  = time.strftime("%x %H:%M:%S")
with open(log_request ,'a') as log:
	log.write('Start Waiting Date_Time for omni conversion and move files-->'+start_date+'\n')
	log.write('End Waiting Date_Time for omni conversion and move files-->'+end_date+'\n')




start_date  = time.strftime("%x %H:%M:%S")
if excel_run_flag == 1:
	Function_bat_run(bat_xlsx)

end_date  = time.strftime("%x %H:%M:%S")
with open(log_request ,'a') as log:
	log.write('Start Date_Time proc call-->'+start_date+'\n')
	log.write('End Date_Time to proc call-->'+end_date+'\n')






