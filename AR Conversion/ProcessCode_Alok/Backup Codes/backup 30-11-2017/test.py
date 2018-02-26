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
from datetime import date,timedelta,datetime

today = date.today() # or you can do today = date.today() for today's date
print today
time1 = time.strftime("%x %H:%M:%S")
print time1


# now = time.strftime("%c")
# ## date and time representation
# print "Current date & time " + time.strftime("%c")
 
# ## Only date representation
# print "Current date "  + time.strftime("%x")
 
# ## Only time representation
# print "Current time " + time.strftime("%X")
 
# ## Display current date and time from now variable 
# print ("Current time %s"  % now )

# import Pdf_Text_To_Sql
# from Pdf_Text_To_Sql import Insert_To_Sql
# from pyPdf import PdfFileWriter, PdfFileReader

# def Check_Server_File_Count(server_list):
# 	server_list_count = []
# 	server_list_count_dict = {}
# 	# server_count = []
# 	# print server_list
# 	# for s in server_list:
# 	# 	# print glob.glob(s+'/*')
# 	# 	x = len(glob.glob(s+'/*'))
# 	# 	server_list_count.append(x)
# 	# print server_list_count
# 	# print min(server_list_count)
# 	# print server_list_count.index(min(server_list_count))
# 	# len(glob.glob('*'))

# 	for s in server_list:
# 		# print glob.glob(s+'/*')
# 		x = len(glob.glob(s+'/*'))	
# 		server_list_count.append(x)
# 		server_list_count_dict.update({s: x})
# 	print server_list_count_dict
# 	# print min(server_list_count_dict,key=server_list_count_dict.get)
# 	return min(server_list_count_dict,key=server_list_count_dict.get)
	

# server_txt_path = r"D:\BSE India Annual Report\ProcessCode 100\Omni Servers\use servers.txt"

# with open(server_txt_path, 'r') as read_server:
# 	server_name = read_server.readlines()
# server_name = ['D:\BSE India Annual Report\ProcessCode 100\Omni Servers\\'+x.replace('\n','') for x in server_name]


# check = Check_Server_File_Count(server_name)
# print "heck is :",check

# print server_name




