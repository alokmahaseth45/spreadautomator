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

	# from PIL import Image

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

	x_black_start = 0
	for y in range(h):
		for x in range(w):
			if temp[y][x] > 170 or x >= w-2 or y >= h-2:
				temp[y][x] = 255
		for x in range(w):
			if temp[y][x] < 255:
				if temp[y][x+1] == 255 and x - x_black_start > 30:
					for c in range (x_black_start+1,x+1):
						temp[y][c] = 255
			else:
				x_black_start = x

	y_black_start = 0
	for x in range(w):
		for y in range(h):
			if temp[y][x] < 255:
				if temp[y+1][x] == 255 and y - y_black_start > 10:
					for c in range (y_black_start+1,y+1):
						temp[c][x] = 255
			else:
				y_black_start = y

	##Test Grayscale
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
				if temp[y][x] == 255 and temp[y-1][x] == 255 and temp[y][x+1] == 255 and temp[y][x+2] == 255 and temp[y][x-1] == 255 and temp[y][x-2] == 255 and x < min(line_list[y])-2 and y_white_start in white_list_0:
					if temp[y+1][x] < 255 and y - y_white_start > 100:
						y_end = get_max_value_smaller_than(y,white_list_0)
						draw_line_flag = 0
						for c in range (y_white_start+1,y_end):
							# print x,c,min(black_list[c]),min(line_list[c])
							if min(black_list[c]) > x and min(black_list[c]) < min(line_list[c]):
								draw_line_flag = 1
								break
						if draw_line_flag == 1:
							print 'line',x,y_white_start,y_end-1
							current_line = []
							for c in range(y_white_start+1,y_end):
								line_list[c].append(x)
								# temp[c][x] = 0
								current_line.append(c)
							if x not in line_dict.keys():
								line_dict.update({x:[]})
								line_dict_x_list.append(x)
							line_dict[x].append(current_line)

				else:
					y_white_start = y
				
				if temp[y][x] < 255:
					black_list[y].append(x)

	# print line_list
	# print black_list
	# print line_dict

	# Delete Lines
	for x in reversed(sorted(line_dict_x_list)):
		print 'x',x
		current_line_list = line_dict[x]
		# print current_line_list
		for current_line in current_line_list:
			# print current_line
			for x_a in reversed(sorted(line_dict_x_list)):
				if x_a < x:
					# print 'x_a',x_a
					for current_line_a in line_dict[x_a]:
						subset_flag = 1
						for item in current_line:
							if item not in current_line_a:
								subset_flag = 0
								break
							black_found = 0
							for c in range(x_a,x):
								if c in black_list[item]:
									black_found = 1
									# print item,c,black_list[item]
									break
							if black_found == 1:
								subset_flag = 0
								break
						if subset_flag == 1:
							line_dict[x].remove(current_line)
							print 'deleted',x
							break
					if subset_flag == 1:
						break
	# Run Again 2
	for x in reversed(sorted(line_dict_x_list)):
		print 'x',x
		current_line_list = line_dict[x]
		# print current_line_list
		for current_line in current_line_list:
			# print current_line
			for x_a in reversed(sorted(line_dict_x_list)):
				if x_a < x:
					# print 'x_a',x_a
					for current_line_a in line_dict[x_a]:
						subset_flag = 1
						for item in current_line:
							if item not in current_line_a:
								subset_flag = 0
								break
							black_found = 0
							for c in range(x_a,x):
								if c in black_list[item]:
									black_found = 1
									# print item,c,black_list[item]
									break
							if black_found == 1:
								subset_flag = 0
								break
						if subset_flag == 1:
							line_dict[x].remove(current_line)
							print 'deleted',x
							break
					if subset_flag == 1:
						break

	# Run Again 3
	for x in reversed(sorted(line_dict_x_list)):
		print 'x',x
		current_line_list = line_dict[x]
		# print current_line_list
		for current_line in current_line_list:
			# print current_line
			for x_a in reversed(sorted(line_dict_x_list)):
				if x_a < x:
					# print 'x_a',x_a
					for current_line_a in line_dict[x_a]:
						subset_flag = 1
						for item in current_line:
							if item not in current_line_a:
								subset_flag = 0
								break
							black_found = 0
							for c in range(x_a,x):
								if c in black_list[item]:
									black_found = 1
									# print item,c,black_list[item]
									break
							if black_found == 1:
								subset_flag = 0
								break
						if subset_flag == 1:
							line_dict[x].remove(current_line)
							print 'deleted',x
							break
					if subset_flag == 1:
						break

	# Run Again 4
	for x in reversed(sorted(line_dict_x_list)):
		print 'x',x
		current_line_list = line_dict[x]
		# print current_line_list
		for current_line in current_line_list:
			# print current_line
			for x_a in reversed(sorted(line_dict_x_list)):
				if x_a < x:
					# print 'x_a',x_a
					for current_line_a in line_dict[x_a]:
						subset_flag = 1
						for item in current_line:
							if item not in current_line_a:
								subset_flag = 0
								break
							black_found = 0
							for c in range(x_a,x):
								if c in black_list[item]:
									black_found = 1
									# print item,c,black_list[item]
									break
							if black_found == 1:
								subset_flag = 0
								break
						if subset_flag == 1:
							line_dict[x].remove(current_line)
							print 'deleted',x
							break
					if subset_flag == 1:
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


	print 'Started x grid lines'
	start_flag = 0
	y_white_last = 0
	y_black_last = 0
	y_black_last_line = 0
	x_line_list = []

	print w,h
	for y in range(h):
		x_sum = 0
		# for x in range(w):
		# 	if temp[y][x] > 190:
		# 		temp[y][x] = 255
		for x in range(w):
			if temp[y][x] < 255:
				x_sum = x_sum + temp[y][x] + 1
				start_flag = 1
				break

		if x_sum == 0 and start_flag == 1 and y == y_white_last + 1 and y > y_black_last + 1 and y_black_last > y_black_last_line:
			for x in range(w):
				temp[y][x] = 0
			y_black_last_line = y
			print y
			x_line_list.append(y)

		if x_sum == 0:
			y_white_last = y
		else:
			y_black_last = y


	from pyPdf import PdfFileWriter, PdfFileReader
	import StringIO
	from reportlab.pdfgen import canvas
	from reportlab.lib.pagesizes import letter

	packet = StringIO.StringIO()
	# create a new PDF with Reportlab
	can = canvas.Canvas(packet, pagesize=letter)
	# can = canvas.Canvas(packet)
	# can.setPageSize((1654, 2339))
	# line = "___________________________________________________________________________________"
	# can.drawString(11, 731, line)
	can.setLineWidth(0.6)
	# can.drawString(11, 716, line)
	# can.drawString(11, 701, line)
	# can.drawString(11, 690, line)
	# can.drawString(11, 676, line)
	# can.drawString(11, 662, line)
	# can.drawString(11, 650, line)
	# can.line(484, 148, 484, 716)
	# can.line(451, 179, 451, 731)
	# can.line(327, 179, 327, 731)
	# can.line(292, 179, 292, 731)
	# can.line(47, 495, 47, 701)
	# can.line(47, 215, 47, 474)

	# can.line(15, 715, 570, 715)
	# can.line(15, 700, 570, 700)
	# can.line(15, 689, 570, 689)
	# can.line(15, 675, 570, 675)
	# can.line(15, 661, 570, 661)
	# can.line(15, 649, 570, 649)

	for x in line_dict.keys():
		for current_line in line_dict[x]:
			can.line(x, h-max(current_line), x, h-min(current_line))

	# print x_line_list
	for c in x_line_list:
		can.line(0, h-c, w, h-c)

	can.save()

	#move to the beginning of the StringIO buffer
	packet.seek(0)
	new_pdf = PdfFileReader(packet)
	# read your existing PDF
	existing_pdf = PdfFileReader(file(pdf_name, "rb"))
	output = PdfFileWriter()
	# add the "watermark" (which is the new pdf) on the existing page
	page = existing_pdf.getPage(0)
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


