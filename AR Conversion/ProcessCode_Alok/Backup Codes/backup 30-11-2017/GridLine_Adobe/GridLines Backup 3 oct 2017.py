from PIL import Image
import sys
import os


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
	print 'image read complete'

	import numpy as np
	import pandas as pd
	import pypyodbc
	from sqlalchemy import create_engine

	# engine = create_engine('mssql+pyodbc://sa:2012@ABHINAV-8\ABHI2012/Pdf_Gridlines?driver=SQL Server')
	engine = create_engine('mssql+pyodbc://sa:spot@99@WIN-6M9N8542A8D/Pdf_Gridlines?driver=SQL Server')
	con = engine.connect()

	table_name_xy = pdf_name.split("\\")[-1].replace(".pdf","_xy")
	query = ""
	query += "If OBJECT_ID('dbo.["+table_name_xy+"]','U') IS NOT NULL Drop Table ["+table_name_xy+"]"+"\n"
	# print query
	print con.execute(query)

	query = ""
	# query += "Create Table ["+table_name_xy+"] (id int identity(1,1),[index] int"+"\n"
	query += "Create Table ["+table_name_xy+"] ([index] int"+"\n"

	col_headers = []
	for x in range(w):
		query += ",X_"+str(x)+" int"
		col_headers.append("X_"+str(x))
	query += ")"+"\n"

	# print col_headers
	# print query
	print con.execute(query),'Table Schema Created'

	# df = pd.DataFrame(temp, columns=col_headers)
	df = pd.DataFrame(temp)
	# print df
	print 'data frame created'
	# print df.values


	# df.to_sql(name = table_name_xy, con = engine, if_exists='append')
	# print 'sql table created'
	pdf_csv = pdf_name.replace(".pdf",".csv")
	df.to_csv(pdf_csv)
	print 'csv created'
	query = 'sqlcmd -E -S localhost -d Pdf_Gridlines -Q'+' '+ '"Exec bulk_insert '+"'"+pdf_csv+"','"+table_name_xy+"'"+'"'
	# query = 'sqlcmd -E -S ABHINAV-8\ABHI2012 -d Pdf_Gridlines -Q'+' '+ '"Exec bulk_insert '+"'"+pdf_csv+"','"+table_name_xy+"'"+'"'
	os.system(query)
	print 'SQL Table Created'
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

	from PyPDF2 import PdfFileWriter, PdfFileReader
	# from pyPdf import PdfFileWriter, PdfFileReader
	import StringIO
	from reportlab.pdfgen import canvas
	from reportlab.lib.pagesizes import letter

	# print 'letter',type(letter),letter
	existing_pdf = PdfFileReader(file(pdf_name, "rb"))
	page = existing_pdf.getPage(0)
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
	# can.setFont("Helvetica", 5)
	# can.setStrokeColorRGB(0,1,0)
	# can.line(15, 649, 570, 649)
	# can.drawString(600, 10, '|AA|')
	main_x_media_offset = 0
	main_y_media_offset = 0
	h=h*0.75

	for row in exist_path.values:
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
			can.line(x1+main_x_offset-3, h-y+main_y_offset-1, x2+main_x_offset+3, h-y+main_y_offset-1)
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


	if os.path.isfile(pdf_converted):
		return pdf_converted

	# except:
	# 	return "xxxxxxxxxx"


