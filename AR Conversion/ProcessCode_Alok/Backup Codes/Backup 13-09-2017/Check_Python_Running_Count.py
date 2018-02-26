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
import codecs
import shutil
from shutil import copyfile
from lxml import html
import psutil


def Function_bat_run(bat):
	print bat
	bat = '""'+bat+'""'
	print bat
	os.system(bat)
	# pdb.set_trace()
	
	return

max_process = 3
max_process_gridline = 3

# process_count = sum(1 for proc in psutil.process_iter() if 'Server_Check_Pdf_Conversion_omni.py' in proc.cmdline())
# print "process count is : ",process_count

check_command = 0
check_command_gridline = 0
for proc in psutil.process_iter():
	if 'python.exe' in proc.name():
		pid = proc.pid
		if "Server_Check_Pdf_Conversion_omni.py" in str(proc.cmdline()):
			print proc.cmdline()
			check_command = check_command+1

		if "Abode_Gridline_To_Pdf.py" in str(proc.cmdline()) or "Abode_Gridline_To_Pdf_Rerun.py" in str(proc.cmdline()):
			print proc.cmdline()
			check_command_gridline = check_command_gridline+1
print check_command
print check_command_gridline

counter = 0
# while check_command < max_process:
# 	bat = "D:\AR Conversion\ProcessCode_Alok\Server_Check_Pdf_Conversion_omni.bat"
# 	Function_bat_run(bat)

if check_command < max_process:
	bat = "D:\AR Conversion\ProcessCode_Alok\Server_Check_Pdf_Conversion_omni.bat"
	Function_bat_run(bat)

if check_command_gridline < max_process_gridline:
	bat = "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Gridline_call_bat_and_run.bat"
	Function_bat_run(bat)

# check_command = 0