from PIL import Image
import sys
import os
import datetime
import cv2
import numpy as np
import time

# Cin = str(sys.argv[1])
# Cin_Name = str(sys.argv[2])
# Server_Name = str(sys.argv[3])
# pdf_name = str(sys.argv[1])
# pdf_name = r"C:\Users\john\Desktop\Resize_Pdf_Dpi\Gridline_ahmedabad_cause_list_1.pdf"
# png_name = pdf_name.replace('.pdf','.png')
# pdf_converted = pdf_name.replace('.pdf','_converted.pdf')

def Convert_png_and_pdf(pdf_name,page_type,reverse):
	# pdf_name = str(sys.argv[1])
	png_name = pdf_name.replace(".pdf",".png")
	pdf_converted = pdf_name.replace(".pdf","_GridLine.pdf")
	ocr_name = pdf_name.replace(".pdf","_OCR.pdf")

	print 'Gridline Python Start',datetime.datetime.now()

	test_flag = 0
	server_flag = 1
	reverse = str(reverse)
	print 'reverse',reverse
	run_procs = 1

	print 'image read start',datetime.datetime.now()

	img = cv2.imread(png_name)
	# if test_flag == 1:
	# 	cv2.imshow("img", img)
	h = img.shape[0]
	w = img.shape[1]
	print 'w',w,'h',h

	# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	# cv2.imshow("hsv", hsv)

	img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# remove shade
	dilated_img = cv2.dilate(img2gray, np.ones((3,3), np.uint8))
	diff_img = 255 - cv2.absdiff(img2gray, dilated_img)
	# cv2.imshow("diff_img", diff_img)

	ret, mask = cv2.threshold(diff_img, 200, 255, cv2.THRESH_BINARY_INV)
	if test_flag == 1:
		# cv2.imshow("mask", mask)
		cv2.imwrite('mask.png',mask)

	# outline = np.zeros(mask.shape, dtype = "uint8")
	# (_, cnts, _) = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	# cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:100]
	# # screenCnt = None
	# print len(cnts)

	# c = cnts[10]
	# cv2.drawContours(outline, [c], -1, 255, -1)
	# # for c in cnts:
	# # 	cv2.drawContours(outline, [c], -1, 255, -1)
	# cv2.imshow("outline", outline)


	# exist_lines = [['Axis','LineNum','St','End','Length']]
	exist_lines = []
	pdf_id = pdf_name.split("\\")[-1].replace(".pdf","")

	ret, mask2 = cv2.threshold(diff_img, 220, 255, cv2.THRESH_BINARY_INV)
	if test_flag == 1:
		cv2.imshow("mask2", mask2)

	closingy = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, np.ones((3,1),np.uint8))
	# cv2.imshow("closingy", closingy)
	erosion_y = cv2.erode(closingy,np.ones((20,1),np.uint8),iterations = 1)
	# cv2.imshow("erosion_y", erosion_y)
	dilation_y = cv2.dilate(erosion_y,np.ones((40,3),np.uint8),iterations = 1)
	# cv2.imshow("dilation_y", dilation_y)
	erosion_y2 = cv2.erode(dilation_y,np.ones((20,1),np.uint8),iterations = 1)
	# cv2.imshow("erosion_y2", erosion_y2)

	kernel_y = np.ones((15,1),np.uint8)
	erosion_y_exist = cv2.erode(mask2,kernel_y,iterations = 1)
	# cv2.imshow("erosion_y_exist", erosion_y_exist)
	dilation_y_exist = cv2.dilate(erosion_y_exist,kernel_y,iterations = 1)
	# cv2.imshow("dilation_y_exist", dilation_y_exist)

	# cv2.waitKey(0)
	# exit()

	counter = 0
	for ia in dilation_y_exist.T:
		if 255 in ia:
			n = len(ia)
			y = np.array(ia[1:] != ia[:-1])     # pairwise unequal (string safe)
			i = np.append(np.where(y), n - 1)   # must include last element posi -- start pos
			z = np.diff(np.append(-1, i))       # run lengths
			p = np.cumsum(np.append(0, z))[:-1] # positions  -- end pos
			# print counter,i,z,p

			color = -1
			if dilation_y_exist[i[0]][counter] == 255:
				color = 1
			for ct in range(len(i)):
				if color > 0:
					exist_lines.append(['Y',counter,p[ct],i[ct],z[ct],pdf_id])
				
				color = color * -1
			# print exist_lines
			# exit()
		counter += 1
	# exist_lines = np.array(exist_lines)
	# print exist_lines
	# exit()


	# closingx = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, np.ones((1,3),np.uint8))
	# # cv2.imshow("closingx", closingx)
	# erosion_x = cv2.erode(closingx,np.ones((1,20),np.uint8),iterations = 1)
	# # cv2.imshow("erosion_x", erosion_x)
	# dilation_x = cv2.dilate(erosion_x,np.ones((3,40),np.uint8),iterations = 1)
	# # cv2.imshow("dilation_x", dilation_x)
	# erosion_x2 = cv2.erode(dilation_x,np.ones((1,20),np.uint8),iterations = 1)
	# # cv2.imshow("erosion_x2", erosion_x2)

	kernel_x = np.ones((1,15),np.uint8)
	erosion_x_exist = cv2.erode(mask,kernel_x,iterations = 1)
	# cv2.imshow("erosion_x_exist", erosion_x_exist)
	dilation_x_exist = cv2.dilate(erosion_x_exist,kernel_x,iterations = 1)
	# cv2.imshow("dilation_x_exist", dilation_x_exist)

	erosion_x2 = dilation_x_exist

	# cv2.waitKey(0)
	# exit()

	# cv2.imwrite('dilation_x.png',dilation_x)
	# np.savetxt("dilation_x.csv", dilation_x, delimiter=",")
	# dilation_x_exist = cv2.dilate(erosion_x,kernel_x,iterations = 1)
	# cv2.imshow("dilation_x_exist", dilation_x_exist)

	# data = dilation_x[84]
	# print data
	# data = np.array([0, 47, 48, 49, 50, 97, 98, 99])
	# print np.split(data, np.where(np.diff(data) != 0)[0]+1)

	counter = 0
	for ia in dilation_x_exist:
		if 255 in ia:
			n = len(ia)
			y = np.array(ia[1:] != ia[:-1])     # pairwise unequal (string safe)
			i = np.append(np.where(y), n - 1)   # must include last element posi
			z = np.diff(np.append(-1, i))       # run lengths
			p = np.cumsum(np.append(0, z))[:-1] # positions
			# print counter,i,z,p

			color = -1
			if dilation_x_exist[counter][i[0]] == 255:
				color = 1
			for ct in range(len(i)):
				if color > 0:
					exist_lines.append(['X',counter,p[ct],i[ct],z[ct],pdf_id])
				
				color = color * -1
			# print exist_lines
			# exit()
		counter += 1
	exist_lines = np.array(exist_lines)
	# print exist_lines
	exist_lines_csv = pdf_name+"xxxx"
	exist_lines_csv = exist_lines_csv.replace(".pdfxxxx","_exist_lines.csv")
	np.savetxt(exist_lines_csv, exist_lines, delimiter=",", newline='\n', fmt='%s')
	print 'exist_lines_csv created',datetime.datetime.now()
	# exit()

	if run_procs == 1:
		if server_flag == 1:
			query = 'sqlcmd -E -S localhost -d Pdf_Gridlines -Q'+' '+ '"Exec Exist_XY_Lines_Insert '+"'"+exist_lines_csv+"','"+pdf_id+"'"+'"'
		else:
			query = 'sqlcmd -E -S ABHINAV-8\ABHI2012 -d Pdf_Gridlines -Q'+' '+ '"Exec Exist_XY_Lines_Insert '+"'"+exist_lines_csv+"','"+pdf_id+"'"+'"'
		os.system(query)
		print 'Existing X Y Lines Inserted',datetime.datetime.now(),pdf_name


	# stepsize = 
	# for data in dilation_x:
	# 	# print data
	# 	np.split(data, np.where(np.diff(data) != stepsize)[0]+1)


	# dilation = dilation_x + dilation_y
	dilation = cv2.bitwise_or(erosion_x2,erosion_y2)
	# np.savetxt("dilation.csv", dilation, delimiter=",")
	# if test_flag == 1:
	# 	cv2.imshow("dilation", dilation)
	# cv2.waitKey(0)
	# exit()

	mask_noline = cv2.bitwise_xor(cv2.bitwise_or(mask,dilation),dilation)
	if test_flag == 1:
		# cv2.imshow("mask_noline", mask_noline)
		cv2.imwrite('mask_noline.png',mask_noline)
		# print type(mask_noline)
		# print mask_noline

	nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(mask_noline, connectivity=8)
	# print centroids
	sizes = stats[1:, -1]; nb_components = nb_components - 1
	# print sizes
	min_size = 3
	#your answer image
	mask_noline2 = np.zeros((output.shape))
	#for every component in the image, you keep it only if it's above min_size
	for i in range(0, nb_components):
		if sizes[i] >= min_size:
			mask_noline2[output == i + 1] = 255
	if test_flag == 1:
		cv2.imshow("mask_noline2", mask_noline2)
	# cv2.waitKey(0)
	# exit()

	# print mask_noline.dtype
	mask_noline = mask_noline2.astype(mask_noline.dtype)
	# print mask_noline.dtype

	hist_x = cv2.reduce(mask_noline, 1, cv2.REDUCE_AVG, dtype=cv2.CV_32S)
	# print hist_x
	# hist_x[hist_x[:, 0] < 3, 0] = 0

	hist_x_list = []
	counter = 0
	for d in hist_x:
		# print type(d)
		# print counter,d,np.count_nonzero(mask_noline[counter])
		hist_x_list.append([counter,d[0],np.count_nonzero(mask_noline[counter]),pdf_id])
		# if counter == 153:
		# 	print mask_noline[counter]
		counter += 1
		# if counter > 6:
		# 	break
	# print hist_x[:, 0]
	hist_x_list = np.array(hist_x_list)
	# print hist_x_list

	hist_x_csv = pdf_name+"xxxx"
	hist_x_csv = hist_x_csv.replace(".pdfxxxx","_hist_x.csv")
	np.savetxt(hist_x_csv, hist_x_list, delimiter=",", newline='\n', fmt='%s')
	print 'hist_x_csv created',datetime.datetime.now()


	# hist_y = cv2.reduce(mask_noline, 0, cv2.REDUCE_AVG, dtype=cv2.CV_32S)
	# # hist_x[hist_x[:, 0] < 3, 0] = 0
	# # print hist_y

	# # print np.count_nonzero(mask_noline.T[160])
	# # exit()

	# hist_y_list = []
	# counter = 0
	# for d in hist_y[0]:
	# 	# print type(d),d
	# 	# exit()
	# 	# print counter,d,np.count_nonzero(mask_noline[counter])
	# 	hist_y_list.append([counter,d,np.count_nonzero(mask_noline.T[counter]),pdf_id])
	# 	# if counter == 153:
	# 	# 	print mask_noline[counter]
	# 	counter += 1
	# 	# if counter > 6:
	# 	# 	break
	# # print hist_x[:, 0]
	# hist_y_list = np.array(hist_y_list)
	# # print hist_x_list

	# hist_y_csv = pdf_name+"xxxx"
	# hist_y_csv = hist_y_csv.replace(".pdfxxxx","_hist_y.csv")
	# np.savetxt(hist_y_csv, hist_y_list, delimiter=",", newline='\n', fmt='%s')
	# print 'hist_y_csv created',datetime.datetime.now()

	if run_procs == 1:
		if server_flag == 1:
			query = 'sqlcmd -E -S localhost -d Pdf_Gridlines -Q'+' '+ '"Exec Histogram_X_Insert '+"'"+hist_x_csv+"','"+pdf_id+"'"+'"'
		else:
			query = 'sqlcmd -E -S ABHINAV-8\ABHI2012 -d Pdf_Gridlines -Q'+' '+ '"Exec Histogram_X_Insert '+"'"+hist_x_csv+"','"+pdf_id+"'"+'"'
		os.system(query)
		print 'Histogram X Inserted',datetime.datetime.now(),pdf_name

	# if server_flag == 1:
	# 	query = 'sqlcmd -E -S localhost -d Pdf_Gridlines -Q'+' '+ '"Exec Histogram_Y_Insert '+"'"+hist_y_csv+"','"+pdf_id+"'"+'"'
	# else:
	# 	query = 'sqlcmd -E -S ABHINAV-8\ABHI2012 -d Pdf_Gridlines -Q'+' '+ '"Exec Histogram_Y_Insert '+"'"+hist_y_csv+"','"+pdf_id+"'"+'"'
	# os.system(query)
	# print 'Histogram Y Inserted',datetime.datetime.now(),pdf_name


	if run_procs == 1:
		if server_flag == 1:
			query = 'sqlcmd -E -S localhost -d Pdf_Gridlines -Q'+' '+ '"Exec draw_grid_lines_V2 '+"'"+pdf_id+"',0"+'"'
		else:
			query = 'sqlcmd -E -S ABHINAV-8\ABHI2012 -d Pdf_Gridlines -Q'+' '+ '"Exec draw_grid_lines_V2 '+"'"+pdf_id+"',0"+'"'
		os.system(query)
		print 'Proc for X Completed',datetime.datetime.now(),pdf_name



	import pandas as pd
	import pypyodbc
	from sqlalchemy import create_engine

	if server_flag == 0:
		engine = create_engine('mssql+pyodbc://sa:2012@ABHINAV-8\ABHI2012/Pdf_Gridlines?driver=SQL Server')
	else:
		engine = create_engine('mssql+pyodbc://sa:spot@99@WIN-6M9N8542A8D/Pdf_Gridlines?driver=SQL Server')
	con = engine.connect()



	query = "EXEC Get_X_lines '" + pdf_id + "'"
	x_lines_sql = pd.read_sql_query(query, con=engine, index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None)
	# if test_flag == 1:
	# 	print type(x_lines_sql.values)
		# print x_lines_sql.values[:,[1]]
		# np.append(mask_noline, x_lines_sql.values[:,[1]], axis=1)

	mask_noline_with_line_num = mask_noline/255
	mask_noline_with_line_num = np.hstack((x_lines_sql.values[:,[1]], mask_noline_with_line_num))
	# mask_noline_with_line_num = mask_noline_with_line_num/255
	# print mask_noline_with_line_num
	# np.savetxt('group_by.csv', mask_noline_with_line_num, delimiter=",", newline='\n', fmt='%s')

	test_df = pd.DataFrame(mask_noline_with_line_num)
	# print test_df
	test_df = test_df.groupby([0]).sum().unstack()
	# test_df = test_df.groupby([0]).sum()
	# test_df.columns = ['A','B','C']
	# print type(test_df)
	# print test_df.columns
	# print type(test_df.values)
	# test_df.to_csv('group_by.csv')
	# print test_df.loc[test_df['C'] != 0]

	if not os.path.exists("D:/AR Conversion/CSV_Path"):
		os.makedirs("D:/AR Conversion/CSV_Path")

	# group_by_csv = pdf_name+"xxxx"
	# group_by_csv = "D:/AR Conversion/CSV_Path/" + group_by_csv.replace(".pdfxxxx","_group_by.csv")
	group_by_csv = "D:/AR Conversion/CSV_Path/" + pdf_id + "_group_by.csv"
	test_df.to_csv(group_by_csv)
	# np.savetxt(group_by_csv, group_by_csv, delimiter=",", newline='\n', fmt='%s')
	print 'group_by_csv created',datetime.datetime.now()

	# for j in test_df.values:
	# 	print j
	# c = (a < 3).astype(int)
	# hist_y2 = (test_df.values > 0).astype(np.uint8)
	# print hist_y2
	# exit()

	# possible_y_lines = []
	# counter = 0
	# for ia in hist_y2.T:
	# 	if 1 in ia:
	# 		n = len(ia)
	# 		y = np.array(ia[1:] != ia[:-1])     # pairwise unequal (string safe)
	# 		i = np.append(np.where(y), n - 1)   # must include last element posi -- start pos
	# 		z = np.diff(np.append(-1, i))       # run lengths
	# 		p = np.cumsum(np.append(0, z))[:-1] # positions  -- end pos
	# 		# print ia
	# 		# print counter,i,z,p

	# 		color = -1
	# 		if dilation_y_exist[i[0]][counter] == 255:
	# 			color = 1
	# 		for ct in range(len(i)):
	# 			if color < 0 and z[ct] > 20:
	# 				possible_y_lines.append(['Y',counter,p[ct],i[ct],z[ct],pdf_id])
				
	# 			color = color * -1
	# 		# print possible_y_lines
	# 		# exit()
	# 	counter += 1
	# possible_y_lines = np.array(possible_y_lines)
	# # print possible_y_lines
	# possible_y_lines_csv = pdf_name+"xxxx"
	# possible_y_lines_csv = possible_y_lines_csv.replace(".pdfxxxx","_possible_y.csv")
	# np.savetxt(possible_y_lines_csv, possible_y_lines, delimiter=",", newline='\n', fmt='%s')
	# print 'possible_y_lines_csv created',datetime.datetime.now()


	if test_flag == 1:
		cv2.waitKey(0)

	if run_procs == 1:
		if server_flag == 1:
			query = 'sqlcmd -E -S localhost -d Pdf_Gridlines -Q'+' '+ '"Exec draw_grid_lines_V2_Cols '+"'"+pdf_id+"',"+page_type+",0"+'"'
		else:
			query = 'sqlcmd -E -S ABHINAV-8\ABHI2012 -d Pdf_Gridlines -Q'+' '+ '"Exec draw_grid_lines_V2_Cols '+"'"+pdf_id+"',"+page_type+",0"+'"'
		os.system(query)
		print 'Proc for Cols Completed',datetime.datetime.now(),pdf_name

	# exit()


	from PyPDF2 import PdfFileWriter, PdfFileReader

	original_pdf = PdfFileReader(file(pdf_name, "rb"))
	page = original_pdf.getPage(0)

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

	if reverse == '1':
		print 'Reverse: Yes'
		if scanned_flag == 0:
			scanned_flag = 1
		else:
			scanned_flag = 0



	table_name_xy = pdf_name.split("\\")[-1].replace(".pdf","_xy")

	query = "EXEC Get_grid_lines '" + table_name_xy + "'"
	# print "Query Is :",query
	# # exist_path = pd.read_sql_query(query, con=engine)
	exist_path = pd.read_sql_query(query, con=engine, index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None)
	print 'received output'
	if test_flag == 1:
		print exist_path

	img_grid = cv2.bitwise_or(img2gray,cv2.bitwise_not(dilation))
	# cv2.imshow("img_grid", img_grid)
	# print img_grid

	flat_img = img_grid.flatten()
	# print flat_img
	counts = np.bincount(flat_img)
	# print counts
	color = np.argmax(counts[0:150])

	# color = 100
	# for row in exist_path.loc[exist_path['Axis'] == 'A'].values:
	# 	color = row[1]
	# 	print 'color',color
	# 	break
	# color = color * 0.6/150
	color = float(color)/255.0
	print 'line color',color
	if color > 0.6:
		color = 0.6

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

	f = file(ocr_name, "rb")
	existing_pdf = PdfFileReader(f)
	# f.close()

	# existing_pdf = PdfFileReader(file(ocr_name, "rb"))
	page = existing_pdf.getPage(0)

	main_x = float(page.cropBox.getUpperRight_x())
	main_y = float(page.cropBox.getUpperRight_y())
	main_x_offset = float(page.cropBox.getLowerLeft_x())
	main_y_offset = float(page.cropBox.getLowerLeft_y())
	# main_x_media_offset = float(page.mediaBox.getLowerLeft_x())
	# main_y_media_offset = float(page.mediaBox.getLowerLeft_y())
	print 'existing_pdf',page.mediaBox,page.trimBox,page.cropBox

	packet = StringIO.StringIO()
	# create a new PDF with Reportlab
	# can = canvas.Canvas(packet, pagesize=letter)
	can = canvas.Canvas(packet, pagesize=(main_x-main_x_offset, main_y-main_y_offset))
	# line = "___________________________________________________________________________________"
	# can.drawString(11, 731, line)
	# can.setLineWidth(0.8)
	# can.setFillColorRGB(0.6,0.6,0.6)

	# from reportlab.pdfbase import pdfmetrics
	# from reportlab.pdfbase.ttfonts import TTFont
	# pdfmetrics.registerFont(TTFont('CurlyHogRunes-Bold','CurlyHogRunes-Bold.ttf'))

	# can.setFont("Times-Bold", 10)
	# print can.getAvailableFonts()
	# can.setStrokeColorRGB(0.8,0.8,0.8)    # 1 1 1 is white
	# can.setStrokeColorRGB(0.6,0.6,0.6)    # 1 1 1 is white
	# can.setStrokeColorRGB(0,0,0)    # 1 1 1 is white
	can.setStrokeColorRGB(color,color,color)    # 1 1 1 is white
	# can.line(15, 649, 570, 649)
	# can.drawString(600, 10, '|AA|')
	# main_x_media_offset = 0
	# main_y_media_offset = 0
	h=h*0.75

	for row in exist_path.values:
		can.setLineWidth(0.9)
		if row[0] == 'Y':
			x_write = row[1]
			x = (row[1]-1)*0.75
			y1 = row[2]*0.75
			y2 = row[3]*0.75
			can.line(x+main_x_offset, h-y2+main_y_offset-1, x+main_x_offset, h-y1+main_y_offset)
			# if server_flag == 0:
			# 	can.drawString(x+main_x_offset, h-y2+main_y_offset-1, str(x_write))
		elif row[0] == 'X':
			y_write = row[1]
			y = row[1]*0.75
			x1 = (row[2]-1)*0.75
			x2 = (row[3]-1)*0.75
			width = row[6] - 1
			if width > 12:
				width = 12
			line_id = int(row[7])
			can.line(x1-18+main_x_offset, h-y+main_y_offset-1, x2+main_x_offset+3, h-y+main_y_offset-1)
			if scanned_flag == 0:
				can.setFont("Helvetica", (width-1)*0.75)
				can.drawString(x1-15+main_x_offset, h-y+main_y_offset+0.75, str(line_id))
			else:
				draw_letters(x1-15+main_x_offset, h-y+main_y_offset+0.75, width-3, line_id)

			# can.line(x1+main_x_offset-3, h-y+main_y_offset-1, x2+main_x_offset+3, h-y+main_y_offset-1)
			# if server_flag == 0:
			# 	can.drawString(x1-31+main_x_offset, h-y+main_y_offset, str(y_write))

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
	f.close()

	if server_flag == 1:
		if os.path.isfile(exist_lines_csv):
			os.remove(exist_lines_csv)
		if os.path.isfile(hist_x_csv):
			os.remove(hist_x_csv)
		if os.path.isfile(group_by_csv):
			os.remove(group_by_csv)
		if os.path.isfile(png_name):
			os.remove(png_name)
		if os.path.isfile(ocr_name):
			os.remove(ocr_name)


	print 'gridline function complete',datetime.datetime.now()
	if os.path.isfile(pdf_converted):
		return pdf_converted

	# except:
	# 	return "xxxxxxxxxx"


