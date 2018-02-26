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

omni_savedir = r"D:\Omni Servers\54.169.41.18"

listpath_new = r"D:\AR Conversion\ProcessCode_Alok\Request\External Omni Request\10178aed-ca82-44eb-ae4e-cc3c6c5c0725_Num1-1_Pending.txt"
listpath_Pending  = listpath_new
listpath_new = listpath_Pending.replace('_Pending.txt','_New.txt')

with open(listpath_Pending, 'r') as r:
	pdfinput = r.readlines()
pdfinput = [x.replace('\n','') for x in pdfinput ]


# listpath_Pending  = listpath_new
# listpath_new = listpath_Pending.replace('_Pending.txt','_New.txt')


# listpath_Pending  = listpath_new.replace('_New.txt','_Pending.txt')
# try:
# 	os.rename(listpath_new,listpath_Pending)
# except:
# 	os.remove(listpath_Pending)
# 	os.rename(listpath_new,listpath_Pending)

listpath = listpath_Pending
req_name = listpath.split('\\')
req = req_name[-1]
req_new = req.split('_')
print req_new
Request_id = req_new[0]
# Internal_process = req_new[1]+'_'+req_new[2]


# log_request = r'D:\AR Conversion\ProcessCode_Alok\Log\\'+Request_id+'_External.txt'
# call_log_bat = r'D:\AR Conversion\ProcessCode_Alok\Log\\log_request.bat'

# #------------------------ Start Log Files ---------------------------------#
# status = 'Start External Pixel conversion'
# Process_Head = 'Pixel Convert'
# Process_Name = 'Pixel Convert'
# Process_Time = '0'
# Current_Status = status
# Time_Stamp = str(start_date)
# # cal_end = end_date - start_date
# # Process_Time =  str(cal_end.total_seconds())
# # call_log(Request_id,status,call_log_bat)
# call_log_new(Request_id,Process_Type,Process_Head,Process_Name,Process_Time,Current_Status,Time_Stamp)
#------------------------ End Log Files ---------------------------------#



pdf_list = [x.replace('\n','') for x in pdfinput]

# bat_xlsx = listpath_new.replace('External Omni Request','External Process Sql Request')

# if os.path.isfile(bat_xlsx):
# 	os.remove(bat_xlsx)


# for pdf in pdf_list:
# 	varp = open(pdf, "rb")
# 	input1 = PdfFileReader(varp)
# 	# input1 = PdfFileReader(open(pdf, "rb"))
# 	input1.getPage(0).mediaBox
# 	pxcel_files  = list(input1.getPage(0).mediaBox)
	
# 	if int(pxcel_files[2])>2015 or int(pxcel_files[3])>2015:
# 		x =  float(1000/float(pxcel_files[3]))
# 		print x
# 		# print input1.getPage(0).scale(0.5, 0.5)
# 		print input1.getPage(0).scaleBy(.3)
# 		output = PdfFileWriter()
# 		print input1.getPage(0).mediaBox
# 		file_folder = pdf.split('\\')
# 		p_name  = file_folder[-1]
# 		omni_filesave= omni_savedir+'\\'+p_name
# 		output.addPage(input1.getPage(0))
# 		outDoc = open(omni_filesave, 'wb')
# 		output.write(outDoc)
# 		outDoc.close()
# 		# pdb.set_trace()

# 	else:
# 		try:
# 			shutil.copy(pdf,omni_savedir)
# 		except Exception,e:
# 			print "Error in copying file to Omni Folder",str(e)

# 	varp.close()

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

	s_omni_pdf_filesave = omni_pdf_filesave.replace('.pdf','_0001.pdf')

	print omni_pdf_filesave
	while main_flag ==1:
		# if (os.path.isfile(omni_pdf_filesave) and os.path.isfile(pdf_xlsx_omni)) and (os.path.isfile(pdf_txt_omni) and os.path.isfile(s_omni_pdf_filesave)):
		if (os.path.isfile(omni_pdf_filesave) and os.path.isfile(s_omni_pdf_filesave)) and (os.path.isfile(pdf_xlsx_omni) and os.path.isfile(pdf_txt_omni)):
			# if os.path.isfile(s_omni_pdf_filesave):
			
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

			s_omni_pdf_filesave = omni_pdf_filesave.replace('.pdf','_0001.pdf')

			# print pdf
			# print s_omni_pdf_filesave
			# pdb.set_trace()
			if os.path.isfile(s_omni_pdf_filesave):
				shutil.copy(s_omni_pdf_filesave,pdf)
			
				try:
					os.remove(s_omni_pdf_filesave)
				except:
					pass





			
			

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
