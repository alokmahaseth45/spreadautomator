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
# import shutil
import pypyodbc
# from shutil import copyfile

# from pyPdf import PdfFileWriter, PdfFileReader
# from PyPDF2 import PdfFileMerger


# connection = pypyodbc.connect('Driver={SQL Server};'
#                                 'Server=127.0.0.1,1433;'
#                                 'Database=new_details;'
#                                 'uid=sa;pwd=Alok@1234') 

# cursor = connection.cursor()

connection = pypyodbc.connect(
    r'Driver={SQL Server};' +
    r'Server=127.0.0.1,1433;' +
    r'Database=Annual_Reports;' +
    r'Trusted_Connection=Yes;')  

cursor = connection.cursor() 





def Insert_To_Sql(pdf_links_list,company,Request_id):


	pdf_links_list = [x for x in pdf_links_list if "Pdf_Single_Files"  in x]

	print pdf_links_list

	for pdf_link in pdf_links_list:
		# pdb.set_trace()
		# print x

		# pdf = r'D:\BSE India Annual Report\BSE Annual Data_A\500002_ABB\Pdf_Single_Files\5000021210_10.txt'

		pdf_text = pdf_link.replace('.pdf','_0001.txt')
		# pdf_text = pdf_link.replace('.pdf','_0001.txt')
		pdf_text = pdf_text.replace('Annual Reports','Annual Reports Converted Omni')

		if os.path.isfile(pdf_link) and os.path.isfile(pdf_text):
			# pdb.set_trace()


			print pdf_link
			print pdf_text
			id_code = pdf_text.split('\\')
			page_no = id_code[-1].replace('_0001','')
			# print id_code[-3]
			# unique = id_code[-3]
			page_no = page_no.replace('.txt','')
			print "Page No Is : ",page_no

			
			

			# break_id = id_code.split('_')
			# print break_id
			# company_Id = break_id[0]
			# company_code= break_id[1]

			# company_Id = unique
			# company_code = unique
			# Unique_Id = unique

			company_Id = Request_id
			company_code = Request_id
			Unique_Id = Request_id
			print company_Id
			print company_code
			# exit()
			# pdb.set_trace()



			with open(pdf_text) as f:
				# f = f.decode("utf-8")
			    inputrow = f.readlines()
			f.close()
			# print "--------",inputrow

			# content  = inputrow

			inputrow = [x.replace('\x00','').replace('\xff','').replace('\r','').replace('\xfe','').replace('\n','').replace('\t',' ') for x in inputrow]
			# print "--------",inputrow
			content = "\n".join(inputrow)
			content = str(content)
			# print content
			# pdb.set_trace()
			# print type(content)
			# content = "".join(inputrow)
			content_len = len(content)
			# print type(content)
			print content_len
			print "-------------",content
			# print "--------",inputrow
			# exit()
			Company = company
			Is_Convert = None 
			# Company = None 
			Type = None 
			PageNo = None 
			keyWord = None 
			AsskeyWord = None 
			NewSinglePage = None 
			CreateDate = None 
			readflag = None 
			Report_type = None 
			# cursor.execute("INSERT INTO dbo.BSE_India_Text_Data (Company_ID, Company_Code,Pdf_Path,Pdf_Page_No,Text_Path,Text_Content,Content_Length,Is_Convert,Company,Type,PageNo,keyWord,AsskeyWord,NewSinglePage,CreateDate,readflag,Report_type,Unique_Id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (company_Id,company_code,pdf_link,page_no,pdf_text,content,content_len,Is_Convert,Company,Type,PageNo,keyWord,AsskeyWord,NewSinglePage,CreateDate,readflag,Report_type,Unique_Id)) ###### Query execute data insert   #########
			# connection.commit()

			cursor.execute("INSERT INTO dbo.Annual_Report_Text (RequestID,Pdf_Path,Pdf_Page_No,Text_Path,Text_Content,Content_Length) VALUES (?, ?,?,?,?,?)", (company_Id,pdf_link,page_no,pdf_text,content,content_len)) ###### Query execute data insert   #########
			connection.commit()

			# exit()




	


