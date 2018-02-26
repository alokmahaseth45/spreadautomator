import sys
import os
import requests
import re
import csv
import requesocks
import time
import datetime
import random
import datetime
import pdb
# from inclu import *
from lxml import html
import codecs
import shutil
from shutil import copyfile
import fnmatch, os
import glob
from os import listdir


# print change_text
# pdb.set_trace()

# session = requesocks.session()
# session.proxies = {'http': 'socks5://127.0.0.1:9050',
#                    'https': 'socks5://127.0.0.1:9050'}
session = requests.Session()

mypath = r'D:\AR Conversion\ProcessCode_Alok\Adobe Conversion Plugins Bat\Adobe conversion new bat files'


def Function_bat_run(bat):
	try:
		print bat
		bat = '""'+bat+'""'
		print bat
		os.system(bat)
		# pdb.set_trace()
		text = "Sucess"
	except:
		text = 'Error'
	return text	


finance_new_file_path = 'D:\AR Conversion\ProcessCode_Alok\Adobe Conversion Plugins Bat\Adobe conversion new bat files'
Finance_batch = []
for root, dirs, files in os.walk(finance_new_file_path):
	for file in files:
		if file.endswith("_adobe.bat"):
			# print(os.path.join(root, file))
			listpath1 = (os.path.join(root, file))
			text = Function_bat_run(listpath1)
			if "Sucess" in text:
				listpath1_done = listpath1.replace('_adobe.bat','_done.bat')
				try:
					os.rename(listpath1,listpath1_done)
				except:
					if os.path.isfile(listpath1_done):
						os.remove(listpath1_done)
						os.rename(listpath1,listpath1_done)

			if 'Error' in text:
				listpath1_done = listpath1.replace('_adobe.bat','_error.bat')
				try:
					os.rename(listpath1,listpath1_done)
				except:
					if os.path.isfile(listpath1_done):
						os.remove(listpath1_done)
						os.rename(listpath1,listpath1_done)
				# os.rename(listpath1,listpath1_done)






			# print listpath1
			# Finance_batch.append(listpath1)
			# break
# print Finance_batch
# Finance_batch_new9 = Finance_batch

