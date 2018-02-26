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
import Pdf_Text_To_Sql
from Pdf_Text_To_Sql import Insert_To_Sql
from pyPdf import PdfFileWriter, PdfFileReader
import pypyodbc


def Function_bat_run(bat):
	print bat
	bat = '""'+bat+'""'
	print bat
	os.system(bat)
	# pdb.set_trace()
	
	return

bat = "D:\AR Conversion\Request_ID/5000090317.bat"

Function_bat_run(bat)