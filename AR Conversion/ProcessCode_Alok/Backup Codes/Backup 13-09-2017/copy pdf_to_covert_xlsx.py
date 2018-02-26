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
import Pdf_Text_To_Sql
from Pdf_Text_To_Sql import Insert_To_Sql

from pyPdf import PdfFileWriter, PdfFileReader
# from pyPdf import PdfFileWriter, PdfFileReader

# from PyPDF2 import PdfFileMerger
# pdf = "D:\AR Conversion\Annual Reports\\admin\Pdf_Single_Files\\14db0fba-2827-4e96-a269-692be4c6a365_Attach P P OIL PRIVATE LIMITED 2016_1.pdf"
# print type(pdf)
# input1 = PdfFileReader(file(pdf, "rb"))
# print "1st done"


def copy_to_omni(pdf_name_single,omni_filesave):

	print "pdf_name_single : ",pdf_name_single

	shutil.copyfile(pdf_name_single,omni_filesave)

	return

def copy_xlsx_to_main_path(pdf_xlsx_omni,pdf_xlsx):

	shutil.copyfile(pdf_xlsx_omni,pdf_xlsx)

	return 


def break_pdf_page(pdf_link):
	try:
		print "pdf lins is : ",pdf_link


		inputpdf = PdfFileReader(open(pdf_link, "rb"))
		# merger = PdfFileMerger()
		print "No of page in pdf : ",inputpdf.numPages
		total_page = inputpdf.numPages
		print type(total_page)
		# pdb.set_trace()

		pdf_folder = pdf_link.split('\\')
		pdf_name = pdf_folder[-1]
		print "pdf name is : ",pdf_name
		# pdb.set_trace()
		pdf_single_filesave = pdf_link.replace(pdf_name,'')
		pdf_single_filesave = pdf_single_filesave+'Pdf_Single_Files/'
		print pdf_single_filesave
		# pdb.set_trace()
		if not os.path.exists(pdf_single_filesave):
			os.makedirs(pdf_single_filesave)
		print pdf_single_filesave
		

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
	print bat
	bat = '""'+bat+'""'
	print bat
	os.system(bat)
	# pdb.set_trace()
	
	return



	



page_break_error = 'D:\AR Conversion\Not_converted_single_pdf_files.txt'
html_move_problem = 'D:\AR Conversion\html_move_problem.txt'



pdf_paths = r'D:\Annual Reports\Requests'
pdf_links_list = []
for root, dirs, files in os.walk(pdf_paths):
	for file in files:
		if file.endswith("_New.txt"):
			# print(os.path.join(root, file))
			listpath1 = (os.path.join(root, file))
			# print listpath1
			pdf_links_list.append(listpath1)
		else:
			print "Waiting For New Request"

# pdf_links_list = [x for x in pdf_links_list if "Pdf_Single_Files"  in x]

print pdf_links_list

# listpath = r'Z:\BSE India Annual Report\Convert HTML And EXEL\Input\pdflinkpath.txt'

omni_savedir = r'D:\BSE India Annual Report\ProcessCode 100\OmniWatch100'


