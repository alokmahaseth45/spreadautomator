from PIL import Image
import sys
import os
import datetime

# Cin = str(sys.argv[1])
# Cin_Name = str(sys.argv[2])
# Server_Name = str(sys.argv[3])
# pdf_name = str(sys.argv[1])
# pdf_name = r"C:\Users\john\Desktop\Resize_Pdf_Dpi\Gridline_ahmedabad_cause_list_1.pdf"
# png_name = pdf_name.replace('.pdf','.png')
# pdf_converted = pdf_name.replace('.pdf','_converted.pdf')

def Convert_png_and_pdf(pdf_name,reverse):
	# pdf_name = str(sys.argv[1])
	png_name = pdf_name.replace(".pdf",".png")
	pdf_converted = pdf_name.replace(".pdf","_GridLine.pdf")

	test_flag = 0

	from PIL import Image

	print 'image read start',datetime.datetime.now()
	im = Image.open(png_name)
	im = im.convert("L")
	im2 = Image.new("L",im.size,255)

	w = im.size[0]
	h = im.size[1]
	print w,h
	temp = [[[] for i in range(w)] for i in range(h)]

	for y in range(h):
		for x in range(w):
			temp[y][x] = im.getpixel((x,y))
	print 'image read complete',datetime.datetime.now()

	def check_for_notLine(x,y,pxl,w,h):
		cntt=0
		last_x=x+3
		last_y=y+3
		if last_x>w:
			last_x=w
		if last_y>h:
			last_y=h
		check_x=x+13
		if check_x>w:
			check_x=w	
		for xx in range(x,check_x):	
			if shade_temp[xx][y]<255 and (shade_temp[xx][y]==pxl or (shade_temp[xx][y]>pxl-5 and shade_temp[xx][y]<pxl+5)) :
				pass
			else:
				return False
				break			
		for xx in range(x,last_x):
			for yy in range(y,last_y):	
				if shade_temp[xx][yy]<255 and (shade_temp[xx][yy]==pxl or (shade_temp[xx][yy]>pxl-5 and shade_temp[xx][yy]<pxl+5)):
					cntt+=1
				else:
					return False	
		if cntt==9:
			return True
		else:
			return False	 	

	def remove_shade(x,y,w,h):
		colr=shade_temp[x][y]
		#print colr
		last_x=0
		last_y=0
		for xx in range(x,x+(w-x)):
			if shade_temp[xx][y]!=colr:
				last_x=xx
				break
		for yy in range(y,y+(h-y)):
			if shade_temp[x][yy]!=colr:
				last_y=yy
				break
		#color_list= im2.getcolors(im2.size[0]*im2.size[1])
		for xx in range(x,last_x):
			for yy in range(y,last_y):	
				if (shade_temp[xx][yy]>170 and shade_temp[xx][yy]!=colr) :
					shade_temp[xx][yy]=0
				#or (shade_temp[xx][yy]>colr-5 and shade_temp[xx][yy]<colr+5)
				elif shade_temp[xx][yy]==colr or (shade_temp[xx][yy]>colr-5 and shade_temp[xx][yy]<colr+5):
					shade_temp[xx][yy]=255	
		# for xx in range(x,last_x):
		# 	for yy in range(y,last_y):	
		# 		if shade_temp[xx][yy]==colr:
		# 			shade_temp[xx][yy]=255
		return (x,y,last_x,last_y)		

	def call_shade_remove():
		#shade_dimen={}
		for x in range(w):
			for y in range(h):	
				if shade_temp[x][y]<255:
					c=check_for_notLine(x,y,shade_temp[x][y],w,h)
					if c is True:
						rs=remove_shade(x,y,w,h)
						#shade_dimen.update({rs:shade_temp[x][y]})	
						# print x,y
						# exit()


	from PyPDF2 import PdfFileWriter, PdfFileReader

	existing_pdf = PdfFileReader(file(pdf_name, "rb"))
	page = existing_pdf.getPage(0)

	page_content = page.extractText()
	# print page_content
	if "\n" in page_content:
		scanned_flag = 0
		print 'Scanned: No'
	else:
		scanned_flag = 1
		print 'Scanned: Yes'
	# exit()
	# scanned_flag = 1


	if scanned_flag == 0:
		global shade_temp
		shade_temp=[[[] for i in range(h)] for i in range(w)]
		for x in range(w):
			for y in range(h):	
				shade_temp[x][y]=temp[y][x]

		for x in range(w):
			shade_temp[x][h-1]=255
			shade_temp[x][0]=255
		for y in range(h):
			shade_temp[w-1][y]=255
			shade_temp[0][y]=255

		call_shade_remove()
		#print shade_dimen
		for x in range(w):
			for y in range(h):	
				temp[y][x]=shade_temp[x][y]
		print 'Shade Removed',datetime.datetime.now()

	for x in range(w):
		for y in range(h):
			im2.putpixel((x,y),temp[y][x])
	im2.save("Grey.png")
		

	import numpy as np
	import pandas as pd
	import pypyodbc
	from sqlalchemy import create_engine

	# engine = create_engine('mssql+pyodbc://sa:2012@ABHINAV-8\ABHI2012/Pdf_Gridlines?driver=SQL Server')
	engine = create_engine('mssql+pyodbc://sa:spot@99@WIN-6M9N8542A8D/Pdf_Gridlines?driver=SQL Server')
	con = engine.connect()
	df = pd.DataFrame(temp)
	# print df.ix[:,0:10]
	# exit()
	table_name_xy = pdf_name.split("\\")[-1].replace(".pdf","_xy")

	if reverse == 0:
		cols = 1000
		table_count = ((w-2)/cols)+1
		print 'cols:',cols,'table_count:',table_count

		for tb in range(1,table_count+1):
			t_num = '_'+str(tb)
			if tb == 1:
				t_num = ''
			st = ((tb-1)*cols)+1
			ed = st + cols
			if st == 1:
				st = 0
			if ed > w:
				ed = w
			print tb,st,ed,t_num

			query = ""
			query += "If OBJECT_ID('dbo.["+table_name_xy+t_num+"]','U') IS NOT NULL Drop Table ["+table_name_xy+t_num+"]"+"\n"
			print query
			print con.execute(query)

			query = ""
			# query += "Create Table ["+table_name_xy+"] (id int identity(1,1),[index] int"+"\n"
			query += "Create Table ["+table_name_xy+t_num+"] ([index] int"+"\n"

			col_headers = []
			for x in range(st,ed):
				query += ",X_"+str(x)+" int"
				col_headers.append("X_"+str(x))
			query += ")"+"\n"

			# print col_headers
			# print query
			print con.execute(query),'Table Schema Created',datetime.datetime.now()

			# df = pd.DataFrame(temp, columns=col_headers)
			if tb == table_count:
				df_n = df.ix[:,st:ed]
			else:
				df_n = df.ix[:,st:ed-1]
			# print df_n
			# exit()
			print 'data frame created',datetime.datetime.now()
			# print df.values


			# df.to_sql(name = table_name_xy, con = engine, if_exists='append')
			# print 'sql table created'
			pdf_csv = pdf_name.replace(".pdf",t_num+".csv")
			df_n.to_csv(pdf_csv)
			print 'csv created',datetime.datetime.now()
			query = 'sqlcmd -E -S localhost -d Pdf_Gridlines -Q'+' '+ '"Exec bulk_insert '+"'"+pdf_csv+"','"+table_name_xy+t_num+"'"+'"'
			# query = 'sqlcmd -E -S ABHINAV-8\ABHI2012 -d Pdf_Gridlines -Q'+' '+ '"Exec bulk_insert '+"'"+pdf_csv+"','"+table_name_xy+t_num+"'"+'"'
			os.system(query)
			print 'SQL Table Created',datetime.datetime.now()
		# exit()


		# query = "EXEC draw_grid_lines_NoPrint '" + table_name_xy + "'"
		# query =  'sqlcmd -E -S ABHINAV-8\ABHI2012 -d Pdf_Gridlines -Q'+' '+ '"Exec draw_grid_lines_NoPrint '+"'"+table_name_xy+"'"+'"'
		query =  'sqlcmd -E -S localhost -d Pdf_Gridlines -Q'+' '+ '"Exec draw_grid_lines_NoPrint '+"'"+table_name_xy+"'"+'"'
		os.system(query)

	# con = engine.connect()
	query = "EXEC Get_grid_lines '" + table_name_xy + "'"
	# print "Query Is :",query
	# # exist_path = pd.read_sql_query(query, con=engine)
	exist_path = pd.read_sql_query(query, con=engine, index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None)
	print 'received output'
	if test_flag == 1:
		print exist_path

	# from PyPDF2 import PdfFileWriter, PdfFileReader
	# from pyPdf import PdfFileWriter, PdfFileReader
	import StringIO
	from reportlab.pdfgen import canvas
	from reportlab.lib.pagesizes import letter

	def draw_letters(x,y,width,line_id):
		print line_id,x,y,width
		can.setLineWidth(0.8)
		r = float(width)/10*0.75
		x_len = float(7) * r
		y_len = float(10) * r
		line_id = str(line_id)
		num_list = ['F','H','I','K','L','N','T','V','X','Z']
		# 			 0   1   2   3   4   5   6   7   8   9
		x = float(x)
		y = float(y)
		print x_len,y_len

		for n in range(len(line_id)):
			pos = float(n) * y_len
			num_write = int(line_id[n:n+1])
			char_write = num_list[num_write]
			print n,num_write,char_write

			if char_write == 'T':
				can.line(pos+x, y+y_len, pos+x+x_len, y+y_len)
				can.line(pos+x+x_len/2, y+y_len, pos+x+x_len/2, y)
			if char_write == 'I':
				can.line(pos+x, y+y_len, pos+x+x_len, y+y_len)
				can.line(pos+x+x_len/2, y+y_len, pos+x+x_len/2, y)
				can.line(pos+x, y, pos+x+x_len, y)
			if char_write == 'F':
				can.line(pos+x, y+y_len, pos+x, y)
				can.line(pos+x, y+y_len, pos+x+x_len*2/3, y+y_len)
				can.line(pos+x, y+y_len/2, pos+x+x_len/2, y+y_len/2)
			if char_write == 'H':
				can.line(pos+x, y+y_len, pos+x, y)
				can.line(pos+x+x_len, y+y_len, pos+x+x_len, y)
				can.line(pos+x, y+y_len/2, pos+x+x_len, y+y_len/2)
			if char_write == 'K':
				can.line(pos+x, y+y_len, pos+x, y)
				can.line(pos+x, y+y_len/2, pos+x+x_len, y+y_len)
				can.line(pos+x, y+y_len/2, pos+x+x_len, y)
			if char_write == 'L':
				can.line(pos+x, y+y_len, pos+x, y)
				can.line(pos+x, y, pos+x+x_len, y)
			if char_write == 'N':
				can.line(pos+x, y+y_len, pos+x, y)
				can.line(pos+x+x_len, y+y_len, pos+x+x_len, y)
				can.line(pos+x, y+y_len, pos+x+x_len, y)
			if char_write == 'V':
				can.line(pos+x, y+y_len, pos+x+x_len/2, y)
				can.line(pos+x+x_len, y+y_len, pos+x+x_len/2, y)
			if char_write == 'X':
				can.line(pos+x, y+y_len, pos+x+x_len, y)
				can.line(pos+x+x_len, y+y_len, pos+x, y)
			if char_write == 'Z':
				can.line(pos+x, y+y_len, pos+x+x_len, y+y_len)
				can.line(pos+x+x_len, y+y_len, pos+x, y)
				can.line(pos+x, y, pos+x+x_len, y)


	if reverse == 1:
		print 'Reverse: Yes'
		if scanned_flag == 0:
			scanned_flag = 1
		else:
			scanned_flag = 0

	main_x = float(page.cropBox.getUpperRight_x())
	main_y = float(page.cropBox.getUpperRight_y())
	main_x_offset = float(page.cropBox.getLowerLeft_x())
	main_y_offset = float(page.cropBox.getLowerLeft_y())
	main_x_media_offset = float(page.mediaBox.getLowerLeft_x())
	main_y_media_offset = float(page.mediaBox.getLowerLeft_y())
	print 'existing_pdf',page.mediaBox,page.trimBox,page.cropBox

	packet = StringIO.StringIO()
	# create a new PDF with Reportlab
	# can = canvas.Canvas(packet, pagesize=letter)
	can = canvas.Canvas(packet, pagesize=(main_x-main_x_offset, main_y-main_y_offset))
	# line = "___________________________________________________________________________________"
	# can.drawString(11, 731, line)
	can.setLineWidth(0.5)
	# can.setFillColorRGB(0.6,0.6,0.6)

	# from reportlab.pdfbase import pdfmetrics
	# from reportlab.pdfbase.ttfonts import TTFont
	# pdfmetrics.registerFont(TTFont('CurlyHogRunes-Bold','CurlyHogRunes-Bold.ttf'))

	# can.setFont("Times-Bold", 10)
	# print can.getAvailableFonts()
	# can.setStrokeColorRGB(0.8,0.8,0.8)    # 1 1 1 is white
	can.setStrokeColorRGB(0.6,0.6,0.6)    # 1 1 1 is white
	# can.setStrokeColorRGB(0,0,0)    # 1 1 1 is white
	# can.line(15, 649, 570, 649)
	# can.drawString(600, 10, '|AA|')
	main_x_media_offset = 0
	main_y_media_offset = 0
	h=h*0.75

	for row in exist_path.values:
		can.setLineWidth(0.6)
		if row[0] == 'Y':
			x_write = row[1]
			x = row[1]*0.75
			y1 = row[2]*0.75
			y2 = row[3]*0.75
			can.line(x+main_x_offset, h-y2+main_y_offset-2, x+main_x_offset, h-y1+main_y_offset)
			# can.drawString(x+main_x_offset, h-y2+main_y_offset-1, str(x_write))
		elif row[0] == 'X':
			y_write = row[1]
			y = row[1]*0.75
			x1 = row[2]*0.75
			x2 = row[3]*0.75
			width = row[6] - 1
			if width > 12:
				width = 12
			line_id = int(row[7])
			can.line(x1-24.75+main_x_offset, h-y+main_y_offset-1, x2+main_x_offset+3, h-y+main_y_offset-1)
			if scanned_flag == 0:
				can.setFont("Helvetica", (width-1)*0.75)
				can.drawString(x1-15+main_x_offset, h-y+main_y_offset+0.75, str(line_id))
			else:
				draw_letters(x1-23.25+main_x_offset, h-y+main_y_offset+0.75, width-3, line_id)

			# can.line(x1+main_x_offset-3, h-y+main_y_offset-1, x2+main_x_offset+3, h-y+main_y_offset-1)
			# can.drawString(x1-11+main_x_offset, h-y+main_y_offset, str(y_write))

	# for x in line_dict.keys():
	# 	for current_line in line_dict[x]:
	# 		can.line(x+main_x_offset+main_x_media_offset, h-max(current_line)+main_y_offset+main_y_media_offset, x+main_x_offset+main_x_media_offset, h-min(current_line)+main_y_offset+main_y_media_offset)
	# 		# can.line(x+(main_x-main_x_offset-w)/2+main_x_offset, h-max(current_line)+((main_y-main_y_offset-h)/2)+main_y_offset-1, x+(main_x-main_x_offset-w)/2+main_x_offset, h-min(current_line)+((main_y-main_y_offset-h)/2)+main_y_offset-1)
	# 		# can.line(x+(main_x-w)/2, h-max(current_line)+((main_y-h)/2), x+(main_x-w)/2, h-min(current_line)+((main_y-h)/2))
	# 		# can.line(x, h-max(current_line), x, h-min(current_line))
	# 	if line_dict[x]:
	# 		can.drawString(x+main_x_offset, h-50, str(x))

	# for x in range(0,w,25):
	# 	can.drawString(x+main_x_offset, h-70, "."+str(x))

	# for c in x_line_list:
	# 	can.line(0+main_x_offset+main_x_media_offset, h-c+main_y_offset+main_y_media_offset, w+main_x_offset+main_x_media_offset, h-c+main_y_offset+main_y_media_offset)
	# 	# can.line((main_x-main_x_offset-w)/2+main_x_offset, h-c+((main_y-main_y_offset-h)/2)+main_y_offset-1, w+(main_x-main_x_offset-w)/2+main_x_offset, h-c+((main_y-main_y_offset-h)/2)+main_y_offset-1)
	# 	# can.line((main_x-w)/2, h-c+((main_y-h)/2)-1, w+(main_x-w)/2, h-c+((main_y-h)/2)-1)
	# 	# can.line(0, h-c, w, h-c)
	# 	can.drawString(10+main_x_offset, h-c+main_y_offset, str(c))

	can.save()

	#move to the beginning of the StringIO buffer
	packet.seek(0)
	new_pdf = PdfFileReader(packet)
	# for testing only
	# if test_flag == 1:
	# 	page_new = new_pdf.getPage(0)
	# 	print 'Only_Lines',page_new.mediaBox,page_new.trimBox
	# 	output_new = PdfFileWriter()
	# 	output_new.addPage(page_new)
	# 	Pdf_Only_Lines = pdf_name.replace(".pdf","_Only_Lines.pdf")
	# 	output_new.write(file(Pdf_Only_Lines, "wb"))



	# read your existing PDF
	# existing_pdf = PdfFileReader(file(pdf_name, "rb"))
	output = PdfFileWriter()
	# add the "watermark" (which is the new pdf) on the existing page
	# page = existing_pdf.getPage(0)
	# print page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y()
	page.mergePage(new_pdf.getPage(0))
	output.addPage(page)
	# finally, write "output" to a real file
	outputStream = file(pdf_converted, "wb")
	output.write(outputStream)
	outputStream.close()

	print 'gridline function complete',datetime.datetime.now()
	if os.path.isfile(pdf_converted):
		return pdf_converted

	# except:
	# 	return "xxxxxxxxxx"


