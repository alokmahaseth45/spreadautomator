

import sys
# path = str(sys.argv[1])
import xlrd
import os
import codecs
import pdb
import requests
from lxml import html
import re
# import xlsxwriter
import pdb

import numpy as np
import pandas as pd
import pypyodbc
from sqlalchemy import create_engine

def Function_bat_run(bat):
	print bat
	bat = '""'+bat+'""'
	print bat
	os.system(bat)
	return "Successfully"

#engine = create_engine('mysql://username:password@host:port/database')
# engine = create_engine('mssql+pyodbc://sa:spot@99@127.0.0.1:1433/Sample100?driver=SQL Server')
engine = create_engine('mssql+pyodbc://sa:spot@99@127.0.0.1:1433/Annual_Reports_Raw?driver=SQL Server')

#engine = create_engine('mssql://localhost/1433?driver=SQL Server?trusted_connection=yes?Database=demo')
#exit()

# connection = pypyodbc.connect('Driver={SQL Server};'
# 								'Server=127.0.0.1,1433;'
# 								'Database=new_details;'
# 								'uid=sa;pwd=Alok@1234') 
# cursor = connection.cursor()
# import requesocks
# session = requesocks.session()
# session.proxies = {'http': 'socks5://127.0.0.1:9050',
# 					'https': 'socks5://127.0.0.1:9050'}

def Function_bat_run(bat):
	# print bat
	# bat = '""'+bat+'""'
	# print bat
	os.system(bat)
	return "Successfully"


table_name = 'Excel_To_Table_fe51978f-7e9c-454a-9441-4bcda8901402_Modi Naturals ar-2015-2016_54_0001_Sheet'

bat_text_profit_Bat =  'sqlcmd -E -S localhost -d Annual_Reports_Raw -Q'+' '+ '"Exec DeleleExistingTable'+' '+ "'"+table_name+ "'"+'"'
print "-------------------",bat_text_profit_Bat

# os.system(bat_text_profit_Bat)

# with open(grid_sql_file, "w") as text_file:
# 	text_file.write(str(bat_text_profit_Bat)+'\n')
Function_bat_run(bat_text_profit_Bat)

