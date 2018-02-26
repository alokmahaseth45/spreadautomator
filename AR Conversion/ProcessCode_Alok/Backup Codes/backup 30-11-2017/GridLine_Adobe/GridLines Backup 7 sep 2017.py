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

def Convert_png_and_pdf(pdf_name):
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
	# print temp

	# ##Test Grayscale
	# for x in range(w):
	# 	for y in range(h):
	# 		im2.putpixel((x,y),temp[y][x])

	# im2.save("Grey 70c147f0-a430-4b98-99fa-0d3bea4cb781_AURUM Soft_48.png")

	existing_xline_list = [0]
	dummy_line = h
	x_black_start = 0
	for y in range(h):
		for x in range(w):
			if temp[y][x] > 170 or x < 10 or x > w-10 or y < 20 or y > h-20:
				temp[y][x] = 255
		existing_xline_flag = 0
		for x in range(w):
			if temp[y][x] < 255:
				# dummy_line = y
				if temp[y][x+1] == 255 and x - x_black_start > 20:
					existing_xline_flag = 1
					# print 'abc',y
					for c in range (x_black_start+1,x+1):
						temp[y][c] = 255
			else:
				x_black_start = x
		if existing_xline_flag == 1:
			existing_xline_list.append(y)
	print 'existing_xline_list',existing_xline_list


	existing_yline_list = [0]
	y_black_start = 0
	for x in range(w):
		existing_yline_flag = 0
		for y in range(h):
			if temp[y][x] < 255:
				if temp[y+1][x] == 255 and y - y_black_start > 10:
					if y - y_black_start > 15:
						existing_yline_flag = 1
					for c in range (y_black_start+1,y+1):
						temp[c][x] = 255
			else:
				y_black_start = y
		if existing_yline_flag == 1:
			existing_yline_list.append(x)
	print 'existing_yline_list',existing_yline_list


	for y in range(1,h-1):
		for x in range(1,w-1):
			if temp[y][x] < 255 and temp[y][x+1] == 255 and temp[y][x-1] == 255 and temp[y+1][x] == 255 and temp[y+1][x+1] == 255 and temp[y+1][x-1] == 255 and temp[y-1][x] == 255 and temp[y-1][x+1] == 255 and temp[y-1][x-1] == 255:
				temp[y][x] = 255
			if temp[y][x] < 255:
				dummy_line = y

	print 'dummy_line',dummy_line
	for x in range(2,w-2):
		temp[dummy_line][x] = 0


	##Test Grayscale
	if test_flag == 1:
		for x in range(w):
			for y in range(h):
				im2.putpixel((x,y),temp[y][x])
		im2.save("Grey.png")

	def get_max_value_smaller_than(s,alist):
		last_val = s
		return_val = max(alist)
		for val in sorted(alist):
			if val > s:
				return_val = last_val
				break
			last_val = val
		return return_val

	def get_min_value_greater_than(s,alist):
		last_val = s
		return_val = min(alist)
		for val in reversed(sorted(alist)):
			if val < s:
				return_val = last_val
				break
			last_val = val
		return return_val

	no_line_list_gap = 30


	print 'Started x grid lines'
	start_flag = 0
	y_white_last = 0
	y_black_last = 0
	y_black_last_line = 0
	x_line_list = []
	x_last_line = 0
	no_line_list = []
	x_dot_count_last = 0

	print w,h
	for y in range(h):
		x_sum = 0
		x_dot_count = 0
		# for x in range(w):
		# 	if temp[y][x] > 190:
		# 		temp[y][x] = 255
		for x in range(w):
			if temp[y][x] < 255:
				x_dot_count = x_dot_count + 1

			if temp[y][x] < 255 and temp[y][x+1] < 255:
				x_sum = x_sum + temp[y][x] + 1
				start_flag = 1
				break

		if x_sum == 0 and start_flag == 1 and y == y_white_last + 1 and y > y_black_last + 1 and y_black_last > y_black_last_line:
			
			if y-y_black_last_line < 6:
				x_line_list.remove(y_black_last_line)
				print 'removed',y_black_last_line
			
			existing_xline = get_min_value_greater_than(y,existing_xline_list)

			if existing_xline - y < 7:
				y = existing_xline
				print 'matched with existing x line',y
			
			y_black_last_line = y
			print y
			x_line_list.append(y)

			if y - x_last_line > no_line_list_gap:
				for c in range(x_last_line+1,y-12):
					no_line_list.append(c)

			x_last_line = y

		elif x_sum > 0 and start_flag == 1 and y == y_white_last + 1 and y > y_black_last + 1 and y_black_last > y_black_last_line and y-y_black_last_line > 5 and x_dot_count_last <= 2:
			existing_xline = get_min_value_greater_than(y-1,existing_xline_list)

			if existing_xline - y-1 < 5:
				y = existing_xline + 1
				print 'matched with existing line',y-1

			y_black_last_line = y-1
			print y-1
			x_line_list.append(y-1)

			if y-1 - x_last_line > no_line_list_gap:
				for c in range(x_last_line+1,y-1-12):
					no_line_list.append(c)

			x_last_line = y-1

		if x_sum == 0:
			y_white_last = y
		else:
			y_black_last = y

		x_dot_count_last = x_dot_count

	print 'no_line_list',no_line_list


	print 'Started y grid lines'
	print 'existing_yline_list',existing_yline_list
	white_list_0 = []
	black_list_0 = []
	for y in range(h):
		x_sum = 0
		# for x in range(w):
		# 	if temp[y][x] > 190:
		# 		temp[y][x] = 255
		for x in range(w):
			if temp[y][x] < 255:
				x_sum = x_sum + temp[y][x] + 1
				break
		if x_sum == 0:
			white_list_0.append(y)
		else:
			black_list_0.append(y)
	# print 'white_list_0',white_list_0
	# print 'black_list_0',black_list_0

	start_flag = 0
	black_list = {}
	line_list = {}
	min_black_list_0 = min(black_list_0)
	line_dict = {}
	line_dict_x_list = []

	for x in range(w-1,0,-1):
		y_white_start = min_black_list_0
		# line_dict.update({x:[]})
		# line_list.update({x:[]})
		# black_list.update({x:[]})
		for y in range(h):
			# if temp[y][x] > 190:
			# 	temp[y][x] = 255
			if x == w-1:
				line_list.update({y:[w]})
				black_list.update({y:[w]})
			if temp[y][x] < 255:
				start_flag = 1
		if start_flag == 1:
			for y in range(y_white_start,h-1):
				line_counter = 0
				# print x,y,temp[y][x],temp[y-1][x],min(line_list[y]),min(black_list[y])
				# if temp[y][x] == 255 and temp[y-1][x] == 255 and x < min(line_list[y])-5 and x < min(black_list[y]) - 1 and temp[y][x-1] == 255 and temp[y][x-2] == 255 and y_white_start in white_list_0:
				
				# if temp[y][x] == 255 and temp[y-1][x] == 255 and temp[y][x+1] == 255 and temp[y][x+2] == 255 and temp[y][x-1] == 255 and temp[y][x-2] == 255 and x < min(line_list[y])-2 and y_white_start in white_list_0:
				if temp[y][x] == 255 and temp[y-1][x] == 255 and temp[y][x+1] == 255 and temp[y][x+2] == 255 and temp[y][x-1] == 255 and temp[y][x-2] == 255 and x < min(line_list[y])-2 and y_white_start in white_list_0 and y not in no_line_list:
					# if temp[y+1][x] < 255 and y - y_white_start > 100:
					if (temp[y+1][x] < 255 or y+1 in no_line_list) and y - y_white_start > 100:
						y_end = get_max_value_smaller_than(y,white_list_0)
						draw_line_flag = 0
						for c in range (y_white_start+1,y_end):
							# print x,c,min(black_list[c]),min(line_list[c])
							if min(black_list[c]) > x and min(black_list[c]) < min(line_list[c]):
								draw_line_flag = 1
								break
						if draw_line_flag == 1:

							existing_yline1 = get_max_value_smaller_than(x,existing_yline_list)
							existing_yline2 = get_min_value_greater_than(x,existing_yline_list)

							if x - existing_yline1 > 0 and x - existing_yline1 <= 15:
								x_new = existing_yline1
								print 'matched with existing y line',x,x_new,existing_yline1
							elif existing_yline2 - x > 0 and existing_yline2 - x <= 15:
								x_new = existing_yline2
								print 'matched with existing y line',x,x_new,existing_yline2
							else:
								x_new = x

							print 'line',x_new,y_white_start,y_end-1
							current_line = []
							for c in range(y_white_start+1,y_end):
								line_list[c].append(x_new)
								# temp[c][x] = 0
								current_line.append(c)
							if x_new not in line_dict.keys():
								line_dict.update({x_new:[]})
								line_dict_x_list.append(x_new)
							line_dict[x_new].append(current_line)

							# print 'line',x,y_white_start,y_end-1
							# current_line = []
							# for c in range(y_white_start+1,y_end):
							# 	line_list[c].append(x)
							# 	# temp[c][x] = 0
							# 	current_line.append(c)
							# if x not in line_dict.keys():
							# 	line_dict.update({x:[]})
							# 	line_dict_x_list.append(x)
							# line_dict[x].append(current_line)

				else:
					y_white_start = y
				
				if temp[y][x] < 255:
					black_list[y].append(x)

	# print line_list
	# print black_list
	# print line_dict

	# Delete Lines

	# col_del_flag = 1
	# while col_del_flag == 1:
	# 	col_del_flag = 0
	# 	for x in reversed(sorted(line_dict_x_list)):
	# 		print 'x',x
	# 		current_line_list = line_dict[x]
	# 		# print current_line_list
	# 		for current_line in current_line_list:
	# 			# print current_line
	# 			for x_a in reversed(sorted(line_dict_x_list)):
	# 				if x_a < x:
	# 					# print 'x_a',x_a
	# 					for current_line_a in line_dict[x_a]:
	# 						subset_flag = 1
	# 						for item in current_line:
	# 							if item not in current_line_a:
	# 								subset_flag = 0
	# 								break
	# 							black_found = 0
	# 							for c in range(x_a,x):
	# 								if c in black_list[item]:
	# 									black_found = 1
	# 									# print item,c,black_list[item]
	# 									break
	# 							if black_found == 1:
	# 								subset_flag = 0
	# 								break
	# 						if subset_flag == 1:
	# 							line_dict[x].remove(current_line)
	# 							print 'deleted',x
	# 							col_del_flag = 1
	# 							break
	# 					if subset_flag == 1:
	# 						break


	col_del_flag = 1
	while col_del_flag == 1:
		col_del_flag = 0
		for x in reversed(sorted(line_dict_x_list)):
			print 'x',x
			current_line_list = line_dict[x]
			# print current_line_list
			for current_line in current_line_list:
				# print current_line
				for x_a in reversed(sorted(line_dict_x_list)):
					subset_flag = 0
					if x_a < x and line_dict[x]:
						# print 'x_a',x_a
						for current_line_a in line_dict[x_a]:
							if min(current_line_a) >= min(current_line) and max(current_line_a) <= max(current_line):
								subset_flag = 2
							elif min(current_line) >= min(current_line_a) and max(current_line) <= max(current_line_a):
								subset_flag = 1
							else:
								subset_flag = 0
							
							black_found = 0
							overlap_len = 0
							for item in current_line:
								if item in current_line_a:
									for c in range(x_a,x):
										if c in black_list[item]:
											black_found = black_found + 1
											# print item,c,black_list[item]
											break
									overlap_len = overlap_len + 1
							# print x,x_a,subset_flag,black_found
							# if x == 355:
							# 	print subset_flag,'overlap_len',overlap_len,max(current_line),min(current_line),float(overlap_len/float(max(current_line)-min(current_line))),black_found
							if (subset_flag == 1 or float(overlap_len/float(max(current_line)-min(current_line))) > 0.8) and black_found < 15 and subset_flag != 2:
								subset_flag == 1
								line_dict[x].remove(current_line)
								print 'deleted x',x
								col_del_flag = 1
								print 'break line loop'
								break
							if subset_flag == 2 and black_found < 20:
								line_dict[x_a].remove(current_line_a)
								print 'deleted x_a',x_a
								col_del_flag = 1
								# break
						if subset_flag == 1:
							print 'break dict loop'
							break


	# print line_dict
	# for x in line_dict.keys():
	# 	for current_line in line_dict[x]:
	# 		for y in current_line:
	# 			temp[y][x] = 0

	# for x in range(w):
	# 	for y in range(h):
	# 		im2.putpixel((x,y),temp[y][x])

	# im2.save("Test noxlines Pages from b1bf86a6-73d7-4f99-aa96-d19e26f42006_ABB.png")



	if test_flag == 1:
		for x in line_dict.keys():
			for current_line in line_dict[x]:
				for y in current_line:
					temp[y][x] = 0

		for y in x_line_list:
			for x in range(w):
				temp[y][x] = 0

		for x in range(w):
			for y in range(h):
				im2.putpixel((x,y),temp[y][x])

		im2.save("Test " + png_name)

	from PyPDF2 import PdfFileWriter, PdfFileReader
	# from pyPdf import PdfFileWriter, PdfFileReader
	import StringIO
	from reportlab.pdfgen import canvas
	from reportlab.lib.pagesizes import letter

	# print 'letter',type(letter),letter
	existing_pdf = PdfFileReader(file(pdf_name, "rb"))
	page = existing_pdf.getPage(0)
	main_x = float(page.trimBox.getUpperRight_x())
	main_y = float(page.trimBox.getUpperRight_y())
	main_x_offset = float(page.trimBox.getLowerLeft_x())
	main_y_offset = float(page.trimBox.getLowerLeft_y())
	main_x_media_offset = float(page.mediaBox.getLowerLeft_x())
	main_y_media_offset = float(page.mediaBox.getLowerLeft_y())
	print 'existing_pdf',page.mediaBox,page.trimBox

	packet = StringIO.StringIO()
	# create a new PDF with Reportlab
	# can = canvas.Canvas(packet, pagesize=letter)
	can = canvas.Canvas(packet, pagesize=(main_x-main_x_offset, main_y-main_y_offset))
	# line = "___________________________________________________________________________________"
	# can.drawString(11, 731, line)
	can.setLineWidth(0.6)

	# can.line(15, 649, 570, 649)
	# can.drawString(600, 10, '|AA|')

	for x in line_dict.keys():
		for current_line in line_dict[x]:
			can.line(x+main_x_offset+main_x_media_offset, h-max(current_line)+main_y_offset+main_y_media_offset, x+main_x_offset+main_x_media_offset, h-min(current_line)+main_y_offset+main_y_media_offset)
			# can.line(x+(main_x-main_x_offset-w)/2+main_x_offset, h-max(current_line)+((main_y-main_y_offset-h)/2)+main_y_offset-1, x+(main_x-main_x_offset-w)/2+main_x_offset, h-min(current_line)+((main_y-main_y_offset-h)/2)+main_y_offset-1)
			# can.line(x+(main_x-w)/2, h-max(current_line)+((main_y-h)/2), x+(main_x-w)/2, h-min(current_line)+((main_y-h)/2))
			# can.line(x, h-max(current_line), x, h-min(current_line))
		# if line_dict[x]:
		# 	can.drawString(x+main_x_offset+main_x_media_offset, h-50, str(x))

	# can.line(1, 1, 1, 200)
	# can.line(45, 1, 45, 200)
	# can.line(559, 1, 559, 200)
	# can.line(590, 750, 590, 751)
	# can.line(0, 761, 1, 761)
	# can.line(1, 760, 500, 760)

	for c in x_line_list:
		can.line(0+main_x_offset+main_x_media_offset, h-c+main_y_offset+main_y_media_offset, w+main_x_offset+main_x_media_offset, h-c+main_y_offset+main_y_media_offset)
		# can.line((main_x-main_x_offset-w)/2+main_x_offset, h-c+((main_y-main_y_offset-h)/2)+main_y_offset-1, w+(main_x-main_x_offset-w)/2+main_x_offset, h-c+((main_y-main_y_offset-h)/2)+main_y_offset-1)
		# can.line((main_x-w)/2, h-c+((main_y-h)/2)-1, w+(main_x-w)/2, h-c+((main_y-h)/2)-1)
		# can.line(0, h-c, w, h-c)
		# can.drawString(50, h-c+main_y_offset+main_y_media_offset, str(c))

	can.save()

	#move to the beginning of the StringIO buffer
	packet.seek(0)
	new_pdf = PdfFileReader(packet)
	# for testing only
	if test_flag == 1:
		page_new = new_pdf.getPage(0)
		print 'Only_Lines',page_new.mediaBox,page_new.trimBox
		output_new = PdfFileWriter()
		output_new.addPage(page_new)
		output_new.write(file("Only_Lines_" + pdf_name, "wb"))
	# 612 792


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