for listpath in pdf_links_list:
	print listpath
	convert_error = 0
	listpath_done = listpath.replace('_New','_Done')
	with open(listpath) as f:
		inputrow = f.readlines()
	f.close()
	print inputrow
	inputrow = [x.replace('\n','') for x in inputrow]
	print inputrow

	request = listpath.split('\\')
	Request_id = request[-1].replace('_New.txt','')
	Request_id = Request_id.strip()
	print "Request Id Is : ",Request_id
	# pdb.set_trace()

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



	# pdf_path = pdf_dir.replace("\\", "/")+'/'+ pdf_name
	pdf_path = pdf_dir+'\\'+ pdf_name


	if not os.path.isfile(pdf_path):
		if not os.path.exists(pdf_dir):
			os.makedirs(pdf_dir)

		shutil.copy(pdf_upload_path,pdf_dir)
		time.sleep(1)
	else:
		print "PDF is aready exist in BSE Folder"

	print "Pdf BSE Path Is : ",pdf_path
	# pdb.set_trace()


	CompanyID_Value = inputrow[4]
	CompanyID = CompanyID_Value.split('::')
	CompanyID = CompanyID[1].strip()
	print "Pdf Path Is : ",CompanyID

	

	# bs_pl_value = inputrow[5]
	# bs_pl_page=bs_pl_value.split('::')
	# bs_pl_page = bs_pl_page[1].strip()
	# print "Bs/Pl Page No is : ",bs_pl_page

	return_output = break_pdf_page(pdf_path)
	print return_output

	if "Page not break"  in return_output:
		print "Page not breaked"
		break
	else:
		pdf_single_filesave = return_output
		print pdf_single_filesave
		pdf_name_without_extention = pdf_name.replace('.pdf','')
		print pdf_name_without_extention

		#-------- Start To Get Single Pdf Files   -----------
		pdf_files = glob.glob(pdf_single_filesave+'/*'+'.pdf')
		# print "pdf files is : ",pdf_files
		pdf_files = [x for x in pdf_files if pdf_name_without_extention in x]
		# print pdf_files.sort()
		print "pdf files is : ",pdf_files
		#-------- End To Get Single Pdf Files   -----------

		# exit()


		print type(pdf_files)
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


		# time.sleep(5)

		bat_xlsx = 'D:\AR Conversion\ProcessCode_Alok\Request Id Batch/'+str(Request_id)+'.bat'

		

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
				# if os.path.isfile(omni_pdf_filesave) and os.path.isfile(pdf_xlsx_omni) and os.path.isfile(pdf_txt_omni) and os.path.isfile(omni_htm_filesave) and os.path.isfile(extra_omni_htm):
				# if os.path.isfile(omni_pdf_filesave) and os.path.isfile(pdf_xlsx_omni) and os.path.isfile(pdf_xlsx_main_omni) and os.path.isfile(pdf_txt_omni) and os.path.isfile(extra_omni_htm):
				if os.path.isfile(omni_pdf_filesave) and os.path.isfile(pdf_xlsx_omni) and os.path.isfile(pdf_txt_omni) and os.path.isfile(extra_omni_htm):


					if not os.path.exists(xlsx_dir):
						os.makedirs(xlsx_dir)

					#-------- Move Excel And Text Files to Main And Converted Folder ----------
					
					# shutil.move(pdf_xlsx_omni,pdf_xlsx)
					shutil.move(pdf_xlsx_omni,xlsx_filesave)
					try:
						shutil.move(pdf_xlsx_main_omni,xlsx_filesave_main)
					except:
						pass
					shutil.move(pdf_txt_omni,pdf_txt)
					try:
						shutil.move(omni_htm_filesave,htm_filesave)
					except:
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


					##----------------- Start To Append Excel File Path To VB script Bat file----------------------
					xlsx_bat =  'call '+'"D:\AR Conversion\ProcessCode_Alok\Open Excel And Read Data\open_And_Read_Excel_Omni.py"'+' '+'"'+xlsx_filesave+'"'
					with open(bat_xlsx, "a") as text_file:
						text_file.write(str(xlsx_bat)+'\n')

					##----------------- End To Append Excel File Path To VB script Bat file----------------------

					

					print "File moved to original folder"
					count_waiting = 0
					main_flag = 0
				else:
					print "waiting for Text and Excel"
					time.sleep(30)
					count_waiting = count_waiting+1
					if count_waiting >30:
						count_waiting = 0
						count_waiting1 = count_waiting1+1
						if count_waiting1>5:
							main_flag = 0
							converted_flag = 1

		
		#----------------- Start To Insert Data Into MYSQL Database----------------------
		try:
			Insert_To_Sql(pdf_files,company,Request_id)
			convert_error =1
		except Exception,e:
			print "Error in inserting to sql",str(e)

		#----------------- End To Insert Data Into MYSQL Database----------------------


		time.sleep(5)

		if converted_flag == 1:
			listpath_converting = listpath.replace('_New','_Error')
		else:
			listpath_converting = listpath.replace('_New','_Converted')

		if convert_error == 1:
			os.rename(listpath,listpath_converting)

		if os.path.isfile(bat_xlsx):
			Function_bat_run(bat_xlsx)



		bat_filesave = 'D:\AR Conversion\Request_ID/'+str(Request_id)+'.bat'

		# sqlcmd -E -S localhost -d Annual_Reports -Q "Exec Annual_Reports.dbo.Update_OverviewNewSite_OnClick 'U24236MH1987PTC044813'">

		bat_text =  'sqlcmd -E -S localhost -d Annual_Reports -Q'+' '+ '"Exec Annual_Reports.dbo.SPV_AR_Process_1'+' '+ "'"+Request_id+ "'"+'"'
		with open(bat_filesave, "w") as text_file:
			text_file.write(str(bat_text)+'\n')

		# bat_text =  'sqlcmd -E -S localhost -d Annual_Reports_Raw -Q'+' '+ '"Exec Annual_Reports_Raw.dbo.read_text_files'+' '+ "'"+Request_id+ "'"+'"'
		# with open(bat_filesave, "a") as text_file:
		# 	text_file.write(str(bat_text)+'\n')

		# bat_text =  'sqlcmd -E -S localhost -d Annual_Reports_Raw -Q'+' '+ '"Exec Annual_Reports_Raw.dbo.arinput'+' '+ "'"+Request_id+ "'"+'"'
		# with open(bat_filesave, "a") as text_file:
		# 	text_file.write(str(bat_text)+'\n')
		# # print bat_filesave

		# bat_text =  'sqlcmd -E -S localhost -d Annual_Reports -Q'+' '+ '"Exec Annual_Reports.dbo.proc_Report_process'+' '+ "'"+Request_id+ "'"+'"'
		# with open(bat_filesave, "a") as text_file:
		# 	text_file.write(str(bat_text)+'\n')

		if os.path.isfile(bat_filesave):
			Function_bat_run(bat_filesave)

	

	




















